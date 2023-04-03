from cryptography.fernet import Fernet
import os


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


def main():
    # Generate the encryption key if it doesn't already exist
    write_key()

    # Load the key from the key file
    key = load_key()

    # Create the Fernet object using the key
    fernet = Fernet(key)

    while True:
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


def view_passwords(fernet):
    print("Viewing passwords...\n")
    # Code to view passwords goes here
    with open('passwords.txt', 'r') as f:
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

    with open('passwords.txt', 'a') as f:
        f.write(f"{username} | {encrypted_password}\n")

    print("Adding a password...")


def exit_program():
    # Code to exit the program goes here
    print("Exiting the program...")
    exit()


if __name__ == "__main__":
    main()
