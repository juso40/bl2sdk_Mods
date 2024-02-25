import unrealsdk
from unrealsdk import *

import os

from . import logging
from . import bl2tools


def weapon_partlist_helper(obj: unrealsdk.UObject, new_wpn_balance: unrealsdk.UObject) -> None:
    """
    This Functions purpose is it to easily create New PartLists to work with.
    If one constructs a new WeaponBalanceDefinition this function gets called and constructs its new PartLists
    The new WeaponPartListCollection name will be "PartList"
    The new RuntimePartListCollection name will be "WeaponPartListCollectionDefinition_1000"
    """
    part_list = obj.WeaponPartListCollection
    new_part_list = unrealsdk.ConstructObject(Class="WeaponPartListCollectionDefinition", Outer=new_wpn_balance,
                                              Name="PartList", Template=part_list)
    unrealsdk.KeepAlive(new_part_list)
    new_part_list.ObjectFlags.B |= 4

    runtime_part_list = obj.RuntimePartListCollection
    new_runtime_part_list = unrealsdk.ConstructObject(Class="WeaponPartListCollectionDefinition",
                                                      Outer=new_wpn_balance,
                                                      Name="WeaponPartListCollectionDefinition_1000",
                                                      Template=runtime_part_list)
    unrealsdk.KeepAlive(new_runtime_part_list)
    new_runtime_part_list.ObjectFlags.B |= 4

    new_wpn_balance.WeaponPartListCollection = new_part_list
    new_wpn_balance.RuntimePartListCollection = new_runtime_part_list


def com_partlist_helper(obj: unrealsdk.UObject, new_com_balance: unrealsdk.UObject) -> None:
    """
    This Functions purpose is it to easily create New PartLists to work with.
    If one constructs a new ClassModBalanceDefinition this function gets called and constructs its new PartLists
    The new ItemPartListCollection name will be "PartList"
    The new RuntimePartListCollection name will be "ItemPartListCollectionDefinition_1000"
    """
    part_list = obj.ItemPartListCollection
    new_part_list = unrealsdk.ConstructObject(Class="ItemPartListCollectionDefinition", Outer=new_com_balance,
                                              Name="PartList", Template=part_list)
    unrealsdk.KeepAlive(new_part_list)
    new_part_list.ObjectFlags.B |= 4

    runtime_part_list = obj.RuntimePartListCollection
    new_runtime_part_list = unrealsdk.ConstructObject(Class="ItemPartListCollectionDefinition",
                                                      Outer=new_com_balance,
                                                      Name="ItemPartListCollectionDefinition_1000",
                                                      Template=runtime_part_list)
    unrealsdk.KeepAlive(new_runtime_part_list)
    new_runtime_part_list.ObjectFlags.B |= 4

    new_com_balance.ItemPartListCollection = new_part_list
    new_com_balance.RuntimePartListCollection = new_runtime_part_list


def inv_partlist_helper(obj: unrealsdk.UObject, new_balance: unrealsdk.UObject) -> None:
    if obj.PartListCollection:
        part_list = obj.PartListCollection
        if obj.PathName(part_list).rsplit(".", 1)[0] == obj.PathName(obj).rsplit(".", 1)[0]:
            new_name = f"Parts_{new_balance.Name}"
        else:
            new_name = new_balance.Name
        new_part_list = unrealsdk.ConstructObject(Class="ItemPartListCollectionDefinition",
                                                  Outer=part_list.Outer,
                                                  Name=new_name, Template=part_list)
        unrealsdk.KeepAlive(new_part_list)
        new_part_list.ObjectFlags.B |= 4
        new_balance.PartListCollection = new_part_list


