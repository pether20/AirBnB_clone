#!/usr/bin/python3
""" define basemodel"""
import uuid
import datetime


class BaseModel:
    """ class BaseModel """
    def __init__(self, *args, **kwargs):
        """ self  """ 
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """ save """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ to dict"""
        dict = self.__dict__.copy()
        dict["__class__"] = BaseModel.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict

    def __str__(self):
        """ str """
        return ("[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__))





obj1 = BaseModel()
print(obj1.to_dict)
