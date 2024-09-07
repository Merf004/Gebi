import pandas as pd
import json
from datetime import date, datetime

# Class Books
class Books:
    list_books = []
    b = 1
    def __init__(self, title, author, gender, isbn, statut, date_pub) -> None:
        self.id = Books.b
        self.title = title
        self.author = author
        self.gender = gender
        self.isbn = isbn
        self.statut = statut
        self.date_pub = date_pub
        
        Books.b += 1
        obj_dict = {"id":self.id, "title": self.title, "author": self.author, "gender": self.gender, "isbn": self.isbn, "statut": self.statut, "Release date": str(self.date_pub)}
        Books.list_books.append(obj_dict)
        
        with open("data/books.json", "w", encoding="utf-8") as f:
            json.dump(Books.list_books, f, indent=4, ensure_ascii=False) 
            
    def to_dict(self):
        return {"id":self.id, "title": self.title, "author": self.author, "gender": self.gender, "isbn": self.isbn, "statut": self.statut, "Release date": str(self.date_pub)}


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
        "Historical",
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
    
    print("Enter the publication date")
    y = int(input("Year: "))
    while (y < 1900) or (y > 2024):
        y = int(input("Invalid year. Enter the year: "))
    m = int(input("Month: "))
    while (m < 1) or (m > 12):
        m = int(input("Invalid month. Enter the month: "))    
    d = int(input("Day: "))
    while (d < 1) or (d > 31):
        d = int(input("Invalid day. Enter the day: "))
    
    pub_date = str(date(y, m, d))
    print("The publication date entered is valid : ", pub_date)  
        
    b = Books(title, author, gender, isbn, statut, pub_date)
    

# Function to delete a book
def del_book():
    id_book = int(input('Enter the ID of the book to be deleted: '))
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
            

# Function to show all books
def show_book():
    df = pd.DataFrame(Books.list_books)
    print(df)
    
# Function to show the books by gender
def show_book_gender():
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
        "Historical",
        "Utopie",
        "Dystopie",
        "Humor"]
    print(list_gender)
    while gender  not in list_gender:
        gender = input("Enter the genre of the book: ")
    list_book_by_gender = []
    for book in Books.list_books:
        if book["gender"] == gender:
            list_book_by_gender.append(book)
    if list_book_by_gender == []:
        print(f"There is no book {gender}")
    else:
        df = pd.DataFrame(list_book_by_gender)
        print(df)        


# Function to modify book title
def modify_book_title(book_id):
    title = ''
    while len(title) < 3:
        title = input("Enter book title (minimum 3 characters): ")
    Books.list_books[book_id - 1]["title"] = title
    print(f"The title of the book ID {book_id} has been changed with success")
    
    with open("data/books.json", "w", encoding="utf-8") as f:
            json.dump(Books.list_books, f, indent=4, ensure_ascii=False)


# Function to modify book author name
def modify_book_author_name(book_id):
    author = ''
    while len(author) < 3:
        author = input("Enter book author name (minimum 3 characters): ")
    Books.list_books[book_id - 1]["author"] = author
    print(f"The author name of the book ID {book_id} has been changed with success")
    
    with open("data/books.json", "w", encoding="utf-8") as f:
            json.dump(Books.list_books, f, indent=4, ensure_ascii=False)    
            
# Function to modify book gender
def modify_gender(book_id):
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
        "Historical",
        "Utopie",
        "Dystopie",
        "Humor"]
    print(list_gender)
    while gender  not in list_gender:
        gender = input("Enter the genre of the book: ")
    
    Books.list_books[book_id - 1]["gender"] = gender
    print(f"The gender of the book ID {book_id} has been changed with success")

    with open("data/books.json", "w", encoding="utf-8") as f:
            json.dump(Books.list_books, f, indent=4, ensure_ascii=False)    
            
# Function to modify ISBN
def modify_isbn(book_id):
    isbn = ''
    while not (isbn.isnumeric() and len(isbn) == 13):
        isbn = input("Enter the book's ISBN (International Standard Book Number). Make sure it contains exactly 13 digits :\n")
    
    Books.list_books[book_id - 1]["isbn"] = isbn    
    print(f"The ISBN of the book ID {book_id} has been changed with success")

    with open("data/books.json", "w", encoding="utf-8") as f:
            json.dump(Books.list_books, f, indent=4, ensure_ascii=False)  
            
# Function to modify the publication date
def modify_pub_date(book_id):
    print("Enter new the publication date")
    y = int(input("Year: "))
    while (y < 1900) or (y > 2024):
        y = int(input("Invalid year. Enter the year: "))
    m = int(input("Month: "))
    while (m < 1) or (m > 12):
        m = int(input("Invalid month. Enter the month: "))    
    d = int(input("Day: "))
    while (d < 1) or (d > 31):
        d = int(input("Invalid day. Enter the day: "))
    
    pub_date = str(date(y, m, d))
    Books.list_books[book_id - 1]["Release date"] = pub_date    
    print(f"The publication date of the book ID {book_id} has been changed with success")

    with open("data/books.json", "w", encoding="utf-8") as f:
            json.dump(Books.list_books, f, indent=4, ensure_ascii=False) 
            
# Function for sorting books by title
def sort_title():
    t = sorted(Books.list_books, key=lambda x: x['title'])
    df = pd.DataFrame(t)
    print(df)    
    
# Function for sorting books by author name
def sort_author_name():
    t = sorted(Books.list_books, key=lambda x: x['author'])
    df = pd.DataFrame(t)
    print(df)  
    
# Function for sorting books by publication date
def sort_pub_date():
    t = sorted(Books.list_books, key=lambda x: x['Release date'])
    df = pd.DataFrame(t)
    print(df)  
    
# Search function for books written by an author
def show_book_author():
    author = input("Enter the author name: ")
    list_book_by_author = []
    for book in Books.list_books:
        if book["author"] == author:
            list_book_by_author.append(book)
    if list_book_by_author == []:
        print(f"The author {author} has no book or does not exist")
    else:
        df = pd.DataFrame(list_book_by_author)
        print(df) 
