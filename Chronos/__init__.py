import bl2sdk
import random

class Chronos(bl2sdk.BL2MOD):
	Name = "Chronos"
	Description = "Replaces the Skullmasher with Chronos, a sniper Rifle that slows down time while aiming down sights. Zooming out randomizes your weapons skin."
	Author = "Juso"

	#This function is used to alter the weapons stats and also change its name and red text.
	def PartChanges(self):
		ChronosBarrel = bl2sdk.FindObject("WeaponPartDefinition", "GD_Weap_SniperRifles.Barrel.SR_Barrel_Jakobs_Skullmasher")
		ChronosTitle = bl2sdk.FindObject("WeaponNamePartDefinition", "GD_Weap_SniperRifles.Name.Title_Jakobs.Title_Legendary_Skullmasher")
		ChronosRedText = bl2sdk.FindObject("AttributePresentationDefinition", "GD_Weap_SniperRifles.Name.Title_Jakobs.Title_Legendary_Skullmasher:AttributePresentationDefinition_8")
		ChronosTitle.PartName = "Chronos"
		ChronosRedText.NoConstraintText = "ZA WARUDO!"
		#Change the actual weapon stats
		'''
		ModifierType = 0 -> MT_Scale
		ModifierType = 1 -> MT_PreAdd
		ModifierType = 2 -> MT_PostAdd
		'''
		#setting the clip size to 1
		ClipSize = bl2sdk.FindObject("AttributeDefinition", "D_Attributes.Weapon.WeaponClipSize")
		ChronosBarrel.WeaponAttributeEffects[0].AttributeToModify = ClipSize
		ChronosBarrel.WeaponAttributeEffects[0].ModifierType = 0
		#ChronosBarrel.WeaponAttributeEffects[0].BaseModifierValue.BaseValueConstant = -100000000.000000
		ChronosBarrel.WeaponAttributeEffects[3].AttributeToModify = ClipSize
		ChronosBarrel.WeaponAttributeEffects[3].ModifierType = 2
		ChronosBarrel.WeaponAttributeEffects[3].BaseModifierValue.BaseValueConstant = 1.000000
		#increasing the damage
		ChronosBarrel.WeaponAttributeEffects[1].BaseModifierValue.BaseValueConstant = 1.000000
		#change shot impulse to crit damage
		CritDamage = bl2sdk.FindObject("AttributeDefinition", "D_Attributes.GameplayAttributes.PlayerCriticalHitBonus")
		ChronosBarrel.WeaponAttributeEffects[2].AttributeToModify = CritDamage
		ChronosBarrel.WeaponAttributeEffects[2].ModifierType = 0
		ChronosBarrel.WeaponAttributeEffects[2].BaseModifierValue.BaseValueConstant = 1.000000

	def GetPlayerController(self):
		return bl2sdk.GetEngine().GamePlayers[0].Actor

	#This function contains a list of all Sniper skins in the game, its used to randomly chose any of these skins as a template for Chronos Skin.
	def GetRandomSkin(self):
		SniperSkins = [
			"Aster_GunMaterials.Materials.Mati_VladofCommonSR_Patriot",
			"Aster_GunMaterials.Materials.sniper.Mati_Dahl_Emerald_Sniper",
			"Aster_GunMaterials.Materials.sniper.Mati_Hyperion_Diamond_Sniper",
			"Aster_GunMaterials.Materials.sniper.Mati_Jakobs_Citrine_Sniper",
			"Aster_GunMaterials.Materials.sniper.Mati_Maliwan_Aquamarine_Sniper",
			"Aster_GunMaterials.Materials.sniper.Mati_Vladof_Garnet_Sniper",
			"Common_GunMaterials.Materials.sniper.Mati_DahUniqueSR_Sloth",
			"Common_GunMaterials.Materials.sniper.Mati_DahlCommonSR",
			"Common_GunMaterials.Materials.sniper.Mati_DahlEpicSR",
			"Common_GunMaterials.Materials.sniper.Mati_DahlLegendarySRPitchfork",
			"Common_GunMaterials.Materials.sniper.Mati_DahlRareSR",
			"Common_GunMaterials.Materials.sniper.Mati_DahlUncommonSR",
			"Common_GunMaterials.Materials.sniper.Mati_GearboxSR",
			"Common_GunMaterials.Materials.sniper.Mati_HyperionCommonSR",
			"Common_GunMaterials.Materials.sniper.Mati_HyperionEpicSR",
			"Common_GunMaterials.Materials.sniper.Mati_HyperionLegendarySRInvader",
			"Common_GunMaterials.Materials.sniper.Mati_HyperionRareSR",
			"Common_GunMaterials.Materials.sniper.Mati_HyperionUncommonSR",
			"Common_GunMaterials.Materials.sniper.Mati_HyperionUniqueSR_FremingtonsEdge",
			"Common_GunMaterials.Materials.sniper.Mati_HyperionUniqueSR_Longbow",
			"Common_GunMaterials.Materials.sniper.Mati_HyperionUniqueSR_Morningstar",
			"Common_GunMaterials.Materials.sniper.Mati_JakobsCommonSR",
			"Common_GunMaterials.Materials.sniper.Mati_JakobsEpicSR",
			"Common_GunMaterials.Materials.sniper.Mati_JakobsLegendarySRSkullmasher",
			"Common_GunMaterials.Materials.sniper.Mati_JakobsRareSR",
			"Common_GunMaterials.Materials.sniper.Mati_JakobsUncommonSR",
			"Common_GunMaterials.Materials.sniper.Mati_JakobsUniqueSR_Buffalo",
			"Common_GunMaterials.Materials.sniper.Mati_JakobsUniqueSR_Tresspasser",
			"Common_GunMaterials.Materials.sniper.Mati_MaliwanCommonSR",
			"Common_GunMaterials.Materials.sniper.Mati_MaliwanEpicSR",
			"Common_GunMaterials.Materials.sniper.Mati_MaliwanLegendarySRVolcano",
			"Common_GunMaterials.Materials.sniper.Mati_MaliwanRareSR",
			"Common_GunMaterials.Materials.sniper.Mati_MaliwanUncommonSR",
			"Common_GunMaterials.Materials.sniper.Mati_MaliwanUniqueSR_ChereAmie",
			"Common_GunMaterials.Materials.sniper.Mati_VladofCommonSR",
			"Common_GunMaterials.Materials.sniper.Mati_VladofEpicSR",
			"Common_GunMaterials.Materials.sniper.Mati_VladofLegendarySRLyudmila",
			"Common_GunMaterials.Materials.sniper.Mati_VladofRareSR",
			"Common_GunMaterials.Materials.sniper.Mati_VladofUncommonSR",
			"Gladiolus_GunMaterials.Materials.sniper.Mati_Maliwan_6_Storm",
			"Iris_GunMaterials.Materials.sniper.Mati_JakobsUniqueSR_Cobra",
			"Lobelia_GunMaterials.Materials.sniper.Mati_Jakobs_Pearl_Godfinger",
			"Orchid_GunMaterials.Materials.sniper.Mati_MaliwanRareSR_Pimpernel",
			"Orchid_GunMaterials.Materials.sniper.Mati_VladofCommonSR_Patriot",
			"Sage_GunMaterials.Materials.sniper.Mati_JakobsCommonSR_ElephantGun",
			"Sage_GunMaterials.Materials.sniper.Mati_JakobsRaidSR_HawkEye"
			]
		return random.choice(SniperSkins)

	#This function gets called everytime the player unzooms the chronos, it will then randomly change the weapons skin
	#It uses one random already existing sniper skin as a template. It copys all the values from the template to its own skin.
	#Search first for the Material of the Skullmasher
	ChronosMaterial = bl2sdk.FindObject("MaterialInstanceConstant", "Common_GunMaterials.Materials.sniper.Mati_JakobsLegendarySRSkullmasher")
	def RandomizeWeaponSkin(self):
		#Find the MaterialInstanceConstant of Random Skin
		RandomMaterial = bl2sdk.FindObject("MaterialInstanceConstant", self.GetRandomSkin())

		#Some skins use a parent skin as a template, in that case copy its values first!
		if not RandomMaterial.Parent.Name == "Master_Gun":
			#print("Material Parent:")
			#print(RandomMaterial.Parent)
			for temp in RandomMaterial.Parent.VectorParameterValues:
				color = (temp.ParameterValue.R, temp.ParameterValue.G, temp.ParameterValue.B, temp.ParameterValue.A)
				self.ChronosMaterial.SetVectorParameterValue(temp.ParameterName, color)
			for temp in RandomMaterial.Parent.TextureParameterValues:
				if not temp.ParameterValue == None:
					self.ChronosMaterial.SetTextureParameterValue(temp.ParameterName, temp.ParameterValue)
			for temp in RandomMaterial.Parent.ScalarParameterValues:
				self.ChronosMaterial.SetScalarParameterValue(temp.ParameterName, temp.ParameterValue)
		#print("Material:")
		#print(RandomMaterial)
		for temp in RandomMaterial.VectorParameterValues:
			color = (temp.ParameterValue.R, temp.ParameterValue.G, temp.ParameterValue.B, temp.ParameterValue.A)
			self.ChronosMaterial.SetVectorParameterValue(temp.ParameterName, color)
		for temp in RandomMaterial.TextureParameterValues:
			if not temp.ParameterValue == None:
				self.ChronosMaterial.SetTextureParameterValue(temp.ParameterName, temp.ParameterValue)
		for temp in RandomMaterial.ScalarParameterValues:
			self.ChronosMaterial.SetScalarParameterValue(temp.ParameterName, temp.ParameterValue)



	SkullMasherBarrel = bl2sdk.FindObject("WeaponPartDefinition", "GD_Weap_SniperRifles.Barrel.SR_Barrel_Jakobs_Skullmasher")

	def HandleZooming(self, caller, function, params):
		#Get the speed of the Player Pawn, needs to be increased while aiming
		PlayerPawn = self.GetPlayerController().Pawn
		if caller.Instigator == PlayerPawn:
			#BaseSpeed = PlayerPawn.GroundSpeed
			if PlayerPawn.Weapon.DefinitionData.BarrelPartDefinition == self.SkullMasherBarrel:
				#Get the Current Worlinfo to set the timedilation
				WorldInfo = bl2sdk.GetEngine().GetCurrentWorldInfo()
				#1==Zooming in / 2==Zoomed in / 3==Zooming out / 0==Not Zoomed
				#Only slow time while zooming in
				if params.NewZoomState in (1, 2):
					WorldInfo.TimeDilation = 0.4500000
					#PlayerPawn.GroundSpeed *= 1.5
					self.RandomizeWeaponSkin()
				elif params.NewZoomState == 0:
					WorldInfo.TimeDilation = 1.0000000
					#PlayerPawn.GroundSpeed = BaseSpeed
			else:
				pass
		else:
			pass

	#Checks if weapon is zoomed in
	#Hooks the games SetZoomState function
	ZoomHook = "WillowGame.WillowWeapon.SetZoomState"
	def Enable(self):
		self.PartChanges()
		bl2sdk.RegisterHook(self.ZoomHook, "ZoomHook", IsZoomingHook)
	def Disable(self):
		bl2sdk.RemoveHook(self.ZoomHook, "ZoomHook")


ChronosInstance = Chronos()

#This function gets called everytime the player starts to change the zoom status
def IsZoomingHook(caller: bl2sdk.UObject, function: bl2sdk.UFunction, params: bl2sdk.FStruct) -> bool:
	ChronosInstance.HandleZooming(caller, function, params)
	return True


bl2sdk.Mods.append(ChronosInstance)