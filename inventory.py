




"""
hamed
sohil
nayim
hamed
new file for git branching

"""

<<<<<<< HEAD
import json
from json_handler import database_json
=======
books = [
    {"title": "old man and sea", "writer": "Hemingway", "subject": "Novel", "available": True, "date": "2025-02-08", "clock": "20:37:32.631366"},
    {"title": "pride and prejudice", "writer": "Jane Austen", "subject": "Novel", "available": True, "date": "2025-02-08", "clock": "20:37:32.631366"},
    {"title": "Trout fishing in America", "writer": "Brautigan", "subject": "Novel", "available": True, "date": "2025-02-08", "clock": "20:37:32.631366"},
    {"title": "life of pi", "writer": "Hemingway", "subject": "Novel", "available": True, "date": "2025-02-08", "clock": "20:37:32.631366"}
]
>>>>>>> e144d62f6577032281a2f026b07e49da38510737

<<<<<<< HEAD
class AddItems:
    def __init__(self):
        pass
    
    def add_title(self):
        pass
    
    def hi_class(self):
        pass
    
=======
class SearchItem:
    def __init__(self):
        self.data = self.read_file()
    
    def read_file(self):
        return database_json().read()
    
    def display(self):
        for dict in self.data :
            print(dict)
            
            
            

<<<<<<< HEAD
D = SearchItem().display()
=======
for book in books:
    print(f"Title: {book['title']}")
    print(f"Writer: {book['writer']}")
    print(f"Subject: {book['subject']}")
    print(f"Available: {book['available']}")
    print(f"Date: {book['date']}")
    print(f"Clock: {book['clock']}")
>>>>>>> e144d62f6577032281a2f026b07e49da38510737
>>>>>>> develop
