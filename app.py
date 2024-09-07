
from datetime import date, datetime
from modules.books import *
from modules.transactions import *
from modules.users import *

import pandas as pd
import json

with open('data/books.json', 'r', encoding='utf-8') as f:
    Books.list_books = json.load(f)
with open('data/users.json', 'r', encoding='utf-8') as f:
    Users.list_users = json.load(f)
    
Books.b = len(Books.list_books) + 1
Users.u = len(Users.list_users) + 1

add_user()
add_book()
 