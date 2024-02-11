#!/usr/bin/python3

import json
import os

class FileStorage():
        
    def __init__(self):
        self.__objects = {}
        self.__file_path = "file.json"

    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        abs_file_path = os.path.abspath(self.__file_path)
        with open(abs_file_path, 'a') as f:
            serializable_objects =  {}
            for key, obj in self.__objects.items():
                if hasattr(obj, 'to_dict'):
                    serializable_objects[key] = obj.to_dict()
            json.dump(serializable_objects, f)
            f.write('\n')
    
    def reload(self):
        abs_file_path = os.path.abspath(self.__file_path)
        if os.path.exists(self.__file_path):
            with open(abs_file_path, 'r') as f:
                self.__objects = {}
                for line in f:
                    obj = json.loads(line)
                    key = list(obj.keys())[0]
                    self.__objects[key] = obj[key]
        else:
            pass
