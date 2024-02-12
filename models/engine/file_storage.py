#!/usr/bin/python3
"""
    module contains class that serializes instances to JSON file
    and deserializes JSON file to instances
"""
from datetime import datetime
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    __file_path = "file.json"
    __objects = {}
    classes = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review
            }

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """creates a new object"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes object into JSON - file.json"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes objects from JSON file into object dictionary."""
        try:
            with open(self.__file_path) as obj_file:
                file_content = obj_file.read()
                if file_content:
                    loaded_objects = json.loads(file_content)
                    for key, obj_dict in loaded_objects.items():
                        class_name, obj_id = key.split('.')
                        obj_dict["created_at"] = datetime.strptime(
                                obj_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                                )
                        obj_dict["updated_at"] = datetime.strptime(
                                obj_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                                )
                        class_definition = globals()[class_name]
                        obj = class_definition(**obj_dict)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
