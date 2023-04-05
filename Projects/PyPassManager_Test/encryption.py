from cryptography.fernet import Fernet
from program_modes import exit_program
import colorama
import os
import re
import pwinput

# function to generate encryption key


def write_key():
    # check if key file exists
    key_file_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "key.key")
    if not os.path.exists(key_file_path):
        # generate key
        key = Fernet.generate_key()
        # write key to file
        with open(key_file_path, "wb") as key_file:
            key_file.write(key)
            print(
                f"{colorama.Fore.GREEN}Key generated.{colorama.Style.RESET_ALL}")
    else:
        print(
            f"\n{colorama.Fore.GREEN}Key already exists.{colorama.Style.RESET_ALL}")


# function to load encryption key from file
def load_key():
    key_file_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "key.key")
    return open(key_file_path, "rb").read()


# function to set the master password
def set_master_password(fernet):
    password_file_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "master_password.txt")

    while True:
        # get user input for password
        password = pwinput.pwinput(
            f"{colorama.Fore.YELLOW}Set the master password (at least 8 characters, one uppercase letter, one lowercase letter, one number, and one special character):{colorama.Style.RESET_ALL}\n> ")
        # check if password meets requirements
        if len(password) < 8:
            print("\nPassword must be at least 8 characters long.\n")
        elif not re.search(r'[A-Z]', password):
            print("\nPassword must contain at least one uppercase letter.\n")
        elif not re.search(r'[a-z]', password):
            print("\nPassword must contain at least one lowercase letter.\n")
        elif not re.search(r'[0-9]', password):
            print("\nPassword must contain at least one number.\n")
        elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print("\nPassword must contain at least one special character.\n")
        else:
            # encrypt password using Fernet object and write to file
            encrypted_password = fernet.encrypt(password.encode()).decode()
            with open(password_file_path, 'w') as f:
                f.write(encrypted_password)
            break


# function to check if master password is correct
def check_master_password(fernet, max_tries=3):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "master_password.txt"), "r") as f:
        encrypted_password = f.read()

    for i in range(max_tries):
        # decrypt stored password and check if input password matches
        decrypted_password = fernet.decrypt(
            encrypted_password.encode()).decode()
        # get user input for password
        input_password = pwinput.pwinput(
            f"{colorama.Fore.YELLOW}\nEnter the master password to access PyPassManager (type 'exit' to quit program)\n(Attempt {i+1} of {max_tries}):{colorama.Style.RESET_ALL}\n> ")

        # exit program if user types 'exit'
        if input_password == "exit":
            exit_program()

        if input_password == decrypted_password:
            return True
        else:
            print(
                f"{colorama.Fore.RED}{colorama.Style.BRIGHT}\nIncorrect master password. Please try again.{colorama.Style.RESET_ALL}")

    # exit program if maximum number of tries is reached
    print(f"\n{colorama.Fore.RED}{colorama.Style.BRIGHT}Max number of tries ({max_tries}) reached. Exiting program.{colorama.Style.RESET_ALL}")
    exit_program()
