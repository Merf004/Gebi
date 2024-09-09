import json
import pandas as pd

class Users:
    
    list_users = []
    u = 1
    def __init__(self, f_name, l_name, gender, age) -> None:
        self.id = Users.u
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        self.age = age
        
        Users.u += 1
        obj_dict = {"id":self.id, "first name": self.f_name, "last name": self.l_name, "gender": self.gender, "age": self.age}
        Users.list_users.append(obj_dict)
        print(f"The ID {self.id} user has been added")
        
        with open("data/users.json", "w", encoding="utf-8") as f:
            json.dump(Users.list_users, f, indent=4, ensure_ascii=False)   

# Function to add a new users
def add_user():
    fname = ''
    while len(fname) < 3:
        fname = input("Enter the first name (minimum 3 characters): ")
    print("The first name entered is valid: ", fname)

    lname = ''
    while len(lname) < 3:
        lname = input("Enter the last name (minimum 3 characters): ")
    print("The last name entered is valid: ", lname)
    
    gender = ''
    while (gender != "M") and (gender != 'F'):
        gender = input("Enter the gender (M or F): ")
    print("The gender entered is valid")
    
    while True:
        age_str = input("Enter the age (between 1 and 100): ")

        if age_str.isdigit():
            age = int(age_str)

            if 1 <= age <= 100:
                print("The age entered is valid")
                break
            else:
                print("Error: Age must be between 1 and 100.")
        else:
            print("Error: Please enter a valid number (no letters or symbols).")
            
    u = Users(fname, lname, gender, age)
    
# Function to delete a user 
def del_user():
    id_user = int(input('Enter the ID of the user to be deleted: '))
    index_user_del = next((i for i, obj in enumerate(Users.list_users) if obj['id'] == id_user), None)
    user_del = Users.list_users[index_user_del]
    user_fname = user_del["first name"]
    user_lname = user_del["last name"]
    answer = ''
    while not (answer == 'Yes' or answer == 'No'):
        answer = input(f"Do you really want to delete the user \"{user_fname} {user_lname}\"?(Yes or No)\n")
    if answer == "Yes":
        del Users.list_users[index_user_del]
        print("User removed")
    elif answer == 'No':
        print('The user has not been removed')
    
    with open("data/users.json", "w", encoding="utf-8") as f:
            json.dump(Users.list_users, f, indent=4, ensure_ascii=False)

# Function to show all users
def show_users():
    df = pd.DataFrame(Users.list_users)
    print(df)
    
    
# Function to modify user first name
def modify_user_fn():
    while True:
        try:
            user_id = int(input("Enter the user ID: "))
            if user_id < 0:
                raise ValueError("The ID must be positive.")
            break
        except ValueError:
            print("No alphabetic characters or symbols")    

    fname = ''
    while len(fname) < 3:
        fname = input("Enter user first name (minimum 3 characters): ")

    decl = False
    for user in Users.list_users:
        if user["id"] == user_id:
            user["first name"] = fname
            decl = True
            print(f"The first name of the user ID {user_id} has been changed with success")
            with open("data/users.json", "w", encoding="utf-8") as f:
                json.dump(Users.list_users, f, indent=4, ensure_ascii=False)
    if not decl:
        print(f"The user ID {user_id} does not exist on the database")
    
            
# Function to modify user last name
def modify_user_ln():
    while True:
        try:
            user_id = int(input("Enter the user ID: "))
            if user_id < 0:
                raise ValueError("The ID must be positive.")
            break
        except ValueError:
            print("No alphabetic characters or symbols") 
    
    lname = ''
    while len(lname) < 3:
        lname = input("Enter user last name (minimum 3 characters): ")

    decl = False
    for user in Users.list_users:
        if user["id"] == user_id:
            user["last name"] = lname
            decl = True
            print(f"The last name of the user ID {user_id} has been changed with success")
            with open("data/users.json", "w", encoding="utf-8") as f:
                json.dump(Users.list_users, f, indent=4, ensure_ascii=False)
    if not decl:
        print(f"The user ID {user_id} does not exist on the database")
            

# Function for sorting users by first name
def sort_fn():
    t = sorted(Users.list_users, key=lambda x: x['first name'])
    df = pd.DataFrame(t)
    print(df)   
    
# Function for sorting users by last name
def sort_ln():
    t = sorted(Users.list_users, key=lambda x: x['last name'])
    df = pd.DataFrame(t)
    print(df)
    
# Function for sorting users by age
def sort_age():
    t = sorted(Users.list_users, key=lambda x: x['age'])
    df = pd.DataFrame(t)
    print(df)   
    
    
# Function to show the users by gender
def show_users_gender():
    gender = ''
    list_gender = []
    while (gender != "M") and (gender != 'F'):
        gender = input("Enter the gender (M or F): ")
    for user in Users.list_users:
        if user["gender"] == gender:
            list_gender.append(user)
    df = pd.DataFrame(list_gender)
    print(df) 
    
# Function to search a user with his first name and last name

def search_user():
    user = ''
    user_fn = input ("Enter the user first name: ")
    user_ln = input ("Enter the user last name: ")
    for u in Users.list_users:
        if user_fn == u["first name"] and user_ln == u["last name"]:
            user = u
            break
    if user == '':
        print(f"The user {user_fn} {user_ln} does not exist on the database")
    else:
        print(user)  