# Password Manager

This is a Python script for a basic password manager that encrypts passwords using the Fernet module from the Cryptography package. The script generates a key file and a master password file that are used to encrypt and decrypt passwords. The key file is stored locally in the directory with the script, while the master password file is used to authenticate access to the passwords.

## Requirements

Python 3.6 or higher
Cryptography package (pip install cryptography)

## How to Use

1. Run the script in a Python environment.
2. When prompted, set a master password to access the password manager.
3. Choose between viewing passwords, adding a new password, or exiting the program.
   - To view passwords, enter 'view' and the stored usernames and passwords will be decrypted and printed to the console.
   - To add a new password, enter 'add' and input the username and password when prompted. The password will be encrypted and stored in a file.
   - To exit the program, enter 'exit' at any time.

Note: The script will generate a key file called "key.key" and a master password file called "master_password.txt" in the same directory as the script. Do not delete or modify these files or else the stored passwords will not be accessible.

# Disclaimer

This is a basic script for educational purposes only. It is not recommended for storing sensitive passwords and should not be used for real-world password management.
