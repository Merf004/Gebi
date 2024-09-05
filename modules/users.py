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
        with open("data/users.json", "w", encoding="utf-8") as f:
            json.dump(Users.list_users, f, indent=4, ensure_ascii=False)   

    def to_dict(self):
        return {"id":self.id, "fist name": self.f_name, "last name": self.l_name, "gender": self.gender}
