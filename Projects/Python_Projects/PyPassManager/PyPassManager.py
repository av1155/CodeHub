from cryptography.fernet import Fernet
import os
import re


def write_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
            print("Key generated.")
    else:
        print("Key already exists.")


def load_key():
    return open("key.key", "rb").read()


def set_master_password(fernet):
    while True:
        password = input(
            "Set the master password (at least 8 characters, one uppercase letter, one lowercase letter, one number, and one special character): ")
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
            encrypted_password = fernet.encrypt(password.encode()).decode()
            with open('master_password.txt', 'w') as f:
                f.write(encrypted_password)
            break


def check_master_password(fernet):
    with open('master_password.txt', 'r') as f:
        encrypted_password = f.read()

    decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
    input_password = input(
        "\nEnter the master password to view passwords (type 'exit' to quit):\n> ")

    if input_password == "exit":
        exit_program()

    return input_password == decrypted_password


def main():
    # Generate the encryption key if it doesn't already exist
    write_key()

    # Load the key from the key file
    key = load_key()

    # Create the Fernet object using the key
    fernet = Fernet(key)

    if not os.path.exists('master_password.txt'):
        set_master_password(fernet)

    while True:
        if check_master_password(fernet):
            program_mode = input(
                "\nEnter 'view' to view passwords, 'add' to add a password, or 'exit' to quit:\n> ").lower()

            if program_mode == "view":
                view_passwords(fernet)

            elif program_mode == "add":
                add_password(fernet)

            elif program_mode == "exit":
                exit_program()

            else:
                print("Invalid input. Please try again.")
        else:
            print("Incorrect master password. Please try again.")


def view_passwords(fernet):
    print("Viewing passwords...\n")
    # Code to view passwords goes here
    with open('passwords.encrypted', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, password = data.split('|')
            decrypted_password = fernet.decrypt(password.encode()).decode()
            print(f"User: {user}| Password: {decrypted_password}")


def add_password(fernet):
    # Code to add a password goes here
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    encrypted_password = fernet.encrypt(password.encode()).decode()

    with open('passwords.encrypted', 'a') as f:
        f.write(f"{username} | {encrypted_password}\n")

    print("Adding a password...")


def exit_program():
    # Code to exit the program goes here
    print("Exiting the program...")
    exit()


if __name__ == "__main__":
    main()
