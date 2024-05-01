#!/usr/bin/pthon3
"""module bears FileStorage"""
import json
from datetime import datetime


class FileStorage:
    """class FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        from .. import base_model, user, place, \
            review, amenity, state, city
        for k, v in FileStorage.__objects.items():
            if type(v) is not dict:
                v = v.to_dict()
            if v['__class__'] == 'BaseModel':
                FileStorage.__objects[k] = base_model.BaseModel(**v)
            elif v['__class__'] == 'User':
                FileStorage.__objects[k] = user.User(**v)
            elif v['__class__'] == 'State':
                FileStorage.__objects[k] = state.State(**v)
            elif v['__class__'] == 'City':
                FileStorage.__objects[k] = city.City(**v)
            elif v['__class__'] == 'Place':
                FileStorage.__objects[k] = place.Place(**v)
            elif v['__class__'] == 'Amenity':
                FileStorage.__objects[k] = amenity.Amenity(**v)
            elif v['__class__'] == 'Review':
                FileStorage.__objects[k] = review.Review(**v)
        return FileStorage.__objects

    def new(self, obj):
        """sets __objects"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON
        file (path: __file_path)"""
        ref = FileStorage.__objects
        for k, v in ref.items():
            if type(v) is not dict:
                FileStorage.__objects[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as s:
            json.dump(FileStorage.__objects, s)

    def reload(self):
        """deserializes the JSON file only if the JSON file exists"""
        try:
            with open(FileStorage.__file_path) as d:
                FileStorage.__objects = json.load(d)
        finally:
            return
