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

#save_todos(data)

def add_expense():
    while True:
        user_input = input("Dollar Amount ($XX.XX): ").strip()

        # Optional: allow "$12.34" by stripping $ and spaces
        cleaned = user_input.strip(" $")

        try:
            money_spent = float(cleaned)
        except ValueError:
            print("Need a number amount (example: 12.50)")
            continue

        if money_spent < 0:
            print("Amount cannot be negative")
            continue
        
        print(f"${money_spent} added to your expense tracker!")
        print()
        break
        


def quit_program():
    print("Goodbye!")

actions = {
    "1": add_expense

}

def main():
    while True:
        print(
            "== Expense Tracker ==\n"
            "1. Add an expense\n"
            "2. View all expenses\n"
            "3. View summary by categorye\n"
            "4. Filter expenses by month\n"
            "5. Delete an expense\n"
            "6. Quit\n")
        user_input = input("Choose: ").strip().lower()

        if user_input == "6":
            quit_program()
            break
        
        action = actions.get(user_input)
        if action is None:
            print("Invalid Response. Try again...")
            print()
            continue
        else:
            action()
            print()

if __name__ == "__main__":
    main()