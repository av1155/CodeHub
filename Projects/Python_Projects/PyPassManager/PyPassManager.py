from cryptography.fernet import Fernet
import os
import re
import colorama
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
                f"{colorama.Fore.GREEN}{colorama.Style.BRIGHT}Key generated.{colorama.Style.RESET_ALL}")
    else:
        print("Key already exists.")

# function to load encryption key from file


def load_key():
    key_file_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "key.key")
    return open(key_file_path, "rb").read()

# function to set the master password


def set_master_password(fernet):
    while True:
        # get user input for password
        password = input(
            "Set the master password (at least 8 characters, one uppercase letter, one lowercase letter, one number, and one special character):\n> ")
        # check if password meets requirements
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
        elif not re.search(r'[A-Z]', password):
            print("Password must contain at least one uppercase letter.")
        elif not re.search(r'[a-z]', password):
            print("Password must contain at least one lowercase letter.")
        elif not re.search(r'[0-9]', password):
            print("Password must contain at least one number.")
        elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print("Password must contain at least one special character.")
        else:
            # encrypt password using Fernet object and write to file
            encrypted_password = fernet.encrypt(password.encode()).decode()
            password_file_path = os.path.join(os.path.dirname(
                os.path.abspath(__file__)), "master_password.txt")
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
        input_password = input(
            f"\nEnter the master password to access PyPassManager (type 'exit' to quit) (Attempt {i+1} of {max_tries}):\n> ")

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

# Define a function to handle the main program logic


def main():
    # Generate the encryption key if it doesn't already exist
    write_key()

    # Load the key from the key file
    key = load_key()

    # Create the Fernet object using the key
    fernet = Fernet(key)

    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'master_password.txt')):
        # if master password file doesn't exist, prompt user to set one
        set_master_password(fernet)

    while True:
        if check_master_password(fernet):
            # Prompt the user for the program mode
            program_mode = input(
                f"{colorama.Fore.BLUE}\nEnter... \n- 'view' to view passwords.\n- 'add' to add a password.\n- 'edit' to edit a password.\n- 'delete' to delete a password.\n- 'exit' to quit.{colorama.Style.RESET_ALL}\n> ").lower()

            # Determine which mode the user has selected and call the appropriate function
            if program_mode == "view":
                view_passwords(fernet)

            elif program_mode == "add":
                add_password(fernet)

            elif program_mode == "edit":
                edit_password(fernet)

            elif program_mode == "delete":
                delete_password(fernet)

            elif program_mode == "exit":
                exit_program()

            else:
                print(
                    f"{colorama.Fore.RED}{colorama.Style.BRIGHT}Invalid input. Please try again.{colorama.Style.RESET_ALL}")

        # If the user enters the wrong master password, prompt them to try again
        else:
            print(f"{colorama.Fore.RED}{colorama.Style.BRIGHT}Incorrect master password. Please try again.{colorama.Style.RESET_ALL}")

# Define a function to view passwords


def view_passwords(fernet):
    print("\nViewing passwords...")
    try:
        # Open the encrypted passwords file and read each line
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'passwords.encrypted'), 'r') as f:
            for line in f.readlines():
                # Split the line into the username and password
                data = (line.rstrip())
                user, password = data.split('|')
                # Decrypt the password and print the username and decrypted password
                decrypted_password = fernet.decrypt(password.encode()).decode()
                print(f"User: {user}| Password: {decrypted_password}")
    except FileNotFoundError:
        print("No passwords found. Please create a password using the 'add' command.")

# Define a function to add a password


def add_password(fernet):
    # Prompt the user for a new username and password
    username = input("\nEnter the username (type 'cancel' to quit):\n> ")
    if username == "cancel":
        print("Canceled adding password.")
        return
    password = input("Enter the password (type 'cancel' to quit):\n> ")
    if password == "cancel":
        print("Canceled adding password.")
        return

    # Encrypt the password and append the new username and encrypted password to the passwords file
    encrypted_password = fernet.encrypt(password.encode()).decode()

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'passwords.encrypted'), 'a') as f:
        f.write(f"{username} | {encrypted_password}\n")

    print("Password added.")

# Define a function to edit a password


def edit_password(fernet):
    try:
        # Prompt the user for the username of the password they want to edit
        username = input(
            "\nEnter the username for the password you want to edit:\n> ").strip()

        # Open the encrypted password file for reading
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'passwords.encrypted'), 'r') as f:
            lines = f.readlines()

        found = False
        # Find the line corresponding to the username and replace it with a new encrypted password
        for i, line in enumerate(lines):
            data = line.rstrip().split('|')
            if re.sub(r'\s', '', data[0].lower()) == re.sub(r'\s', '', username.lower()):
                found = True
                # Prompt the user for the new password and encrypt it
                new_password = input("Enter the new password:\n> ")
                encrypted_password = fernet.encrypt(
                    new_password.encode()).decode()
                # Replace the old password with the new encrypted password in the file
                lines[i] = f"{data[0]} | {encrypted_password}\n"
                with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'passwords.encrypted'), 'w') as f:
                    f.write(''.join(lines))
                print("Password edited successfully.")
                break

        if not found:
            print("No password found for that username.")

    except FileNotFoundError:
        print("No passwords found. Please create a password using the 'add' command.")

# Define a function to delete a password


def delete_password(fernet):
    try:
        # Prompt the user for the username of the password they want to delete
        username = input(
            "\nEnter the username for the password you want to delete:\n> ").strip()

        # Get the full path to the passwords file
        passwords_file = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'passwords.encrypted')

        # Open the encrypted password file for reading
        with open(passwords_file, 'r') as f:
            lines = f.readlines()

        found = False
        # Find the line corresponding to the username and delete it
        for i, line in enumerate(lines):
            data = line.rstrip().split('|')
            if re.sub(r'\s', '', data[0].lower()) == re.sub(r'\s', '', username.lower()):
                found = True
                del lines[i]
                # Write the updated password file without the deleted line
                with open(passwords_file, 'w') as f:
                    f.write(''.join(lines))
                print("Password deleted successfully.")
                break

        if not found:
            print("No password found for that username.")

    except FileNotFoundError:
        print("No passwords found. Please create a password using the 'add' command.")

# Function to exit the program


def exit_program():
    print("\nExiting the program...")
    exit()


# Check if this script is being run as the main program
if __name__ == "__main__":
    # Call the main function to start the program
    main()
