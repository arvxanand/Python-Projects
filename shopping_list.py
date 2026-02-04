shopping_list = []

def add_item():
    item_choice = input("Add items seperated by commas: ")
    for item in item_choice.split(","): #["Milk, Eggs, Pasta"] 
        cleaned = item.strip() # Here it is stripping the empty spaces so it goes from " Eggs" to "Eggs"
        if cleaned:
            shopping_list.append(cleaned)

def remove_item():
    remove_item = input("What item would you like to remove from the list?: ")
    return shopping_list.remove(remove_item)

def view_list():
    print(shopping_list)

def quit_program():
    print("Goodbye")

actions = {
    "1": add_item,
    "2": remove_item,
    "3": view_list,
    "4": quit_program,
}

def main():
    while True:
        print(
            "1. Add item\n"
            "2. Remove item\n"
            "3. View list\n"
            "4. Quit")
        user_input = input("Which option would you like to choose: ")
        #print(user_input)

        if user_input == "4":
            quit_program()
            break

        action = actions.get(user_input)
        #print(action)
    

        if action is None:
            print("Invalid option. Please try again")
        else:
            action()
            print()


if __name__ == "__main__":
    main()