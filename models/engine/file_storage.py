#!/usr/bin/python3
""" define file storage"""
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances toa JSON  fiel and deserialize file to instances"""
    # __file_path: string - path to the JSON file (ex: file.json)
    __file_path = "file.json"
    # __objects: dictionary - empty but will
    # store all objects by <class name>.id
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        # BaseModel.12121212
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        json_obj = self.__objects.copy()
        for key, val in self.__objects.items():
            json_obj[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            file.write(json.dumps(json_obj))

    def reload(self):
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                json_read = json.load(file)
                for keys, value in json_read.items():
                    class_name = value["__class__"]
                    self.new(class_dict[class_name](**value))
        except FileNotFoundError:
            pass
