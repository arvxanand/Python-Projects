import json 
import datetime as dt
import os

EXPENSES_JSON = "expenses.json"

def load_todos():
    if not os.path.exists(EXPENSES_JSON):
        return []
    try:
        with open(EXPENSES_JSON, "r") as file:
            return json.load(file)
    except ValueError:
        return []

data = {"name": "Alice", "age": 30}

def save_todos(data):
    with open(EXPENSES_JSON, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

