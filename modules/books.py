import json

# Class Books
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


# Function to add a book
def add_book():
    title = ''
    while len(title) < 3:
        title = input("Enter book title (minimum 3 characters): ")
    print("The title entered is valid: ", title)
    
    author = ''
    while len(author) < 3:
        author = input("Enter book author's name (3 characters minimum): ")
    print("Author name entered is valid: ", author)
    gender = ""
    list_gender = [
        "Drama"
        "Fiction",
        "Science-fiction",
        "Fantasy",
        "Police",
        "Horror",
        "Biography",
        "Essai",
        "Documentary",
        "Handbook",
        "Poetry",
        "Theater",
        "Children",
        "Young Adult",
        "BD",
        "historical",
        "Utopie",
        "Dystopie",
        "Humor"]
    print(list_gender)
    while gender  not in list_gender:
        gender = input("Enter the genre of the book: ")
    print("The genre entered is valid: ", gender)
    
    isbn = ''
    while not (isbn.isnumeric() and len(isbn) == 13):
        isbn = input("Enter the book's ISBN (International Standard Book Number). Make sure it contains exactly 13 digits :\n")
    
    print("The ISBN entered is valid : ", isbn)    
    
    statut = "Available"
    
    b = Books(title, author, gender, isbn, statut)
    

# Function to delete a book
def del_book():
    id_book = int(input('Enter the id of the book to be deleted: '))
    book_del = Books.list_books[id_book - 1]
    book_title = book_del["title"]
    answer = ''
    while not (answer == 'Yes' or answer == 'No'):
        answer = input(f"Do you really want to delete the book \"{book_title}\"?(Yes or No)\n")
    if answer == "Yes":
        del Books.list_books[id_book - 1]
        print("Book removed")
    elif answer == 'No':
        print('The book has not been removed')
    
    with open("data/books.json", "w", encoding="utf-8") as f:
            json.dump(Books.list_books, f, indent=4, ensure_ascii=False)