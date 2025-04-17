



"""
new file for git branching
"""

books = [
    {"title": "old man and sea", "writer": "Hemingway", "subject": "Novel", "available": True, "date": "2025-02-08", "clock": "20:37:32.631366"},
    {"title": "pride and prejudice", "writer": "Jane Austen", "subject": "Novel", "available": True, "date": "2025-02-08", "clock": "20:37:32.631366"},
    {"title": "Trout fishing in America", "writer": "Brautigan", "subject": "Novel", "available": True, "date": "2025-02-08", "clock": "20:37:32.631366"},
    {"title": "life of pi", "writer": "Hemingway", "subject": "Novel", "available": True, "date": "2025-02-08", "clock": "20:37:32.631366"}
]


for book in books:
    print(f"Title: {book['title']}")
    print(f"Writer: {book['writer']}")
    print(f"Subject: {book['subject']}")
    print(f"Available: {book['available']}")
    print(f"Date: {book['date']}")
    print(f"Clock: {book['clock']}")