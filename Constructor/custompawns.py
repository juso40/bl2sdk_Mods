import unrealsdk
from unrealsdk import *

from . import set_iterpreter as set, logging

import os


@logging.log_all_calls(logging.call_logger)
class Pawns:

    def __init__(self, path):
        self.PATH = path
        self.pop_files = []
        self.pawn_files = []
        self.components_to_destroy = []

    def Enable(self):
        self.load_files()

        def StartLoading(caller: UObject, function: UFunction, params: FStruct) -> bool:
            if params.MovieName != "None":
                emitterpool = GetEngine().GetCurrentWorldInfo().MyEmitterPool
                for component in self.components_to_destroy:
                    emitterpool.ReturnToPool(component)
                self.components_to_destroy.clear()
            return True

        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.WillowClientShowLoadingMovie", "StartLoading",
                               StartLoading)

    def Disable(self):
        pass

    def on_end_load(self):
        self.construct_custom_pawn()
        self.fake_hotfix_popdef()

    def load_files(self):
        for root, dirs, filenames in os.walk(self.PATH):
            for file in filenames:
                if file.lower().endswith(".pawn"):
                    self.pawn_files.append(os.path.join(root, file))
                elif file.lower().endswith(".popdef"):
                    self.pop_files.append(os.path.join(root, file))

    def append_popdef(self, pop_def, new_actor):
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

    def fake_hotfix_popdef(self):
        for file in self.pop_files:
            logging.logger.verbose(f"fake_hotfix_popdef reading file: {file}")
            with open(file, "r") as File:
                b_skip_to_next = False
                for line in File:
                    logging.logger.verbose(f"{file}-> {line}")
                    if line[0] == "+":
                        b_skip_to_next = False

                    if not line.split() or line[0] == "-" or b_skip_to_next:
                        continue
                    elif line.split()[0].lower() == "set":
                        set.set(line)
                    elif line[0] == "+":
                        if line[1:].strip() == str(GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName()):
                            continue
                        else:
                            b_skip_to_next = True
                    elif line[0] == "#":
                        willow_popdef = FindObject("WillowPopulationDefinition", line[1:].strip())
                        if willow_popdef is None:
                            b_skip_to_next = True
                    else:
                        s = line.split()
                        if s[0] == "SpawnFactory":
                            obj = FindObject("PopulationFactoryBalancedAIPawn", s[1].strip())
                            spawn_factory = ConstructObject(Class=obj.Class,
                                                            Outer=obj.Outer,
                                                            Name=obj.Name + "_09999",
                                                            SetFlags=0x83, Template=obj)
                            spawn_factory.PawnBalanceDefinition = FindObject("AIPawnBalanceDefinition", s[2].strip())
                        elif s[0] == "Probability":
                            if s[1] == "BaseValueConstant":
                                prob_bvc = float(s[2].strip())
                            elif s[1] == "BaseValueAttribute":
                                prob_bva = FindObject("Object", s[2].strip())
                            elif s[1] == "InitializationDefinition":
                                prob_init_def = FindObject("Object", s[2].strip())
                            elif s[1] == "BaseValueScaleConstant":
                                prob_bvsc = float(s[2].strip())
                        elif s[0] == "MaxActiveAtOneTime":
                            if s[1] == "BaseValueConstant":
                                max_bvc = float(s[2].strip())
                            elif s[1] == "BaseValueAttribute":
                                max_bva = FindObject("Object", s[2].strip())
                            elif s[1] == "InitializationDefinition":
                                max_init_def = FindObject("Object", s[2].strip())
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

    def construct_custom_pawn(self):
        for file in self.pawn_files:
            logging.logger.verbose(f"construct_custom_pawn() reading file: {file}")
            with open(file, "r") as File:
                logging.logger.debug(
                    f"Loading map: {GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName()}")
                b_skip_to_next = False
                for line in File:
                    logging.logger.verbose(f"{file}-> {line}")
                    if line[0] == "+":
                        b_skip_to_next = False

                    if not line.split() or line[0] == "-" or b_skip_to_next:
                        continue
                    elif line[0] == "+":
                        if line[1:].strip() == str(GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName()):
                            continue
                        else:
                            b_skip_to_next = True
                    elif line[0] == "#":
                        template_pawn = FindObject("AIPawnBalanceDefinition", line[1:].split()[0].strip())
                        name = line.split()[1]

                        ai_balance = ConstructObject(Class=template_pawn.Class,
                                                     Outer=template_pawn.Outer,
                                                     Name=name,
                                                     SetFlags=0x83, Template=template_pawn)
                        pawn = ai_balance.AIPawnArchetype
                        ai_balance.AIPawnArchetype = ConstructObject(Class=pawn.Class,
                                                                     Outer=pawn.Outer,
                                                                     Name="Pawn_" + name.split("_")[-1],
                                                                     SetFlags=0x83, Template=pawn)
                        pawn = ai_balance.AIPawnArchetype
                        ### Mesh Tests ####
                        # pawn.BodyClass = ConstructObject(Class=pawn.BodyClass.Class, Outer=pawn,
                        #                                  Name="BodyClassDefinition_" + name.split("_")[-1],
                        #                                  SetFlags=0x83, Template=pawn.BodyClass)

                        # The Following code was meant to add new StaticMeshComponents to the BodyClassDefinition
                        # But for some reason the game will crash when traveling or save quitting with additional
                        # StaticMeshComponents. Maybe someone will find a workaround or a fix for this issue.
                        # emitterpool = GetEngine().GetCurrentWorldInfo().MyEmitterPool
                        # attachements = []
                        # for i in range(10):
                        #     component = emitterpool.GetFreeStaticMeshComponent(True)
                        #     component.Outer = bodyclass
                        #     attachements.append((("", 4, 0, 0, 0, False, False, 0, 0.0,
                        #                           (0.0, 0.0, 0.0), None,
                        #                           (component, 1, False, False, False, "", None, None, None),
                        #                           "", i), "", 0, 0))
                        #
                        # bodyclass.BodyComposition.Attachments = attachements
                        ###################

                        ai_class = ai_balance.AIPawnArchetype.AIClass
                        ai_balance.AIPawnArchetype.AIClass = ConstructObject(Class=ai_class.Class,
                                                                             Outer=ai_class.Outer,
                                                                             Name="CharClass_" + name.split("_")[-1],
                                                                             SetFlags=0x83, Template=ai_class)

                    elif line.split()[0].lower() == "set":
                        pc = GetEngine().GamePlayers[0].Actor
                        pc.ConsoleCommand(line, 1)

                    elif line.split()[0].lower() == "set_skin":
                        need_mat = FindObject("AIPawnBalanceDefinition", line.split()[1].strip())
                        if need_mat.PlayThroughs[0].MeshMaterial is None:
                            mat = unrealsdk.GetEngine().GetCurrentWorldInfo().MyEmitterPool.GetFreeMatInstConsts(True)
                            need_mat.PlayThroughs[0].MeshMaterial = mat

                        pc = GetEngine().GamePlayers[0].Actor

                        cmd = "set " + mat.PathName(mat) + " " + " ".join(line.split()[2:])
                        pc.ConsoleCommand(cmd, 1)