def custom_presentation_helper(obj: unrealsdk.UObject, new_name_part: unrealsdk.UObject) -> None:
    """
    This function tries to copy the CustomPresentations from the old template
     object to the new constructed "WeaponNamePartDefinition".
    """
    new_custom_presentations = []
    for number, Presentation in enumerate(obj.CustomPresentations):
        new_presentation = unrealsdk.ConstructObject(Class="AttributePresentationDefinition", Outer=new_name_part,
                                                     Name=f"AttributePresentationDefinition_{1000 + number}",
                                                     Template=Presentation)
        unrealsdk.KeepAlive(new_presentation)
        new_presentation.ObjectFlags.B |= 4
        new_custom_presentations.append(new_presentation)
    new_name_part.CustomPresentations = new_custom_presentations


def skill_presentation_helper(cloned_obj: unrealsdk.UObject, new_obj: unrealsdk.UObject) -> None:
    new_custom_presentations = []
    for number, Presentation in enumerate(cloned_obj.SkillEffectPresentations):
        new_presentation = unrealsdk.ConstructObject(Class="AttributePresentationDefinition", Outer=new_obj,
                                                     Name=f"AttributePresentationDefinition_{1000 + number}",
                                                     Template=Presentation)
        unrealsdk.KeepAlive(new_presentation)
        new_presentation.ObjectFlags.B |= 4
        new_custom_presentations.append(new_presentation)
    new_obj.SkillEffectPresentations = new_custom_presentations


def evaluator_expression_helper(evaluator: unrealsdk.UObject) -> None:
    if evaluator.Expression1:
        new_expression = unrealsdk.ConstructObject(Class=evaluator.Expression1.Class, Outer=evaluator,
                                                   Name=f"{evaluator.Expression1.Name}_1",
                                                   Template=evaluator.Expression1)
        unrealsdk.KeepAlive(new_expression)
        new_expression.ObjectFlags.B |= 4
        evaluator.Expression1 = new_expression
    if evaluator.Expression2:
        new_expression = unrealsdk.ConstructObject(Class=evaluator.Expression1.Class, Outer=evaluator,
                                                   Name=f"{evaluator.Expression1.Name}_2",
                                                   Template=evaluator.Expression1)
        unrealsdk.KeepAlive(new_expression)
        new_expression.ObjectFlags.B |= 4
        evaluator.Expression1 = new_expression


def skill_constraints_helper(new_obj: unrealsdk.UObject) -> None:
    number = 1000
    for i, constraint in enumerate(new_obj.SkillConstraints):
        if constraint.Evaluator:
            obj = constraint.Evaluator
            new_constraint = unrealsdk.ConstructObject(Class=obj.Class, Outer=new_obj,
                                                       Name=f"{obj.Name}_{number}",
                                                       Template=obj)
            unrealsdk.KeepAlive(new_constraint)
            new_constraint.ObjectFlags.B |= 4
            new_obj.SkillConstraints[i].Evaluator = new_constraint
            evaluator_expression_helper(new_constraint)
        else:
            for j, obj in enumerate(constraint.EvaluatorDefinitions):
                new_constraint = unrealsdk.ConstructObject(Class=obj.Class, Outer=new_obj,
                                                           Name=f"{obj.Name}_{number}",
                                                           Template=obj)
                unrealsdk.KeepAlive(new_constraint)
                new_constraint.ObjectFlags.B |= 4
                new_obj.SkillConstraints[i].EvaluatorDefinitions[j] = new_constraint
                evaluator_expression_helper(new_constraint)
        number += 1


