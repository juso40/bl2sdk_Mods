import bl2sdk
import datetime

class DPS(bl2sdk.BL2MOD):

	Name = "DPS/TTK Calculator"
	Description = "Upon damaging an enemy a counter will start in the background. On kill it will then calculate the " \
				  "DPS in that amount of time, from dealing damage to the kill. The longer you need to kill an enemy " \
				  "the more precise the DPS actually is. "
	Author = "Juso"
	_started_at = datetime.datetime.utcnow()
	_DamagedEnemy = False

	#Returns the current WillowPlayerController
	def GetPlayerController(self):
		return bl2sdk.GetEngine().GamePlayers[0].Actor
	
	def DPSFeedback(self, EnemyName):
		#This gets the Players HUD
		playerController = self.GetPlayerController()
		HUDMovie = playerController.GetHUDMovie()
		time_passed = datetime.datetime.utcnow() - self._started_at
		DPSCalcString = str(int(self._CombinedDamage/time_passed.total_seconds()))+" DPS"
		#This First clears the old message and then rewrites the new one
		HUDMovie.ClearTrainingText()
		HUDMovie.AddTrainingText("Dealt: "+str(int(self._CombinedDamage))+" in "+str(time_passed.total_seconds())+" seconds", DPSCalcString, 10.000000, (), "", False, 0, playerController.PlayerReplicationInfo, True)
	_CombinedDamage = 0
	def HandleKill(self, caller, function, params):
		self._DamagedEnemy = False
		self.DPSFeedback(params.EnemyName)
		self._CombinedDamage = 0
		return True
		
	def HandleDamage(self, caller, function, params):
		if params.InDamageInstigator == self.GetPlayerController():
			self._DamagedEnemy = True
			self._started_at = datetime.datetime.utcnow()
			self._CombinedDamage += params.IncomingDamage
		return True	
		
	def DamagedEnemy(self):
		return self._DamagedEnemy
		
	KillHook = "WillowGame.WillowPlayerController.NotifyKilledEnemy"
	DamagedHook = "WillowGame.WillowDamagePipeline.AdjustDamage"
	def Enable(self):
		bl2sdk.RegisterHook(self.KillHook, "KillHook", KilledHook)
		bl2sdk.RegisterHook(self.DamagedHook, "DamagedHook", DamageHook)
	def Disable(self):
		bl2sdk.RemoveHook(self.KillHook, "KillHook")
		bl2sdk.RemoveHook(self.DamagedHook, "DamagedHook")

DPSInstance = DPS()

def KilledHook(caller: bl2sdk.UObject, function: bl2sdk.UFunction, params: bl2sdk.FStruct) -> bool:
	DPSInstance.HandleKill(caller, function, params)
	return True

def DamageHook(caller: bl2sdk.UObject, function: bl2sdk.UFunction, params: bl2sdk.FStruct) -> bool:
	if DPSInstance.DamagedEnemy() == False:
		DPSInstance.HandleDamage(caller, function, params)	
	return True


bl2sdk.Mods.append(DPSInstance)
