import hashlib
import getpass

PASSWORD_FILE = "password.txt"

credentials = []

def add_credential(): #Gets the site, username, and password. It then takes those inputs and stores them in a dictionary and adds them to our credentials dictionary so that we can use them later on
    site = input("What is the name of your site you wish to save to the password manager?: ")
    username = input("What is your saved username on that site?: ")
    password = input("What is your saved password on that site?: ")
    login_details = {"site": site, "username": username, "password": password}
    credentials.append(login_details)

add_credential()
print(credentials)

def view_credentials(): #Function to let the user see the credentials. If there are none, then print basic response. If there are, it starts at 1 and prints the site and username. 
    if credentials == []:
        print("No credentials added yet")
    else:
        num = 1
        for login_details in credentials:
            print(f"{num}. {login_details["site"]} - username: {login_details["username"]}")
            num += 1

view_credentials()

def search_credentials():
    pass

def load_credentials():
    pass

def save_credential():
    pass

def quit_program():
    print("Goodbye!")

actions = {
    "1": add_credential,
    "2": view_credentials,
    "3": search_credentials,
    "4": quit_program,
}

#def main():
    