def append_classmoddefinitions(com_def: unrealsdk.UObject) -> None:
    req_player_class = com_def.PathName(com_def.RequiredPlayerClass)
    com_balance = None
    if "Assassin" in req_player_class:
        com_balance = unrealsdk.FindObject("ClassModBalanceDefinition",
                                           "GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin")
    elif "Mercenary" in req_player_class:
        com_balance = unrealsdk.FindObject("ClassModBalanceDefinition",
                                           "GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary")
    elif "Siren" in req_player_class:
        com_balance = unrealsdk.FindObject("ClassModBalanceDefinition",
                                           "GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren")
    elif "Soldier" in req_player_class:
        com_balance = unrealsdk.FindObject("ClassModBalanceDefinition",
                                           "GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier")
    elif "Psycho" in req_player_class:
        com_balance = unrealsdk.FindObject("ClassModBalanceDefinition", "GD_Lilac_ClassMods."
                                                                        "BalanceDefs.BalDef_ClassMod_Psycho")
    elif "Mechromancer" in req_player_class:
        com_balance = unrealsdk.FindObject("ClassModBalanceDefinition", "GD_Tulip_ItemGrades.ClassMods."
                                                                        "BalDef_ClassMod_Mechromancer")
    if com_balance:
        new_class_mod_definitions = [x for x in com_balance.ClassModDefinitions]
        new_class_mod_definitions.append(com_def)
        com_balance.ClassModDefinitions = new_class_mod_definitions


def append_attr_presentation_def(presentation_def: unrealsdk.UObject) -> None:
    category = presentation_def.PathName(presentation_def).split(".")[1]
    if category == "Artifacts":
        presentation_list = unrealsdk.FindObject("AttributePresentationListDefinition",
                                                 "GD_AttributePresentation._AttributeList."
                                                 "ArtifactOverridePresentationList")
    elif category == "ClassMods_Only":
        presentation_list = unrealsdk.FindObject("AttributePresentationListDefinition",
                                                 "GD_AttributePresentation._AttributeList."
                                                 "ClassModOverridePresentationList")
    elif category == "GrenadeMod":
        presentation_list = unrealsdk.FindObject("AttributePresentationListDefinition",
                                                 "GD_AttributePresentation._AttributeList."
                                                 "GrenadeModOverridePresentationList")
    elif category == "Inventory" or category == "Echo":
        presentation_list = unrealsdk.FindObject("AttributePresentationListDefinition",
                                                 "GD_AttributePresentation._AttributeList."
                                                 "ItemOverridePresentationList")
    elif category == "Weapons":
        presentation_list = unrealsdk.FindObject("AttributePresentationListDefinition",
                                                 "GD_AttributePresentation._AttributeList."
                                                 "WeaponOverridePresentationList")
    elif category == "Shields":
        presentation_list = unrealsdk.FindObject("AttributePresentationListDefinition",
                                                 "GD_AttributePresentation._AttributeList."
                                                 "ShieldOverridePresentationList")
    else:
        presentation_list = unrealsdk.FindObject("AttributePresentationListDefinition",
                                                 "GD_AttributePresentation._AttributeList."
                                                 "DefaultPresentationList")

    temp = [x for x in presentation_list.Attributes]
    temp.append(presentation_def)
    presentation_list.Attributes = temp


def attribute_definition_helper(new_obj: unrealsdk.UObject) -> None:
    if new_obj.ValueResolverChain:
        counter = 0
        temp = []
        for value in new_obj.ValueResolverChain:
            new_value = unrealsdk.ConstructObject(Class=value.Class, Outer=new_obj,
                                                  Name=f"{value.Name}_{counter}",
                                                  Template=value)
            unrealsdk.KeepAlive(new_value)
            new_value.ObjectFlags.B |= 4
            temp.append(new_value)
            counter += 1
        new_obj.ValueResolverChain = temp

    if new_obj.ContextResolverChain:
        counter = 0
        temp = []
        for context in new_obj.ContextResolverChain:
            new_context = unrealsdk.ConstructObject(Class=context.Class, Outer=new_obj,
                                                    Name=f"{context.Name}_{counter}",
                                                    Template=context)
            unrealsdk.KeepAlive(new_context)
            new_context.ObjectFlags.B |= 4
            temp.append(new_context)
            counter += 1
        new_obj.ContextResolverChain = temp


