#!/usr/bin/python3
""" Defines a Base class """

import json


class Base:
    """ Represents base class
    Attributes:
        __nb_objects (int): number of instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base constructor
        Args:
            id (int): id of instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json string
        Args:
            list_dictionaries (list): list to convert to json
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_of_obj_dict = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_of_obj_dict))

    @staticmethod
    def from_json_string(json_string):
        """ returns an array of objects from json_string
        Args:
           json_string (str): json string representing array of objects
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance from dictionary as its attributes
        Args:
           **dictionary (dict): key/value pairs to be used as attributes
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1,1)
            else:
                new = cls(1)

            new.update(**dictionary)

            return new
        
        @classmethod
    def load_from_file(cls):
        """ returns a list of instances from file
        """
        filename = cls.__name__ + ".json"
        
        try:
            with open(filename) as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**obj) for obj in list_dicts]
        except IOError:
            return []
