import colorama
import os
from cryptography.fernet import Fernet
from encryption import write_key, load_key, set_master_password, check_master_password
from program_modes import add_password, view_passwords, edit_password, delete_password, exit_program


def main():
    # Generate the encryption key if it doesn't already exist
    write_key()

    # Load the key from the key file
    key = load_key()

    # Create the Fernet object using the key
    fernet = Fernet(key)

    # Check if passwords.encrypted file exists
    password_file_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "master_password.txt")
    passwords_encrypted_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'passwords.encrypted')

    try:
        if os.path.exists(passwords_encrypted_file_path) and not os.path.exists(password_file_path):
            os.remove(passwords_encrypted_file_path)
            print(f"\n{colorama.Fore.RED}{colorama.Style.BRIGHT}Master password file not found. Deleting existing passwords file...{colorama.Style.RESET_ALL}\n")

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'master_password.txt')):
            # if master password file doesn't exist, prompt user to set one
            set_master_password(fernet)

    except FileNotFoundError:
        os.remove(passwords_encrypted_file_path)
        print(f"\n{colorama.Fore.RED}{colorama.Style.BRIGHT}Master password file not found. Deleting existing passwords file...{colorama.Style.RESET_ALL}\n")
        set_master_password(fernet)

    # Flag to keep track of whether the user has entered the correct master password
    password_entered = False

    while True:
        if not password_entered:
            # Check the master password
            if check_master_password(fernet):
                password_entered = True
            else:
                print(
                    f"{colorama.Fore.RED}{colorama.Style.BRIGHT}Incorrect master password. Please try again.{colorama.Style.RESET_ALL}")
                continue

        # Prompt the user for the program mode
        program_mode = input(
            f"{colorama.Fore.BLUE}{colorama.Style.BRIGHT}\nEnter... \n- 'view' to view passwords.\n- 'add' to add a password.\n- 'edit' to edit a password.\n- 'delete' to delete a password.\n- 'exit' to quit.{colorama.Style.RESET_ALL}\n> ").lower()

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
                f"\n{colorama.Fore.RED}{colorama.Style.BRIGHT}Invalid input. Please try again.{colorama.Style.RESET_ALL}")


if __name__ == "__main__":
    main()
