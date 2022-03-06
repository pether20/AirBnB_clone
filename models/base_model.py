#!/usr/bin/python3
"""
Class BaseModel for Airbnb
"""
import uuid
from datetime import datetime
import models
# format date
fd = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """Methode init_self"""
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)
            if type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], fd)
            if type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], fd)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Methode save """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Methode to dict"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict

    def __str__(self):
        """Methode str """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)
