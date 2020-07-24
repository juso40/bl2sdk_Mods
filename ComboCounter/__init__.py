import bl2sdk
import datetime
import random

class ComboCounter(bl2sdk.BL2MOD):

	Name = "Kill Combo Counter"
	Description = "Adds a Kill Combo Counter to your screen.\nAfter 6 seconds of no killing the combo will vanish.\nThe higher the Combo the more additional exp you gain on kill."
	Author = "Juso"
	_started_at = datetime.datetime.utcnow()
	KillCounter = 0
	#This is our timer function it gets called with the Instance of this class. In this case its ComboInstance()
	def __call__(self):
		time_passed = datetime.datetime.utcnow() - self._started_at
		#If 6 seconds are up, then reset the Kill Counter
		if time_passed.total_seconds() > 6:
			self.KillCounter = 0
			return False
		return True

	#Returns the current WillowPlayerController
	def GetPlayerController(self):
		return bl2sdk.GetEngine().GamePlayers[0].Actor

	def PlayAudio(self):
		AkEvents = [
				"Ake_VOCT_Contextual.Ak_Play_VOCT_GuiltGun_Killed_Enemy",
				"Ake_VOCT_Contextual.Ak_Play_VOCT_Fink_CoS_Arena_Win",
				"Ake_VOCT_Contextual.Ak_Play_VOCT_Loader1340_Killed_Enemy",
				"Ake_VOCT_Contextual.Ak_Play_VOCT_Loader1340_One_Shot_Kill",
				"Ake_VOCT_Contextual.Ak_Play_VOCT_CaptCabrera_CoS_Arena_Win",
				"Ake_VOCT_Contextual.Ak_Play_VOCT_IndoBot5K_CoS_Arena_Win",
				"Ake_VOCT_Contextual.Ak_Play_VOCT_Fink_CoS_Arena_Round_Commence",
				"Ake_VOCT_Contextual.Ak_Play_VOCT_Fink_CoS_Arena_Round_Begin"
				]
		MakeNoise = bl2sdk.FindObject("AkEvent", random.choice(AkEvents))
		PlayerController = self.GetPlayerController()
		PlayerController.PlayAkEvent(MakeNoise)
	
	def ComboFeedback(self, EnemyName):
		ComboNames = [
				"First Blood",
				"Double Kill",
				"Triple Kill",
				"Overkill",
				"Multi Kill",
				"Monster Kill",
				"Ultra Kill",
				"Killing Spree",
				"Killtrocity",
				"Killamanjaro",
				"Killtastrophe",
				"Killpocalypse",
				"Godlike",
				"Unstoppable!",
				"Unfriggenbelievable"
				]
		if self.KillCounter < len(ComboNames)+1:
			ComboName = ComboNames[self.KillCounter-1]
		else:
			ComboName = ComboNames[-1]
		#This gets the Players HUD
		playerController = self.GetPlayerController()
		HUDMovie = playerController.GetHUDMovie()
		#This is the Title of the Combo Counter
		KillString = str(self.KillCounter) + " Kills\n\nLast Killed Enemy: " + EnemyName
		#This First clears the old message and then rewrites the new one
		HUDMovie.ClearTrainingText()
		HUDMovie.AddTrainingText(KillString, ComboName, 6.000000, (), "", False, 0, playerController.PlayerReplicationInfo, True)
		
	#We reset our timer
	#then increase the kill counter by one, because a kill happened
	def KillCombo(self, caller, function, params):
		self._started_at = datetime.datetime.utcnow()
		self.KillCounter+=1
		
		#Optional Extra Experience
		bl2sdk.GetEngine().GamePlayers[0].Actor.ExpEarn(int(self.KillCounter**2.8),0)
		
		#50% chance to trigger an AkEvent
		if random.randint(0, 100) > 50:
			self.PlayAudio()
		self.ComboFeedback(params.EnemyName)
		return True
		
	KillHook = "WillowGame.WillowPlayerController.NotifyKilledEnemy"
	def Enable(self):
		bl2sdk.RegisterHook(self.KillHook, "KillHook", KillComboHook)
	def Disable(self):
		bl2sdk.RemoveHook(self.KillHook, "KillHook")

ComboInstance = ComboCounter()

def KillComboHook(caller: bl2sdk.UObject, function: bl2sdk.UFunction, params: bl2sdk.FStruct) -> bool:
	ComboInstance()
	ComboInstance.KillCombo(caller, function, params)
	return True


bl2sdk.Mods.append(ComboInstance)
