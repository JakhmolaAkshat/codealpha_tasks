import os
import subprocess
import pickle
import hashlib
import getpass

def insecure_password_storage(password):
    """Stores password in an insecure way (MD5 is weak)"""
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    with open("passwords.txt", "a") as f:
        f.write(hashed_password + "\n")
    print("Password stored insecurely!")

def command_injection():
    """Takes user input and executes it without validation"""
    user_input = input("Enter a command: ")
    os.system(user_input)  # Vulnerable to command injection

def unsafe_deserialization():
    """Loads a pickle file without validation (can execute arbitrary code)"""
    with open("data.pkl", "rb") as f:
        data = pickle.load(f)  # Vulnerable to arbitrary code execution
    print("Data loaded:", data)

def hardcoded_secret():
    """Contains a hardcoded secret key"""
    secret_key = "12345-abcdef-67890"  # Hardcoded secret
    print("Using secret key:", secret_key)

def weak_authentication():
    """Uses plaintext password checking (no hashing, no security)"""
    password = getpass.getpass("Enter password: ")
    if password == "admin123":  # Hardcoded weak password
        print("Access Granted!")
    else:
        print("Access Denied!")

if __name__ == "__main__":
    print("[1] Insecure Password Storage")
    print("[2] Command Injection")
    print("[3] Unsafe Deserialization")
    print("[4] Hardcoded Secret Key")
    print("[5] Weak Authentication")
    
    choice = input("Choose a vulnerability to test: ")
    
    if choice == "1":
        insecure_password_storage(input("Enter password to store: "))
    elif choice == "2":
        command_injection()
    elif choice == "3":
        unsafe_deserialization()
    elif choice == "4":
        hardcoded_secret()
    elif choice == "5":
        weak_authentication()
    else:
        print("Invalid choice!")
