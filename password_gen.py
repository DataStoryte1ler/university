import os
import sys
import argparse
import secrets
from cryptography.fernet import Fernet

def generate_password(length):
    # Generates a random password of the specified length
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def encrypt_password(password, key):
    # Encrypts the password using AES-256 encryption
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def save_password(encrypted_password, filename):
    # Saves the encrypted password to a file
    with open(filename, 'wb') as file:
        file.write(encrypted_password)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate and encrypt a random password')
    parser.add_argument('-l', '--length', type=int, default=16, help='Length of the password')
    parser.add_argument('-k', '--keyfile', type=str, required=True, help='File containing encryption key')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output filename')
    args = parser.parse_args()

    # Generates an encryption key and saves it into the file
    key = Fernet.generate_key()
    with open('key.txt', 'wb') as file:
        file.write(key)
    # Read an encryption key from file
    with open(args.keyfile, 'rb') as file:
        key = file.read()

    # Generate a random password and encrypt it
    password = generate_password(args.length)
    encrypted_password = encrypt_password(password, key)

    # Save the encrypted password to a file
    save_password(encrypted_password, args.output)

    # Print the password to the console
    print('Generated password:', password)

if __name__ == '__main__':
    main()
