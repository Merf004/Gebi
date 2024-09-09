from modules.books import *
from modules.transactions import *
from modules.users import *


def main_menu():
    while True:
        print("Main menu")
        print("1. Books management")
        print("2. Users management")
        print("3. Transactions management")
        print("0. Exit")
    
        choice = input("Choice: ")
        
        if choice == '1':
            books_management()
        elif choice == '2':
            users_management()
        elif choice == '3':
            transactions_management()
        elif choice == '0':
            break
        else:
            print("Please try again")
            
def books_management():
    while True:
        print("Book management")
        print("1. Add a new book")
        print("2. Delete a book")
        print("3. Show books")
        print("4. modify books")
        print("5. Search a book")
        print("0. Return")
        
        choice = input("Choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            del_book()
        elif choice == '3':
            menu_show_book()
        elif choice == '4':
            menu_modify_book()
        elif choice == '5':
            search_book()
        elif choice == '0':
            break
        else:
            print("Please try again")
        
def menu_show_book():
    while True:
        print('Show book')
        print("1. Show all books")
        print("2. Show books by gender")
        print("3. Sort books by title")
        print("4. Sort books by author name")
        print("5. Sort books by publication date")
        print("6. Books written by an author")
        print("7. All available books")
        print("8. All unavailable books")
        print("0. Return")

        choice = input("Choice: ")
        if choice == "1":
            show_books()
        elif choice == "2":
            show_book_gender()   
        elif choice == '3':
            sort_title()
        elif choice == '4':
            sort_author_name()
        elif choice == '5':
            sort_pub_date()
        elif choice == '6':
            show_book_author()
        elif choice == '7':
            show_available_book()
        elif choice == '8':
            show_unavailable_book() 
        elif choice == '0':
            break
        else:
            print("Please try again")
            
def menu_modify_book():
    while True:
        print("Modify a book")
        print("1. Modify title")
        print("2. Modify author name")
        print("3. Modify gender")
        print("4. Modify ISBN code")
        print("5. Modify publication date")
        print("0. Return")
        
        choice = input("Choice: ")
        if choice == '1':
            modify_book_title()
        elif choice == '2':
            modify_book_author_name()
        elif choice == '3':
            modify_gender()
        elif choice == '4':
            modify_isbn()
        elif choice == '5':
            modify_pub_date()
        elif choice == '0':
            break
        else:
            print("Please try again") 
            
def users_management():
    while True:
        print("Users management")
        print("1. Add an user")
        print("2. Delete an user")
        print("3. Show users")
        print("4. Modify an user")
        print("5. Search user")
        print("0. Return")
        
        choice = input("Choice: ")
        if choice == "1":
            add_user()
        elif choice == "2":
            del_user()
        elif choice == "3":
            menu_show_user()
        elif choice == "4":
            menu_modify_user()
        elif choice == "5":
            search_user()
        elif choice == "0":
            break
        else:
            print("Please try again") 
            
def menu_show_user():
    while True:
        print("Show users")
        print("1. Show all users")
        print("2. Show users by gender")
        print("3. Sort users by first name")
        print("4. Sort users by last name")
        print("5. Sort users by age")
        print("0. Return")
        
        choice = input('Choice: ')
        if choice == '1':
            show_users()
        elif choice == '2':
            show_users_gender()
        elif choice == '3':
            sort_fn()
        elif choice == '4':
            sort_ln()
        elif choice == '5':
            sort_age()
        elif choice == '0':
            break
        else:
            print("Please try again") 
            
def menu_modify_user():
    while True:
        print("Modify user")
        print("1. Modify user first name")
        print("2. Modify user last name")
        print("0. Return")
        
        choice = input("Choice: ")
        if choice == '1':
            modify_user_fn()
        elif choice == '2':
            modify_user_ln()
        elif choice == '0':
            break
        else:
            print("Please try again") 
            
def transactions_management():
    while True:
        print("Transactions management")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Show transactions")
        print("0. Return")
        
        choice = input("Choice: ")
        if choice == '1':
            borrow_book()
        elif choice == '2':
            return_book()
        elif choice == '3':
            show_trans()
        elif choice == '0':
            break
        else:
            print("Please try again")        
        
    