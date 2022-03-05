#!/usr/bin/python3
""" define basemodel"""


from unicodedata import name
import uuid
from datetime import datetime
#importo models puedo acceder a todo lo que este dentro del __init__.py
import models
# format date
fd = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ class BaseModel """

    def __init__(self, *args, **kwargs):
        """Methode init(self)  """
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
        """ Methode str """
        name = BaseModel.__name__
        return ("[{}] ({}) {}".format(name, self.id, self.__dict__))
