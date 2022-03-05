#!/usr/bin/python3
""" define file storage"""
import json
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances toa JSON  fiel and deserialize file to instances"""
    # __file_path: string - path to the JSON file (ex: file.json)
    __file_path = "file.json"
    # __objects: dictionary - empty but will store
    # all objects by <class name>.id
    __objects = {}

    def all(self):
        """ return all objects in __objects"""
        return self.__objects

    def new(self, obj):
        """ create a object in __onjects"""
        # BaseModel.12121212
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ save a objects in file.json"""
        json_obj = {}
        for k in self.__objects.keys():
            json_obj[k] = self.__objects[k].to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(json_obj, file)

    def reload(self):
        """ get a objects in file.json"""
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                json_read = json.load(file)
            for k in json_read:
                self.__objects[k] = BaseModel(**json_read[k])
        except FileNotFoundError:
            pass
