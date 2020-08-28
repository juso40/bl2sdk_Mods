import unrealsdk
from unrealsdk import *

import os

from . import logging


@logging.log_all_calls(logging.call_logger)
class Constructor:

    def __init__(self, path):
        self.PATH = path
        self.c_files = []
        self.l_files = []

    def Enable(self):
        self.load_files()
        self.keep_loaded()
        self.construct()

    def Disable(self):
        pass

    def load_files(self):
        for root, dirs, filenames in os.walk(self.PATH):
            for file in filenames:
                if file.lower().endswith(".construct"):
                    self.c_files.append(os.path.join(root, file))
                elif file.lower().endswith(".loaded"):
                    self.l_files.append(os.path.join(root, file))

    def get_full_name(self, obj):
        if obj is not None:
            return obj.PathName(obj)
        elif obj is None:
            return "None"

    def weapon_partlist_helper(self, obj, new_wpn_balance):
        """
        This Functions purpose is it to easily create New PartLists to work with.
        If one constructs a new WeaponBalanceDefinition this function gets called and constructs its new PartLists
        The new WeaponPartListCollection name will be "PartList"
        The new RuntimePartListCollection name will be "WeaponPartListCollectionDefinition_1000"
        """
        part_list = obj.WeaponPartListCollection
        new_part_list = unrealsdk.ConstructObject(Class="WeaponPartListCollectionDefinition", Outer=new_wpn_balance,
                                                  Name="PartList", SetFlags=0x83, Template=part_list)
        unrealsdk.KeepAlive(new_part_list)

        runtime_part_list = obj.RuntimePartListCollection
        new_runtime_part_list = unrealsdk.ConstructObject(Class="WeaponPartListCollectionDefinition",
                                                          Outer=new_wpn_balance,
                                                          Name="WeaponPartListCollectionDefinition_1000",
                                                          SetFlags=0x83, Template=runtime_part_list)
        unrealsdk.KeepAlive(new_runtime_part_list)

        new_wpn_balance.WeaponPartListCollection = new_part_list
        new_wpn_balance.RuntimePartListCollection = new_runtime_part_list

    def com_partlist_helper(self, obj, new_com_balance):
        """
        This Functions purpose is it to easily create New PartLists to work with.
        If one constructs a new ClassModBalanceDefinition this function gets called and constructs its new PartLists
        The new ItemPartListCollection name will be "PartList"
        The new RuntimePartListCollection name will be "ItemPartListCollectionDefinition_1000"
        """
        part_list = obj.ItemPartListCollection
        new_part_list = unrealsdk.ConstructObject(Class="ItemPartListCollectionDefinition", Outer=new_com_balance,
                                                  Name="PartList", SetFlags=0x83, Template=part_list)
        unrealsdk.KeepAlive(new_part_list)

        runtime_part_list = obj.RuntimePartListCollection
        new_runtime_part_list = unrealsdk.ConstructObject(Class="ItemPartListCollectionDefinition",
                                                          Outer=new_com_balance,
                                                          Name="ItemPartListCollectionDefinition_1000",
                                                          SetFlags=0x83, Template=runtime_part_list)
        unrealsdk.KeepAlive(new_runtime_part_list)

        new_com_balance.ItemPartListCollection = new_part_list
        new_com_balance.RuntimePartListCollection = new_runtime_part_list

    def inv_partlist_helper(self, obj, newBalance):
        if obj.PartListCollection:
            part_list = obj.PartListCollection
            new_part_list = unrealsdk.ConstructObject(Class="ItemPartListCollectionDefinition",
                                                      Outer=part_list.Outer,
                                                      Name=newBalance.Name, SetFlags=0x83, Template=part_list)
            KeepAlive(new_part_list)
            newBalance.PartListCollection = new_part_list

    def custom_presentation_helper(self, obj, newNamePart):
        """
        This function tries to copy the CustomPresentations from the old template
         object to the new constructed "WeaponNamePartDefinition".
        """
        new_custom_presentations = []
        number = 0
        for Presentation in obj.CustomPresentations:
            new_presentation = unrealsdk.ConstructObject(Class="AttributePresentationDefinition", Outer=newNamePart,
                                                         Name="AttributePresentationDefinition_100" + str(number),
                                                         SetFlags=0x83, Template=Presentation)
            unrealsdk.KeepAlive(new_presentation)
            number += 1
            new_custom_presentations.append(new_presentation)
        newNamePart.CustomPresentations = new_custom_presentations

    def skill_presentation_helper(self, cloned_obj, new_obj):
        new_custom_presentations = []
        number = 0
        for Presentation in cloned_obj.SkillEffectPresentations:
            new_presentation = unrealsdk.ConstructObject(Class="AttributePresentationDefinition", Outer=new_obj,
                                                         Name="AttributePresentationDefinition_100" + str(number),
                                                         SetFlags=0x83, Template=Presentation)
            unrealsdk.KeepAlive(new_presentation)
            number += 1
            new_custom_presentations.append(new_presentation)
        new_obj.SkillEffectPresentations = new_custom_presentations

    def skill_constraints_helper(self, new_obj):
        number = 1000
        for i, constraint in enumerate(new_obj.SkillConstraints):
            if constraint.Evaluator:
                obj = constraint.Evaluator
                new_constraint = unrealsdk.ConstructObject(Class=obj.Class, Outer=new_obj,
                                                           Name=obj.Name + "_" + str(number),
                                                           SetFlags=0x83, Template=obj)
                unrealsdk.KeepAlive(new_constraint)
                number += 1
                new_obj.SkillConstraints[i].Evaluator = new_constraint
                self.evaluator_expression_helper(new_constraint)
            else:
                for j, obj in enumerate(constraint.EvaluatorDefinitions):
                    new_constraint = unrealsdk.ConstructObject(Class=obj.Class, Outer=new_obj,
                                                               Name=obj.Name + "_" + str(number),
                                                               SetFlags=0x83, Template=obj)
                    unrealsdk.KeepAlive(new_constraint)
                    number += 1
                    new_obj.SkillConstraints[i].EvaluatorDefinitions[j] = new_constraint
                    self.evaluator_expression_helper(new_constraint)

    def evaluator_expression_helper(self, evaluator):
        if evaluator.Expression1:
            new_expression = unrealsdk.ConstructObject(Class=evaluator.Expression1.Class, Outer=evaluator,
                                                       Name=evaluator.Expression1.Name + "_1",
                                                       SetFlags=0x83, Template=evaluator.Expression1)
            KeepAlive(new_expression)
            evaluator.Expression1 = new_expression
        if evaluator.Expression2:
            new_expression = unrealsdk.ConstructObject(Class=evaluator.Expression1.Class, Outer=evaluator,
                                                       Name=evaluator.Expression1.Name + "_2",
                                                       SetFlags=0x83, Template=evaluator.Expression1)
            KeepAlive(new_expression)
            evaluator.Expression1 = new_expression

    def append_classmoddefinitions(self, COMDefinition):
        req_player_class = COMDefinition.PathName(COMDefinition.RequiredPlayerClass)
        com_balance = None
        if "Assassin" in req_player_class:
            com_balance = FindObject("ClassModBalanceDefinition", "GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin")
        elif "Mercenary" in req_player_class:
            com_balance = FindObject("ClassModBalanceDefinition", "GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary")
        elif "Siren" in req_player_class:
            com_balance = FindObject("ClassModBalanceDefinition", "GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren")
        elif "Soldier" in req_player_class:
            com_balance = FindObject("ClassModBalanceDefinition", "GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier")
        elif "Psycho" in req_player_class:
            com_balance = FindObject("ClassModBalanceDefinition", "GD_Lilac_ClassMods."
                                                                  "BalanceDefs.BalDef_ClassMod_Psycho")
        elif "Mechromancer" in req_player_class:
            com_balance = FindObject("ClassModBalanceDefinition", "GD_Tulip_ItemGrades.ClassMods."
                                                                  "BalDef_ClassMod_Mechromancer")
        if com_balance:
            new_class_mod_definitions = [x for x in com_balance.ClassModDefinitions]
            new_class_mod_definitions.append(COMDefinition)
            com_balance.ClassModDefinitions = new_class_mod_definitions

    def append_attr_presentation_def(self, PresentationDef):
        category = PresentationDef.PathName(PresentationDef).split(".")[1]
        if category == "Artifacts":
            presentation_list = FindObject("AttributePresentationListDefinition",
                                           "GD_AttributePresentation._AttributeList.ArtifactOverridePresentationList")
        elif category == "ClassMods_Only":
            presentation_list = FindObject("AttributePresentationListDefinition",
                                           "GD_AttributePresentation._AttributeList.ClassModOverridePresentationList")
        elif category == "GrenadeMod":
            presentation_list = FindObject("AttributePresentationListDefinition",
                                           "GD_AttributePresentation._AttributeList.GrenadeModOverridePresentationList")
        elif category == "Inventory" or category == "Echo":
            presentation_list = FindObject("AttributePresentationListDefinition",
                                           "GD_AttributePresentation._AttributeList.ItemOverridePresentationList")
        elif category == "Weapons":
            presentation_list = FindObject("AttributePresentationListDefinition",
                                           "GD_AttributePresentation._AttributeList.WeaponOverridePresentationList")
        elif category == "Shields":
            presentation_list = FindObject("AttributePresentationListDefinition",
                                           "GD_AttributePresentation._AttributeList.ShieldOverridePresentationList")
        else:
            presentation_list = FindObject("AttributePresentationListDefinition",
                                           "GD_AttributePresentation._AttributeList.DefaultPresentationList")

        temp = [x for x in presentation_list.Attributes]
        temp.append(PresentationDef)
        presentation_list.Attributes = temp

    def bpd_helper(self, new_bpd):
        counter = 0
        for Sequence in new_bpd.BehaviorSequences:
            for Data in Sequence.BehaviorData2:
                if Data.Behavior:
                    new_behavior = unrealsdk.ConstructObject(Class=Data.Behavior.Class, Outer=new_bpd,
                                                             Name=Data.Behavior.Name + "_" + str(counter),
                                                             SetFlags=0x83, Template=Data.Behavior)
                    KeepAlive(new_behavior)
                    Data.Behavior = new_behavior
                    counter += 1
                    if Data.Behavior.Class == FindClass("Behavior_AttributeEffect"):
                        self.behavior_attribute_effect_helper(new_behavior)
                    elif Data.Behavior.Class == FindClass("Behavior_ActivateSkill"):
                        self.behavior_activate_skill_helper(new_behavior)

    def behavior_activate_skill_helper(self, new_obj):
        if new_obj.SkillToActivate:
            name = self.get_full_name(new_obj)
            new_name = name.split(":")[0].split("_")[-1] + "_Skill_" + name.split("_")[-1]
            new_skill = unrealsdk.ConstructObject(Class=new_obj.SkillToActivate.Class,
                                                  Outer=new_obj.SkillToActivate.Outer,
                                                  Name=new_name,
                                                  SetFlags=0x83, Template=new_obj.SkillToActivate)
            KeepAlive(new_skill)
            new_obj.SkillToActivate = new_skill
            self.bpd_copy_helper(new_skill)

    def behavior_attribute_effect_helper(self, new_obj):
        if new_obj.AttributeEffect:
            new_effect = unrealsdk.ConstructObject(Class=new_obj.AttributeEffect.Class, Outer=new_obj,
                                                   Name=new_obj.AttributeEffect.Name + "_1",
                                                   SetFlags=0x83, Template=new_obj.AttributeEffect)
            KeepAlive(new_effect)
            new_obj.AttributeEffect = new_effect
            if new_effect == FindClass("SkillDefinition"):
                self.bpd_copy_helper(new_effect)
                self.skill_constraints_helper(new_effect)

    def bpd_copy_helper(self, newObj):
        if newObj.BehaviorProviderDefinition:
            new_BPD = unrealsdk.ConstructObject(Class="BehaviorProviderDefinition", Outer=newObj,
                                                Name=newObj.BehaviorProviderDefinition.Name + "_0",
                                                SetFlags=0x83, Template=newObj.BehaviorProviderDefinition)
            KeepAlive(new_BPD)
            newObj.BehaviorProviderDefinition = new_BPD
            self.bpd_helper(new_BPD)

    def on_any_impact_helper(self, newObj):
        if newObj.OnAnyImpact:
            new_on_any_impact = []
            counter = 0
            for behavior in newObj.OnAnyImpact:
                new_behavior = unrealsdk.ConstructObject(Class=behavior.Class, Outer=newObj,
                                                         Name=behavior.Name + "_" + str(counter),
                                                         SetFlags=0x83, Template=behavior)
                counter += 1
                KeepAlive(new_behavior)
                new_on_any_impact.append(new_behavior)
                if behavior.Class == FindClass("Behavior_AttributeEffect"):
                    self.behavior_attribute_effect_helper(new_behavior)
            newObj.OnAnyImpact = new_on_any_impact

    def attribute_definition_helper(self, new_obj):
        if new_obj.ValueResolverChain:
            counter = 0
            temp = []
            for value in new_obj.ValueResolverChain:
                new_value = unrealsdk.ConstructObject(Class=value.Class, Outer=new_obj,
                                                      Name=value.Name + "_" + str(counter),
                                                      SetFlags=0x83, Template=value)
                KeepAlive(new_value)
                temp.append(new_value)
                counter += 1
            new_obj.ValueResolverChain = temp

        if new_obj.ContextResolverChain:
            counter = 0
            temp = []
            for context in new_obj.ContextResolverChain:
                new_context = unrealsdk.ConstructObject(Class=context.Class, Outer=new_obj,
                                                        Name=context.Name + "_" + str(counter),
                                                        SetFlags=0x83, Template=context)
                KeepAlive(new_context)
                temp.append(new_context)
                counter += 1
            new_obj.ContextResolverChain = temp

    def population_definition_helper(self, new_obj, template_obj):
        counter = 1000
        spawn_factories = []
        for l in template_obj.ActorArchetypeList:
            factory = l.SpawnFactory
            new = unrealsdk.ConstructObject(Class=factory.Class, Outer=new_obj, Name=f"{new_obj.name}_{counter}",
                                            SetFlags=0x83, Template=template_obj)
            counter += 1
            KeepAlive(new)
            spawn_factories.append(new)

        new_obj.ActorArchetypeList = [(x, (1, None, None, 1), (0, None, None, 0), False, False) for x in
                                      spawn_factories]

    def construct(self):
        """
        This function reads in all lines from any "*.construct" file from any folder.
        The lines that start with "#" decide in what class the newly constructed object belongs.
        The lines that start with "-" get ignored and can be used as a comment.
        If you add an additional String behind the to be constructed object it will be used as the new objs name.
        """
        for file in self.c_files:
            with open(file, "r") as TemplateFile:
                for line in TemplateFile:
                    try:
                        if not line.split() or line[0] == "-":  # "-" counts as comment
                            continue
                        elif line[0] == "#":  # "#" is used to set the new Class
                            in_class = line[1:].strip()
                        else:
                            obj_name = line.split()
                            template_object_str = obj_name[0].strip()
                            cloned_obj = unrealsdk.FindObject(in_class, template_object_str)
                            if len(obj_name) == 1:
                                new_name = cloned_obj.Name + "Cloned"
                                new_object = unrealsdk.ConstructObject(Class=in_class, Outer=cloned_obj.Outer,
                                                                       Name=new_name, SetFlags=0x83,
                                                                       Template=cloned_obj)
                            elif len(obj_name) == 2:
                                new_name = obj_name[1].strip()
                                new_object = unrealsdk.ConstructObject(Class=in_class, Outer=cloned_obj.Outer,
                                                                       Name=new_name, SetFlags=0x83,
                                                                       Template=cloned_obj)
                            elif len(obj_name) == 3:
                                new_name = obj_name[1].strip()
                                outer = FindObject("Object", obj_name[2].strip())
                                new_object = unrealsdk.ConstructObject(Class=in_class, Outer=outer,
                                                                       Name=new_name, SetFlags=0x83,
                                                                       Template=cloned_obj)
                            unrealsdk.KeepAlive(new_object)
                            if in_class == "WeaponBalanceDefinition":
                                self.weapon_partlist_helper(cloned_obj, new_object)
                            elif in_class == "ClassModBalanceDefinition":
                                self.com_partlist_helper(cloned_obj, new_object)
                            elif in_class == "InventoryBalanceDefinition":
                                self.inv_partlist_helper(cloned_obj, new_object)
                            elif in_class in ("ClassModDefinition", "CrossDLCClassModDefinition"):
                                try:
                                    self.custom_presentation_helper(cloned_obj, new_object)
                                except:
                                    logging.logger.debug(
                                        f"{cloned_obj.PathName(cloned_obj)} does not have its own custom presentation!")

                                self.append_classmoddefinitions(new_object)
                            elif in_class == "AttributePresentationDefinition":
                                self.append_attr_presentation_def(new_object)
                            elif in_class == "GrenadeModPartDefinition":
                                try:
                                    self.custom_presentation_helper(cloned_obj, new_object)
                                except:
                                    logging.logger.debug(
                                        f"{cloned_obj.PathName(cloned_obj)} does not have its own custom presentation!")
                            elif in_class in ("WeaponNamePartDefinition", "ShieldDefinition",
                                              "ArtifactPartDefinition", "ItemNamePartDefinition",
                                              "WeaponTypeDefinition"):
                                try:
                                    self.custom_presentation_helper(cloned_obj, new_object)
                                except:
                                    logging.logger.debug(
                                        f"{cloned_obj.PathName(cloned_obj)} does not have its own custom presentation!")
                            elif in_class == "BehaviorProviderDefinition":
                                self.bpd_helper(new_object)
                            elif in_class == "Behavior_AttributeEffect":
                                self.behavior_attribute_effect_helper(new_object)
                            elif in_class in ("AttributeDefinition", "InventoryAttributeDefinition"):
                                self.attribute_definition_helper(new_object)

                            if in_class in ("ProjectileDefinition", "WeaponPartDefinition", "ShieldPartDefinition",
                                            "ShieldDefinition", "SkillDefinition", "ArtifactDefinition",
                                            "GrenadeModDefinition", "ClassModDefinition", "UsableItemDefinition"):
                                self.bpd_copy_helper(new_object)
                            if in_class == "FiringModeDefinition":
                                self.on_any_impact_helper(new_object)

                            if in_class in ("ShieldPartDefinition", "WeaponPartDefinition"):
                                try:
                                    self.custom_presentation_helper(cloned_obj, new_object)
                                except:
                                    logging.logger.debug(
                                        f"{cloned_obj.PathName(cloned_obj)} does not have its own custom presentation!")
                            if in_class == "SkillDefinition":
                                try:
                                    self.skill_presentation_helper(cloned_obj, new_object)
                                    self.skill_constraints_helper(new_object)
                                except:
                                    logging.logger.verbose(
                                        f"{cloned_obj.PathName(cloned_obj)} does not have presentations!")
                            if in_class == "PopulationDefinition":
                                self.population_definition_helper(new_object, cloned_obj)
                    except Exception as e:
                        logging.logger.error(f"{e}")
                        logging.logger.error(f"An exception occured in {file}")
                        logging.logger.error(f"Please check this line: {line}")

    def keep_loaded(self):
        """
        Small helper function for easily keeping objects loaded.
        "#" defines what Package to load, "-" are comments.
        Searches for any text file with the custom ending ".loaded" and tries to
         keep the objects listet in the file loaded.
        """
        for file in self.l_files:
            with open(file, "r") as TemplateFile:
                for line in TemplateFile:
                    if not line.split() or line[0] == "-":
                        continue
                    elif line[0] == "#":
                        package = line[1:].strip()
                        unrealsdk.LoadPackage(package)
                    else:
                        unrealsdk.KeepAlive(unrealsdk.FindObject("Object", line.strip()))
