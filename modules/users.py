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
    
# Function to delete a book 
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
    
    
# Function to modify book title
def modify_user_fn(user_id):
    fname = ''
    while len(fname) < 3:
        fname = input("Enter user first name (minimum 3 characters): ")
    Users.list_users[user_id - 1]["first name"] = fname
    print(f"The first name of the user ID {user_id} has been changed with success")
    
    with open("data/users.json", "w", encoding="utf-8") as f:
            json.dump(Users.list_users, f, indent=4, ensure_ascii=False)
            
# Function to modify book title
def modify_user_ln(user_id):
    lname = ''
    while len(lname) < 3:
        lname = input("Enter user last name (minimum 3 characters): ")
    Users.list_users[user_id - 1]["last name"] = lname
    print(f"The last name of the user ID {user_id} has been changed with success")
    
    with open("data/users.json", "w", encoding="utf-8") as f:
            json.dump(Users.list_users, f, indent=4, ensure_ascii=False)
            

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