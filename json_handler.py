import os
import json
from abc import ABC, abstractmethod


class BaseFileHandler(ABC):

    def __init__(self, file_path):
        try:
            self.file_path = self.validate_file_path(file_path)
        except Exception as e:
            print(e)

    @staticmethod
    def validate_file_path(path):
        if not os.path.exists(path):
            raise FileNotFoundError("File does not exist")
        return path
    
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data: dict):
        pass


class JsonFileHandler(BaseFileHandler):

    def read(self):
        with open(self.file_path, 'r') as f:
            data = f.read()
            return json.loads(data) if data else []
        return None
    
    def write(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)



def database_json():
    return JsonFileHandler(file_path="CW28\database.json")
    