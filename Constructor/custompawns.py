import os
from typing import Tuple

import unrealsdk
from unrealsdk import *

from . import bl2tools
from . import hookmanager
from . import logging, set_iterpreter
from . import matinstconsts


@logging.log_all_calls(logging.call_logger)
class Pawns:

    def __init__(self, path: os.PathLike):
        self.PATH = path
        self.pop_files = []
        self.pawn_files = []
        self.is_game_bl2 = unrealsdk.FindObject("Object",
                                                "GD_Itempools.Runnables.Pool_Bunker") is not None

    def Enable(self) -> None:
        hookmanager.instance.register_end_load(self.on_end_load, 0)
        hookmanager.instance.register_start_load(self.on_start_load, 999)
        self.load_files()

    def Disable(self) -> None:
        pass

    def on_start_load(self, movie_name: str) -> None:
        pass

    def on_end_load(self, curr_map: str) -> None:
        if logging.logger.level in logging.logger.levels[:2]:
            self.load_files()

        self.construct_custom_pawn(curr_map)
        self.fake_hotfix_popdef(curr_map)

    def load_files(self) -> None:
        self.pop_files.clear()
        self.pawn_files.clear()
        for root, dirs, filenames in os.walk(self.PATH):
            for file in filenames:
                if file.lower().endswith(".pawn"):
                    self.pawn_files.append(os.path.join(root, file))
                elif file.lower().endswith(".popdef"):
                    self.pop_files.append(os.path.join(root, file))

    def append_popdef(self, pop_def: unrealsdk.UObject, new_actor: Tuple[unrealsdk.UObject,
                                                                         Tuple[float,
                                                                               unrealsdk.UObject,
                                                                               unrealsdk.UObject,
                                                                               float],
                                                                         Tuple[float,
                                                                               unrealsdk.UObject,
                                                                               unrealsdk.UObject,
                                                                               float],
                                                                         float, float]
                      ) -> None:
        actor_list = [(actor.SpawnFactory, (actor.Probability.BaseValueConstant,
                                            actor.Probability.BaseValueAttribute,
                                            actor.Probability.InitializationDefinition,
                                            actor.Probability.BaseValueScaleConstant),
                       (actor.MaxActiveAtOneTime.BaseValueConstant,
                        actor.MaxActiveAtOneTime.BaseValueAttribute,
                        actor.MaxActiveAtOneTime.InitializationDefinition,
                        actor.MaxActiveAtOneTime.BaseValueScaleConstant,),
                       actor.TestVisibility,
                       actor.TestFOV)
                      for actor in pop_def.ActorArchetypeList]
        if not actor_list:
            return
        actor_list.append(new_actor)
        pop_def.ActorArchetypeList = actor_list

    def fake_hotfix_popdef(self, loaded_map: str) -> None:
        for file in self.pop_files:
            logging.logger.verbose(f"fake_hotfix_popdef reading file: {file}")
            with open(file, "r", encoding="cp1252") as File:
                b_skip_to_next = False
                for line in File:
                    logging.logger.verbose(f"{file}-> {line}")
                    if line[0] == "/":
                        b_skip_to_next = False

                    if not line.split() or line[0] == "-" or b_skip_to_next:
                        continue
                    elif line.split()[0].lower() == "set":
                        set_iterpreter.set_cmd(line)
                    elif line[0] == "!":
                        unrealsdk.LoadPackage(line[1:].strip())
                    elif line[0] == "/":
                        if line[1:].strip().lower() == loaded_map.lower():
                            continue
                        else:
                            b_skip_to_next = True
                    elif line[0] == "#":
                        willow_popdef = unrealsdk.FindObject("WillowPopulationDefinition", line[1:].strip())
                        if willow_popdef is None:
                            b_skip_to_next = True
                    else:
                        s = line.split()
                        if s[0] == "SpawnFactory":
                            obj = unrealsdk.FindObject("PopulationFactoryBalancedAIPawn", s[1].strip())
                            spawn_factory = unrealsdk.ConstructObject(Class=obj.Class,
                                                                      Outer=obj.Outer,
                                                                      Name=f"{obj.Name}_09999",
                                                                      SetFlags=0x83, Template=obj)
                            spawn_factory.PawnBalanceDefinition = unrealsdk.FindObject("AIPawnBalanceDefinition",
                                                                                       s[2].strip())
                        elif s[0] == "Probability":
                            if s[1] == "BaseValueConstant":
                                prob_bvc = float(s[2].strip())
                            elif s[1] == "BaseValueAttribute":
                                prob_bva = unrealsdk.FindObject("Object", s[2].strip())
                            elif s[1] == "InitializationDefinition":
                                prob_init_def = unrealsdk.FindObject("Object", s[2].strip())
                            elif s[1] == "BaseValueScaleConstant":
                                prob_bvsc = float(s[2].strip())
                        elif s[0] == "MaxActiveAtOneTime":
                            if s[1] == "BaseValueConstant":
                                max_bvc = float(s[2].strip())
                            elif s[1] == "BaseValueAttribute":
                                max_bva = unrealsdk.FindObject("Object", s[2].strip())
                            elif s[1] == "InitializationDefinition":
                                max_init_def = unrealsdk.FindObject("Object", s[2].strip())
                            elif s[1] == "BaseValueScaleConstant":
                                max_bvsc = float(s[2].strip())
                        elif s[0] == "TestVisibility":
                            visibility = s[1].strip().lower() == "true"
                        elif s[0] == "TestFOV":
                            fov = s[1].strip().lower() == "true"
                            self.append_popdef(willow_popdef, (spawn_factory,
                                                               (prob_bvc, prob_bva, prob_init_def, prob_bvsc),
                                                               (max_bvc, max_bva, max_init_def, max_bvsc),
                                                               visibility, fov))

    def construct_custom_pawn(self, loaded_map: str) -> None:
        pc = bl2tools.get_player_controller()
        for file in self.pawn_files:
            logging.logger.verbose(f"construct_custom_pawn() reading file: {file}")
            with open(file, "r", encoding="cp1252") as File:
                b_skip_to_next = False
                skip_pawn: bool = False
                for line in File:
                    logging.logger.verbose(f"{file}-> {line}")
                    if line[0] == "/":
                        b_skip_to_next = False
                        skip_pawn = False
                    if line[0] == "#":
                        skip_pawn = False

                    if not line.split() or line[0] == "-" or b_skip_to_next or skip_pawn:
                        continue
                    elif line[0] == "/":
                        if line[1:].strip().lower() == loaded_map.lower() or line[1:].strip().lower() == "none":
                            continue
                        else:
                            b_skip_to_next = True
                    elif line[0] == "!":
                        unrealsdk.LoadPackage(line[1:].strip())
                    elif line[0] == "?":
                        copy_me, new_name, outer = line[1:].split()
                        copy_me = unrealsdk.FindObject("Object", copy_me)
                        outer = unrealsdk.FindObject("Object", outer)
                        new_obj = unrealsdk.ConstructObject(Class=copy_me.Class,
                                                            Outer=outer,
                                                            Name=new_name,
                                                            Template=copy_me)
                        new_obj.ObjectFlags.B |= 4

                    elif line[0] == "#":
                        template_pawn = unrealsdk.FindObject("AIPawnBalanceDefinition", line[1:].split()[0].strip())
                        if template_pawn is None:
                            skip_pawn = True
                            continue

                        name = line.split()[1]

                        ai_balance = unrealsdk.ConstructObject(Class=template_pawn.Class,
                                                               Outer=template_pawn.Outer,
                                                               Name=name,
                                                               SetFlags=0x83, Template=template_pawn)
                        pawn = ai_balance.AIPawnArchetype
                        ai_balance.AIPawnArchetype = unrealsdk.ConstructObject(Class=pawn.Class,
                                                                               Outer=pawn.Outer,
                                                                               Name=f"Pawn_{name.split('_')[-1]}",
                                                                               SetFlags=0x83, Template=pawn)
                        pawn = ai_balance.AIPawnArchetype

                        ai_class = pawn.AIClass
                        pawn.AIClass = unrealsdk.ConstructObject(Class=ai_class.Class,
                                                                 Outer=ai_class.Outer,
                                                                 Name=f"CharClass_{name.split('_')[-1]}",
                                                                 SetFlags=0x83, Template=ai_class
                                                                 )

                        ai_class = pawn.AIClass
                        ai_class.AIDef = unrealsdk.ConstructObject(Class=ai_class.AIDef.Class,
                                                                   Outer=ai_class.AIDef.Outer,
                                                                   Name=f"AIDef_{name.split('_')[-1]}",
                                                                   SetFlags=0x83, Template=ai_class.AIDef
                                                                   )

                    elif line.split()[0].lower() == "set":
                        pc.ConsoleCommand(line, 1)

                    elif line.split()[0].lower().startswith("set_skin"):
                        playtrough = line.split()[0].lower().replace("set_skin", "")
                        if playtrough.isdigit():
                            playtrough = int(playtrough) - 1
                        else:
                            playtrough = -1
                        # do it per playtrough
                        pc = bl2tools.get_player_controller()
                        need_mat: unrealsdk.UObject = unrealsdk.FindObject(
                            "AIPawnBalanceDefinition", line.split()[1].strip()
                        )

                        if playtrough == -1:
                            for pt, _ in enumerate(need_mat.PlayThroughs):
                                if need_mat.PlayThroughs[pt].MeshMaterial is None:
                                    mat = bl2tools.get_world_info().MyEmitterPool.GetFreeMatInstConsts(True)
                                    need_mat.PlayThroughs[pt].MeshMaterial = mat

                                mat = need_mat.PlayThroughs[pt].MeshMaterial
                                cmd = f"set {mat.PathName(mat)} {' '.join(line.split()[2:])}"
                                if self.is_game_bl2:
                                    pc.ConsoleCommand(cmd, 1)
                                else:
                                    matinstconsts.Materials.exec_skins(cmd, self.is_game_bl2)
                        else:
                            if need_mat.PlayThroughs[playtrough].MeshMaterial is None:
                                mat = unrealsdk.GetEngine().GetCurrentWorldInfo().MyEmitterPool.GetFreeMatInstConsts(
                                    True)
                                need_mat.PlayThroughs[playtrough].MeshMaterial = mat

                            mat = need_mat.PlayThroughs[pt].MeshMaterial

                            cmd = f"set {mat.PathName(mat)} {' '.join(line.split()[2:])}"
                            if self.is_game_bl2:
                                pc.ConsoleCommand(cmd, 1)
                            else:
                                matinstconsts.Materials.exec_skins(cmd, self.is_game_bl2)
