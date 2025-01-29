import os
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

def generate_key_from_password(password, salt, iterations=100000, key_length=32):
    """Generates a key from a password using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=key_length,
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

def encrypt_file(input_filename, password, output_filename, salt):
    key = generate_key_from_password(password, salt)
    try:
        with open(input_filename, "rb") as infile:
            plaintext = infile.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return
    except OSError as e:
        print(f"Error reading input file: {e}")
        return

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    ciphertext_with_iv = iv + ciphertext

    try:
        with open(output_filename, "wb") as outfile:
            outfile.write(ciphertext_with_iv)
        print(f"File '{input_filename}' encrypted and saved as '{output_filename}'.")
    except OSError as e:
        print(f"Error writing to output file: {e}")
        return

def decrypt_file(input_filename, password, output_filename, salt):
    key = generate_key_from_password(password, salt)
    try:
        with open(input_filename, "rb") as infile:
            ciphertext_with_iv = infile.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return
    except OSError as e:
        print(f"Error reading input file: {e}")
        return

    iv = ciphertext_with_iv[:16]
    ciphertext = ciphertext_with_iv[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    try:
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    except ValueError:
        print("Decryption error: Invalid padding. Incorrect password?")
        return

    try:
        with open(output_filename, "wb") as outfile:
            outfile.write(plaintext)
        print(f"File '{input_filename}' decrypted and saved as '{output_filename}'.")
    except OSError as e:
        print(f"Error writing to output file: {e}")
        return

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python crypto.py <encrypt/decrypt> <input_file> <password> <output_file> <salt>")
        sys.exit(1)

    operation = sys.argv[1].lower()
    input_file = sys.argv[2]
    password = sys.argv[3]
    output_file = sys.argv[4]
    salt = sys.argv[5].encode() # Salt should be bytes

    if operation == "encrypt":
        encrypt_file(input_file, password, output_file, salt)
    elif operation == "decrypt":
        decrypt_file(input_file, password, output_file, salt)
    else:
        print("Invalid operation. Use 'encrypt' or 'decrypt'.")
