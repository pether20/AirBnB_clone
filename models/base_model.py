#!/usr/bin/python3
"""
Class BaseModel
"""

from datetime import datetime
import uuid
import models
# dtm = date format
dtm = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base Model"""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel"""
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)
            if hasattr(self, 'created_at') and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], dtm)
            if hasattr(self, 'updated_at') and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], dtm)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """str representation"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the public ins attr upd_at with the curren one"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dic containing keys and values of the instance"""
        n_dict = self.__dict__.copy()
        if "created_at" in n_dict:
            n_dict["created_at"] = n_dict["created_at"].strftime(dtm)
        if "updated_at" in n_dict:
            n_dict["updated_at"] = n_dict["updated_at"].strftime(dtm)
        n_dict["__class__"] = self.__class__.__name__
        return n_dict
