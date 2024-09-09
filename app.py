
from datetime import date, datetime
from modules.books import *
from modules.transactions import *
from modules.users import *
from modules.menu import *

import pandas as pd
import json

with open('data/books.json', 'r', encoding='utf-8') as f:
    Books.list_books = json.load(f)
with open('data/users.json', 'r', encoding='utf-8') as f:
    Users.list_users = json.load(f)
with open('data/transactions.json', 'r', encoding='utf-8') as f:
    Transactions.list_transactions = json.load(f)

if Books.list_books == []:
    Books.b = 1
else:
    Books.b = Books.list_books[-1]["id"] + 1
    
if Users.list_users == []:
    Users.u = 1
else:
    Users.u = Users.list_users[-1]["id"] + 1
    
if Transactions.list_transactions == []:
    Transactions.t = 1
else:
    Transactions.t = Transactions.list_transactions[-1]["id"] + 1


print("_______________________________________GeMi________________________________________")
main_menu()