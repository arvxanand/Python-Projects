#!/usr/bin/env python3
import json
import os
import argparse
from datetime import datetime as dt

JSON_TODO = "todo.json"

def load_todos():
    if not os.path.exists(JSON_TODO):
        return []
    try:
        with open(JSON_TODO, "r") as file:
            return json.load(file)
    except ValueError:
        return []

def save_todos(todos):
    with open(JSON_TODO, "w") as file:
        json.dump(todos, file, indent=2)

def next_id(todos): #returning the next avaliabe id spot to be taken
    if not todos:
        return 1
    else:
        return max(todo["id"] for todo in todos) + 1
