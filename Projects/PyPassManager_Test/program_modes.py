from tabulate import tabulate
import colorama
import os
import re

# Define a function to view passwords


def view_passwords(fernet):
    print(f"{colorama.Fore.GREEN}\nViewing passwords...{colorama.Style.RESET_ALL}\n")
    try:
        # Open the encrypted passwords file and read each line
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'passwords.encrypted'), 'r') as f:
            table_data = [['Website', 'Username', 'Password']]
            for line in f.readlines():
                # Split the line into the website, username, and password
                data = (line.rstrip())
                website, user, password = data.split('|')
                # Decrypt the password and add the website, username, and decrypted password to the table data
                decrypted_password = fernet.decrypt(password.encode()).decode()
                table_data.append([website, user, decrypted_password])
            # Output the table
            print(tabulate(table_data, headers='firstrow', tablefmt='psql'))

    except FileNotFoundError:
        print(f"{colorama.Fore.RED}No passwords found. Please create a password using the 'add' command.{colorama.Style.RESET_ALL}")


# Define a function to add a password
def add_password(fernet):
    # Prompt the user for a new website, username, and password
    website = input("\nEnter the website (type 'cancel' to quit):\n> ")
    if website == "cancel":
        print(f"{colorama.Fore.RED}Canceled adding password.{colorama.Style.RESET_ALL}")
        return
    username = input("\nEnter the username (type 'cancel' to quit):\n> ")
    if username == "cancel":
        print(f"{colorama.Fore.RED}Canceled adding password.{colorama.Style.RESET_ALL}")
        return
    password = input("\nEnter the password (type 'cancel' to quit):\n> ")
    if password == "cancel":
        print(f"{colorama.Fore.RED}Canceled adding password.{colorama.Style.RESET_ALL}")
        return

    # Encrypt the password and append the new username and encrypted password to the passwords file
    encrypted_password = fernet.encrypt(password.encode()).decode()

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'passwords.encrypted'), 'a') as f:
        f.write(f"{website} | {username} | {encrypted_password}\n")

    print(f"\n{colorama.Fore.GREEN}Password added.{colorama.Style.RESET_ALL}")


# Define a function to edit a password
def edit_password(fernet):
    try:
        # Prompt the user for the website of the password they want to edit
        website = input(
            "\nEnter the website for the password you want to edit:\n> ").strip()

        # Open the encrypted password file for reading
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'passwords.encrypted'), 'r') as f:
            lines = f.readlines()

        found = False
        # Find the line corresponding to the website and replace it with a new encrypted password
        for i, line in enumerate(lines):
            data = line.rstrip().split('|')
            if re.sub(r'\s', '', data[0].lower()) == re.sub(r'\s', '', website.lower()):
                found = True
                # Prompt the user for the new password and encrypt it
                new_password = input("\nEnter the new password:\n> ")
                encrypted_password = fernet.encrypt(
                    new_password.encode()).decode()
                # Replace the old password with the new encrypted password in the file
                lines[i] = f"{data[0]} | {data[1]} | {encrypted_password}\n"
                with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'passwords.encrypted'), 'w') as f:
                    f.write(''.join(lines))
                print(
                    f"{colorama.Fore.GREEN}Password edited successfully.{colorama.Style.RESET_ALL}")
                break

        if not found:
            print(
                f"{colorama.Fore.RED}No password found for that website.{colorama.Style.RESET_ALL}")

    except FileNotFoundError:
        print(f"{colorama.Fore.RED}No passwords found. Please create a password using the 'add' command.{colorama.Style.RESET_ALL}")


# Define a function to delete a password
def delete_password(fernet):
    try:
        # Prompt the user for the website of the password they want to delete
        website = input(
            "\nEnter the website for the password you want to delete:\n> ").strip()

        # Get the full path to the passwords file
        passwords_file = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'passwords.encrypted')

        # Open the encrypted password file for reading
        with open(passwords_file, 'r') as f:
            lines = f.readlines()

        found = False
        # Find the line corresponding to the website and delete it
        for i, line in enumerate(lines):
            data = line.rstrip().split('|')
            if re.sub(r'\s', '', data[0].lower()) == re.sub(r'\s', '', website.lower()):
                found = True
                del lines[i]
                # Write the updated password file without the deleted line
                with open(passwords_file, 'w') as f:
                    f.write(''.join(lines))
                print(
                    f"{colorama.Fore.GREEN}Password deleted successfully.{colorama.Style.RESET_ALL}")
                break

        if not found:
            print(
                f"{colorama.Fore.RED}No password found for that website.{colorama.Style.RESET_ALL}")

    except FileNotFoundError:
        print(f"{colorama.Fore.RED}No passwords found. Please create a password using the 'add' command.{colorama.Style.RESET_ALL}")


# Function to exit the program
def exit_program():
    print(f"{colorama.Fore.GREEN}\nExiting the program...{colorama.Style.RESET_ALL}")
    exit()
