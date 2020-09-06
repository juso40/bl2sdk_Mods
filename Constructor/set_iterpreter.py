import unrealsdk
from unrealsdk import *

from . import logging

import re


def set(line):
    pattern = re.compile(r"^\s*(set)\s+(\S+)\s+(\S+)\s+\((.*)\)", re.IGNORECASE)  # simple array of objects
    obj = FindObject("Object", line.split()[1])
    if not obj:
        logging.logger.error(f"Could not find Object: {line}")
        return
    re_line = re.match(pattern, line)
    if re_line:
        setattr(FindObject("Object", re_line[2]),
                re_line[3], [FindObject("Object", x.strip()) for x in re_line[4].split(",")])
    else:
        try:
            attributes = line.split()[2].split(".")
            val = FindObject("Object", line.split()[3])  # assume our val is an object
            if not val:
                try:
                    val = float(line.split()[3])  # assume it's a float
                except ValueError:  # obviously not a float nor object
                    val = line.split()[3]
                    if val.lower() == "true":
                        val = True
                    elif val.lower() == "false":
                        val = False
                    elif val.lower() == "none":
                        val = None
            while len(attributes) > 1:
                attribute = attributes.pop(0)
                if "[" in attribute and "]" in attribute:
                    index = int(attribute[attribute.find("[") + 1:attribute.find("]")])
                    obj = getattr(obj, attribute[:attribute.find("[")])[index]
                else:
                    obj = getattr(obj, attribute)
            if "[" in attributes[0] and "]" in attributes[0]:
                attribute = attributes[0]
                index = int(attribute[attribute.find("[") + 1:attribute.find("]")])
                obj = getattr(obj, attribute[:attribute.find("[")])
                obj[index] = val
            else:
                setattr(obj, attributes[0], val)
        except IndexError:
            logging.logger.error(f"IndexError in line:\n->{line}")
        except Exception as e:
            logging.logger.error(e)
            logging.logger.error(f"Could not set using following statement: {line}")
