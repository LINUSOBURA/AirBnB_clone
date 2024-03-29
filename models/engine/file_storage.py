#!/usr/bin/python3
"""File Storage Module"""
import json
import os

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    def __init__(self):
        self.__objects = {}
        self.__file_path = "file.json"

    def all(self):
        """All Objects"""
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            obj_dict = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(obj_dict, f, indent=4, sort_keys=True, default=str)

    def reload(self):
        all_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    name = key.split(".")[0]
                    if name in all_classes:
                        obj = all_classes[name](**value)
                        self.__objects[key] = obj
