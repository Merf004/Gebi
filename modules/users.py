import json

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
        obj_dict = {"id":self.id, "fist name": self.f_name, "last name": self.l_name, "gender": self.gender}
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