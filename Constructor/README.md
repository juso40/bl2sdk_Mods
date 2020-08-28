# Constructor
[PythonSDK](https://github.com/bl-sdk/PythonSDK) Mod/Ressource that allows the easy creation and use of new non replacing Objects.

## Installation
1. Download and install [PythonSDK](https://github.com/bl-sdk/PythonSDK)  
2. Download this mod by downloading the provided `.zip`  
3. Extract the `.zip` archive into the `/Binaries/Win32/Mods` directory of your game.
4. To enable the mod go start the game, go to `Mods` menu and press `Enter` on the `Constructor`  

## Installing constructor addons/Non replacing mods
Simply place the provided files/folders anywhere inside `/Binaries/Win32/Mods/Constructor`.  
The names of the files do not really matter, as most mods will add new objects, so they won't overwrite each other and
shouldn't cause any compatibility issues.  
If you do care about load order, the files will be loaded in alphabetical order of their respective directory.

## Using normal text mods alongside of the Constructor
As always, use BLCMM to configure your mods and decrease compatibility issues. 
After you are done in BLCMM make sure the files extension is `.blcm` and then place the file inside of the `Constructor` directory.  
It's basically the same as with constructor addons/Non replacing mods. Load order of the `.blcm` files is again, alphabetically.
The `.blcm` mods will then automatically be merged and enabled. 

## FAQ
- Can I use gibbeds Save editor to acquire new objects? 
  - No, all your items will be stored in a `.json` file instead of the `.sav` file the game uses. You can open this `.json` with any text editor and simply give yourself any item you want, but you will need to know the parts object name.
- Do I need all DLCs to use this mod?
  - No, you only need the base game. But if you plan on using an addon that uses an DLC item as its base, then you will ofc need the DLC to use this new item.
- Why does my game crash when I throw a grenade?
  - This is related to multiple objects having the same name. So you either have a duplicate copy of an addon inside the Constructor directory or one of the addons you use has a bug/duplicate entry.
- Does this work in coop?
  - No.

## Getting Addons
- No Addons have currently been uploaded. If you've created a Repo or mod page with your creations message me, and I'll happily add it to this list :)

### Contact me
- Discord `juso#6352`
- Discord servers that can help you:
  - [Borderlands 2 Modding](https://discord.gg/DK74kjy)
  - [BL: Exodus](https://discord.gg/tdK5MGK)
  