import hashlib
import getpass
import sys

PASSWORD_FILE = "password.txt"
MASTER_PASSWORD_FILE = "master_hash.txt"

credentials = []


def create_master_password():
    with open(MASTER_PASSWORD_FILE, 'r') as file:
        content = file.read()
        if content == "":
            create_master_input = getpass.getpass("Create Master Password: ", echo_char="*")
            hashed = hashlib.sha256(create_master_input.encode()).hexdigest()
            with open(MASTER_PASSWORD_FILE, "w") as file:
                file.write(hashed)
        else:
            return

def master_password():
    master_input = getpass.getpass("Master Password: ", echo_char="*")
    user_hash = hashlib.sha256(master_input.encode()).hexdigest()
    
    with open(MASTER_PASSWORD_FILE, 'r') as file:
        stored_hash = file.read().strip()
        if user_hash == stored_hash:
            print("Access Granted!")
            print()
            return True
        else:
            print("Access not granted...")
            quit_program()
            sys.exit()
            

def save_credential(cred):
    line = f"{cred["site"]}:{cred["username"]}:{cred["password"]}\n"
    with open(PASSWORD_FILE, "a") as file:
        file.write(line)

def add_credential(): #Gets the site, username, and password. It then takes those inputs and stores them in a dictionary and adds them to our credentials dictionary so that we can use them later on
    site = input("What is the name of your site you wish to save to the password manager?: ").strip() 
    #The .strip() removes any unwanted spaces so that in function view credentials it can read whether the user inputed values or not and 
    # if there are no values then the function prints No credentials added
    username = input("What is your saved username on that site?: ").strip()
    password = getpass.getpass("What is your saved password on that site?: ", echo_char="*").strip() 

    if site == "":
        print("Site name required. Info not saved.")
        return 
    
    login_details = {"site": site, "username": username, "password": password}
    credentials.append(login_details)
    save_credential(login_details)

#add_credential()
#print(credentials)

def view_credentials(): #Function to let the user see the credentials. If there are none, then print basic response. If there are, it starts at 1 and prints the site and username. 
    if credentials == []:
        print("No credentials added yet")
    else:
        num = 1
        for login_details in credentials:
            print(f"{num}. {login_details["site"]} - username: {login_details["username"]}")
            num += 1

#view_credentials()

def search_credentials():
    search = input("Enter the site name to search: ")
    for login_details in credentials: #FOR HERE ADD A FEATURE LATER THAT ALLOWS ME TO UNCASESENSITIVE WORDING SO THAT IF I SEARCH UP "NET", IT SHOWS ALL THE SITES NAMES WITH NET IN IT.
        if login_details["site"] == search:
            print(f"{login_details["site"]} - username: {login_details["username"]}")
        elif login_details["site"] == "":
            print("No credentials found for that site")

#search_credentials()

def load_credentials():
    try:
        with open(PASSWORD_FILE, "r") as file:
            for line in file:
                cleaned = line.strip()
                seperated = cleaned.split(":")
                if len(seperated) == 3:
                    cred = {"site": seperated[0], "username": seperated[1], "password": seperated[2]}
                    credentials.append(cred)
    except FileNotFoundError:
        pass


def quit_program():
    print("Goodbye!")

actions = {
    "1": add_credential,
    "2": view_credentials,
    "3": search_credentials,
    "4": quit_program,
}

def main():
    load_credentials()

    create_master_password()
    master_password()

    while True:
        print(
            "== Password Manager ==\n"
            "1. Add credentials\n"
            "2. View alll\n"
            "3. Search by site\n"
            "4. Quit\n")
        user_input = input("Choose: ")

        if user_input == "4":
            quit_program()
            break

        action = actions.get(user_input)

        if action is None:
            print("Invalid option. Please try again")
        else:
            action()
            print()
        
if __name__ == "__main__":
    main()