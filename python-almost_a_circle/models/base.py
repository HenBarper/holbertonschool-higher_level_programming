#!/usr/bin/python3
"""
class Base:

private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute
    id with this argument value - you can assume id is an
    integer and you don’t need to test the type of it
otherwise, increment __nb_objects and assign the new
    value to the public instance attribute id
"""
import json


class Base():
    """Base class for all shapes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init method"""
        if id is not None:
            self.id = id
        else:
            #Base.__nb_objects += 1
            self.id = Base.__nb_objects
        #Base.__nb_objects += 1
        Base.add_base()

    @classmethod
    def add_base(cls):
        """class method"""
        Base.__nb_objects += 1

    @classmethod
    def num_obj(cls):
        """Property width to retrieve it"""
        return cls.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Func to make into json file"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Func to write json str to file"""
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """returns list of json string data"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        if cls.__name__ == "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        the_file = cls.__name__ + ".json"
        all_instances = []
        try:
            with open(the_file, 'r', encoding='utf-8') as file:
                all_instances = cls.from_json_string(file.read())
            for key, value in enumerate(all_instances):
                all_instances[key] = cls.create(**all_instances[key])
        except:
            pass
        return all_instances
