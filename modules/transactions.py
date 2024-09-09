import json
from datetime import date, datetime
from modules.users import *
from modules.books import *
import pandas as pd

class Transactions:
    list_transactions = []
    t = 1
    
    def __init__(self, date, user, book, type) -> None:
        self.id = Transactions.t
        self.date = date
        self.user = user
        self.book = book
        self.type = type
        
        Transactions.t += 1
        obj_user = {"id":self.user["id"], "first name": self.user["first name"], "last name": self.user["last name"], "gender": self.user["gender"], "age": self.user["age"]}  
        obj_book = {"id":self.book["id"], "title": self.book["title"], "author": self.book["author"], "gender": self.book["gender"], "isbn": self.book["isbn"], "statut": self.book["statut"], "Release date": str(self.book["Release date"])}
      
        obj_dict = {"id":self.id, "date": str(self.date), "user": obj_user, "book": obj_book, "type": self.type}
        Transactions.list_transactions.append(obj_dict)
        if self.type == "Borrow":
            print(f"The ID {self.id} transaction has been add\nTransaction type: Borrow book)")
        else:
            print(f"The ID {self.id} transaction has been add\nTansaction type: Return book")
        
        with open("data/transactions.json", "w", encoding="utf-8") as f:
            json.dump(Transactions.list_transactions, f, indent=4, ensure_ascii=False) 
       
# Function to borrow a book
def borrow_book():
    print("Enter the borrow date")
    y = int(input("Year: "))
    while (y < 1900) or (y > 2024):
        y = int(input("Invalid year. Enter the year: "))
    m = int(input("Month: "))
    while (m < 1) or (m > 12):
        m = int(input("Invalid month. Enter the month: "))    
    d = int(input("Day: "))
    while (d < 1) or (d > 31):
        d = int(input("Invalid day. Enter the day: "))
    
    borrow_date = str(date(y, m, d))
    print("The borrow date entered is valid : ", borrow_date)  
     
    list_userID = []
    for u in Users.list_users:
        list_userID.append(u["id"])
    while True:
        userID_str = input("Enter the user ID: ")

        if userID_str.isdigit():
            userID = int(userID_str)

            if userID in list_userID:
                print(f"Done: User ID {userID}")
                break
            else:
                print(f"User ID {userID} does not exist in database")
        else:
            print("Error: Please enter a valid number (no letters or symbols).")

    for u in Users.list_users:
        if u["id"] == userID:
            user = u
            
    list_bookID = []
    for b in Books.list_books:
        list_bookID.append(b["id"])
    while True:
        bookID_str = input("Enter the book ID: ")

        if bookID_str.isdigit():
            bookID = int(bookID_str)

        
            if bookID in list_bookID:
                print(f"Done: Book ID {bookID}")
                break
            else:
                print(f"Book ID {bookID} does not exist in database")
        else:
            print("Error: Please enter a valid number (no letters or symbols).")
    decl = False
    for b in Books.list_books:
        if b["id"] == bookID and b["statut"] == "Available":
            book = b
            b["statut"] = "Unavailable"
            type_trans = "Borrow"
            decl = True
            t = Transactions(borrow_date, user, book, type_trans)
            with open("data/books.json", "w", encoding="utf-8") as f:
                json.dump(Books.list_books, f, indent=4, ensure_ascii=False) 
    if not decl:
        print("Unable to register this transaction: The book is not available")
    
# Function to return a book
def return_book():
    print("Enter the return date")
    y = int(input("Year: "))
    while (y < 1900) or (y > 2024):
        y = int(input("Invalid year. Enter the year: "))
    m = int(input("Month: "))
    while (m < 1) or (m > 12):
        m = int(input("Invalid month. Enter the month: "))    
    d = int(input("Day: "))
    while (d < 1) or (d > 31):
        d = int(input("Invalid day. Enter the day: "))
    
    return_date = str(date(y, m, d))
    print("The return date entered is valid : ", return_date)  
     
    list_userID = []
    for u in Users.list_users:
        list_userID.append(u["id"])
    while True:
        userID_str = input("Enter the user ID: ")

        if userID_str.isdigit():
            userID = int(userID_str)

            if userID in list_userID:
                print(f"Done: User ID {userID}")
                break
            else:
                print(f"User ID {userID} does not exist in database")
        else:
            print("Error: Please enter a valid number (no letters or symbols).")

    for u in Users.list_users:
        if u["id"] == userID:
            user = u
            
    list_bookID = []
    for b in Books.list_books:
        list_bookID.append(b["id"])
    while True:
        bookID_str = input("Enter the book ID: ")

        if bookID_str.isdigit():
            bookID = int(bookID_str)

        
            if bookID in list_bookID:
                print(f"Done: Book ID {bookID}")
                break
            else:
                print(f"Book ID {bookID} does not exist in database")
        else:
            print("Error: Please enter a valid number (no letters or symbols).")

    for b in Books.list_books:
        if b["id"] == bookID and b["statut"] == "Unavailable":
            book = b
            b["statut"] = "Available"
            type_trans = "Return"
            t = Transactions(return_date, user, book, type_trans)
            with open("data/books.json", "w", encoding="utf-8") as f:
                json.dump(Books.list_books, f, indent=4, ensure_ascii=False)

# Function to show all transactions
def show_trans():
    df = pd.DataFrame(Transactions.list_transactions)
    df.rename(columns={'user': 'user ID'}, inplace=True)
    df.rename(columns={'book': 'book ID'}, inplace=True)
    df['user ID'] = df['user ID'].apply(lambda x: x['id'])
    df['book ID'] = df['book ID'].apply(lambda x: x['id'])
    print(df)
    