import json

class Books:
    list_books = []
    b = 1
    def __init__(self, title, author, gender, isbn, statut) -> None:
        self.id = Books.b
        self.title = title
        self.author = author
        self.gender = gender
        self.isbn = isbn
        self.statut = statut
        
        Books.b += 1
        obj_dict = {"id":self.id, "title": self.title, "author": self.author, "gender": self.gender, "isbn": self.isbn, "statut": self.statut}
        Books.list_books.append(obj_dict)
        
        with open("data/books.json", "w", encoding="utf-8") as f:
            json.dump(Books.list_books, f, indent=4, ensure_ascii=False) 
            
    def to_dict(self):
        return {"id":self.id, "title": self.title, "author": self.author, "gender": self.gender, "isbn": self.isbn, "statut": self.statut}
