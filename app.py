
from datetime import date, datetime
from modules.books import *
from modules.transactions import *
from modules.users import *

import pandas as pd
import json

with open('data/books.json', 'r', encoding='utf-8') as f:
    Books.list_books = json.load(f)

modify_isbn(1)