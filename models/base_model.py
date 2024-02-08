#!/usr/bin/python3

"""Base Module"""

import uuid
from datetime import datetime

class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    
    def __init__(self):
        self.id = BaseModel.id
        self.created_at = BaseModel.created_at
        self.updated_at = BaseModel.updated_at
            
    
    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    
    def save(self):
        '''Method to update the public instance attribute "updated_at"
        With the current datetime'''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''Method to generate a dictionary representation of the instance BaseModel'''
        class_name = self.__class__.__name__
        attributes = vars(self)
        instace_dict = {**attributes, '__class__': class_name}
        instace_dict['created_at'] = datetime.isoformat(self.created_at)
        instace_dict['updated_at'] = datetime.isoformat(self.updated_at)
        return instace_dict