def population_definition_helper(new_obj: unrealsdk.UObject, template_obj: unrealsdk.UObject) -> None:
    counter = 1000
    spawn_factories = []
    for l in template_obj.ActorArchetypeList:
        factory = l.SpawnFactory
        new = unrealsdk.ConstructObject(Class=factory.Class, Outer=new_obj, Name=f"{new_obj.name}_{counter}",
                                        Template=template_obj)
        counter += 1
        unrealsdk.KeepAlive(new)
        new.ObjectFlags.B |= 4
        spawn_factories.append(new)

    new_obj.ActorArchetypeList = [(x, (1, None, None, 1), (0, None, None, 0), False, False) for x in
                                  spawn_factories]


def bpd_copy_helper(new_obj: unrealsdk.UObject) -> None:
    if new_obj.BehaviorProviderDefinition:
        new_bpd = unrealsdk.ConstructObject(Class="BehaviorProviderDefinition", Outer=new_obj,
                                            Name=f"{new_obj.BehaviorProviderDefinition.Name}_0",
                                            Template=new_obj.BehaviorProviderDefinition)
        unrealsdk.KeepAlive(new_bpd)
        new_bpd.ObjectFlags.B |= 4
        new_obj.BehaviorProviderDefinition = new_bpd
        bpd_helper(new_bpd)


def behavior_attribute_effect_helper(new_obj: unrealsdk.UObject) -> None:
    if new_obj.AttributeEffect:
        new_effect = unrealsdk.ConstructObject(Class=new_obj.AttributeEffect.Class, Outer=new_obj,
                                               Name=f"{new_obj.AttributeEffect.Name}_1",
                                               Template=new_obj.AttributeEffect)
        unrealsdk.KeepAlive(new_effect)
        new_effect.ObjectFlags.B |= 4
        new_obj.AttributeEffect = new_effect
        if new_effect == unrealsdk.FindClass("SkillDefinition"):
            bpd_copy_helper(new_effect)
            skill_constraints_helper(new_effect)


def on_any_impact_helper(new_obj: unrealsdk.UObject) -> None:
    if new_obj.OnAnyImpact:
        new_on_any_impact = []
        counter = 0
        for behavior in new_obj.OnAnyImpact:
            new_behavior = unrealsdk.ConstructObject(Class=behavior.Class, Outer=new_obj,
                                                     Name=f"{behavior.Name}_{counter}",
                                                     Template=behavior)
            counter += 1
            unrealsdk.KeepAlive(new_behavior)
            new_behavior.ObjectFlags.B |= 4
            new_on_any_impact.append(new_behavior)
            if behavior.Class == unrealsdk.FindClass("Behavior_AttributeEffect"):
                behavior_attribute_effect_helper(new_behavior)
        new_obj.OnAnyImpact = new_on_any_impact


def behavior_activate_skill_helper(new_obj: unrealsdk.UObject) -> None:
    if new_obj.SkillToActivate:
        name = bl2tools.get_obj_path_name(new_obj)
        new_name = f'{name.split(":")[0].split("_")[-1]}_Skill_{name.split("_")[-1]}'
        new_skill = unrealsdk.ConstructObject(Class=new_obj.SkillToActivate.Class,
                                              Outer=new_obj.SkillToActivate.Outer,
                                              Name=new_name,
                                              Template=new_obj.SkillToActivate)
        unrealsdk.KeepAlive(new_skill)
        new_skill.ObjectFlags.B |= 4
        new_obj.SkillToActivate = new_skill
        bpd_copy_helper(new_skill)


def bpd_helper(new_bpd: unrealsdk.UObject) -> None:
    counter = 0
    for Sequence in new_bpd.BehaviorSequences:
        for Data in Sequence.BehaviorData2:
            if Data.Behavior:
                new_behavior = unrealsdk.ConstructObject(Class=Data.Behavior.Class, Outer=new_bpd,
                                                         Name=f"{Data.Behavior.Name}_{counter}",
                                                         Template=Data.Behavior)
                unrealsdk.KeepAlive(new_behavior)
                new_behavior.ObjectFlags.B |= 4
                Data.Behavior = new_behavior
                counter += 1
                if Data.Behavior.Class == unrealsdk.FindClass("Behavior_AttributeEffect"):
                    behavior_attribute_effect_helper(new_behavior)
                elif Data.Behavior.Class == unrealsdk.FindClass("Behavior_ActivateSkill"):
                    behavior_activate_skill_helper(new_behavior)


