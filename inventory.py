



"""
new file for git branching
"""

import json
from json_handler import database_json

class SearchItem:
    def __init__(self):
        self.data = self.read_file()
    
    def read_file(self):
        return database_json().read()
    
    def display(self):
        for dict in self.data :
            print(dict)
            
            
            

D = SearchItem().display()