import json

class Transactions:
    list_transactions = []
    t = 1
    
    def __init__(self, date_b, date_r, user, book) -> None:
        self.id = Transactions.t
        self.date_b = date_b
        self.date_r = date_r
        self.user = user
        self.book = book
        
        Transactions.t += 1
        obj_dict = {"id":self.id, "date borrowed": str(self.date_b), "date returned": str(self.date_r), "user": self.user.to_dict(), "book": self.book.to_dict()}
        Transactions.list_transactions.append(obj_dict)
        
        with open("data/transactions.json", "w", encoding="utf-8") as f:
            json.dump(Transactions.list_transactions, f, indent=4, ensure_ascii=False) 