def material_instance_constant_copy_helper(template_obj: unrealsdk.UObject, new_obj: unrealsdk.UObject) -> None:
    new_obj.SetParent(template_obj)


def projectile_body_composition_helper(template_obj: unrealsdk.UObject, new_obj: unrealsdk.UObject) -> None:
    for i, data_union in enumerate(template_obj.BodyComposition.Attachments):
        if data_union.Data.ComponentData.Component:
            template = data_union.Data.ComponentData.Component
            new_comp = unrealsdk.ConstructObject(Class=template.Class, Outer=new_obj,
                                                 Name=f"{template.Name}_{i}", Template=template)
            unrealsdk.Log(bl2tools.get_obj_path_name(new_comp))
            unrealsdk.KeepAlive(new_comp)
            if new_comp:
                new_comp.ObjectFlags.B |= 4
                try:
                    unrealsdk.Log(new_obj.BodyComposition.Attachments)
                    new_obj.BodyComposition.Attachments[i].Data.ComponentData.Component = new_comp
                    unrealsdk.Log("works")
                except Exception as e:
                    unrealsdk.Log(f"Exception: {repr(e)}")
                    unrealsdk.Log(e)


@logging.log_all_calls(logging.call_logger)
class Constructor:

    def __init__(self, path: os.PathLike) -> None:
        self.PATH = path
        self.c_files = []
        self.l_files = []

    def Enable(self) -> None:
        self.load_files()
        self.keep_loaded()
        self.construct()

    def Disable(self) -> None:
        pass

    def load_files(self) -> None:
        for root, _dirs, filenames in os.walk(self.PATH):
            for file in filenames:
                if file.lower().endswith(".construct"):
                    self.c_files.append(os.path.join(root, file))
                elif file.lower().endswith(".loaded"):
                    self.l_files.append(os.path.join(root, file))

    def construct(self) -> None:
        """
        This function reads in all lines from any "*.construct" file from any folder.
        The lines that start with "#" decide in what class the newly constructed object belongs.
        The lines that start with "-" get ignored and can be used as a comment.
        If you add a string behind the to be constructed-object, it will be used as the new objects name.
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
                                new_name = f"{cloned_obj.Name}Cloned"

                                if "Constant" in in_class:
                                    new_object = unrealsdk.ConstructObject(Class=in_class, Outer=cloned_obj.Outer,
                                                                           Name=new_name,
                                                                           Template=cloned_obj.Template)
                                else:
                                    new_object = unrealsdk.ConstructObject(Class=in_class, Outer=cloned_obj.Outer,
                                                                           Name=new_name,
                                                                           Template=cloned_obj)
                            elif len(obj_name) == 2:
                                new_name = obj_name[1].strip()
                                if "Constant" in in_class:
                                    new_object = unrealsdk.ConstructObject(Class=in_class, Outer=cloned_obj.Outer,
                                                                           Name=new_name,
                                                                           Template=cloned_obj.Template)
                                else:
                                    new_object = unrealsdk.ConstructObject(Class=in_class, Outer=cloned_obj.Outer,
                                                                           Name=new_name,
                                                                           Template=cloned_obj)
                            elif len(obj_name) == 3:
                                new_name = obj_name[1].strip()
                                outer = unrealsdk.FindObject("Object", obj_name[2].strip())
                                if "Constant" in in_class:
                                    new_object = unrealsdk.ConstructObject(Class=in_class, Outer=outer,
                                                                           Name=new_name,
                                                                           Template=cloned_obj.Template)
                                else:
                                    new_object = unrealsdk.ConstructObject(Class=in_class, Outer=outer,
                                                                           Name=new_name,
                                                                           Template=cloned_obj)
                            unrealsdk.KeepAlive(new_object)
                            new_object.ObjectFlags.B |= 4
                            if in_class == "WeaponBalanceDefinition":
                                weapon_partlist_helper(cloned_obj, new_object)
                            elif in_class == "ClassModBalanceDefinition":
                                com_partlist_helper(cloned_obj, new_object)
                            elif in_class == "InventoryBalanceDefinition":
                                inv_partlist_helper(cloned_obj, new_object)
                            elif in_class in ("ClassModDefinition", "CrossDLCClassModDefinition"):
                                try:
                                    custom_presentation_helper(cloned_obj, new_object)
                                except:
                                    logging.logger.debug(
                                        f"{cloned_obj.PathName(cloned_obj)} does not have its own custom presentation!")

                                append_classmoddefinitions(new_object)
                            elif in_class == "AttributePresentationDefinition":
                                append_attr_presentation_def(new_object)
                            elif in_class == "GrenadeModPartDefinition":
                                try:
                                    custom_presentation_helper(cloned_obj, new_object)
                                except:
                                    logging.logger.debug(
                                        f"{cloned_obj.PathName(cloned_obj)} does not have its own custom presentation!")
                            elif in_class in ("WeaponNamePartDefinition", "ShieldDefinition",
                                              "ArtifactPartDefinition", "ItemNamePartDefinition",
                                              "WeaponTypeDefinition"):
                                try:
                                    custom_presentation_helper(cloned_obj, new_object)
                                except:
                                    logging.logger.debug(
                                        f"{cloned_obj.PathName(cloned_obj)} does not have its own custom presentation!")
                            elif in_class == "BehaviorProviderDefinition":
                                bpd_helper(new_object)
                            elif in_class == "Behavior_AttributeEffect":
                                behavior_attribute_effect_helper(new_object)
                            elif in_class in ("AttributeDefinition", "InventoryAttributeDefinition",
                                              "ResourcePoolAttributeDefinition", "DesignerAttributeDefinition"):
                                attribute_definition_helper(new_object)

                            if in_class in ("ProjectileDefinition", "WeaponPartDefinition", "ShieldPartDefinition",
                                            "ShieldDefinition", "SkillDefinition", "ArtifactDefinition",
                                            "GrenadeModDefinition", "ClassModDefinition", "UsableItemDefinition",
                                            "ArtifactPartDefinition"):
                                bpd_copy_helper(new_object)
                            if in_class == "FiringModeDefinition":
                                on_any_impact_helper(new_object)
                            if in_class == "ProjectileDefinition":
                                pass
                                # projectile_body_composition_helper(cloned_obj, new_object)

                            if in_class in ("ShieldPartDefinition", "WeaponPartDefinition"):
                                try:
                                    custom_presentation_helper(cloned_obj, new_object)
                                except:
                                    logging.logger.debug(
                                        f"{cloned_obj.PathName(cloned_obj)} does not have its own custom presentation!")
                            if in_class == "SkillDefinition":
                                try:
                                    skill_presentation_helper(cloned_obj, new_object)
                                    skill_constraints_helper(new_object)
                                except:
                                    logging.logger.verbose(
                                        f"{cloned_obj.PathName(cloned_obj)} does not have presentations!")
                            if in_class == "PopulationDefinition":
                                population_definition_helper(new_object, cloned_obj)

                            if in_class == "MaterialInstanceConstant":
                                material_instance_constant_copy_helper(cloned_obj, new_object)
                    except Exception as e:
                        logging.logger.error(f"{e}")
                        logging.logger.error(f"An exception occurred in {file}")
                        logging.logger.error(f"Please check this line: {line}")

    def keep_loaded(self) -> None:
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
