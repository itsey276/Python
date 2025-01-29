import os
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def generate_key(key_filename, key_length=32):
    """Generates a random key and saves it to a file.

    Args:
        key_filename: The name of the file to save the key to.
        key_length: The length of the key in bytes (default: 32 for AES-256).
    """
    try:
        if os.path.exists(key_filename):
            overwrite = input(f"File '{key_filename}' already exists. Overwrite? (y/n): ")
            if overwrite.lower() != 'y':
                print("Key generation aborted.")
                return

        key = os.urandom(key_length)
        with open(key_filename, "wb") as key_file:
            key_file.write(key)
        print(f"Key generated and saved to '{key_filename}'.")
    except OSError as e:
        print(f"Error writing key to file: {e}")

def encrypt_file(input_filename, key_filename, output_filename):
    try:
        with open(key_filename, "rb") as key_file:
            key = key_file.read()
            if len(key) != 32:
                raise ValueError("Key must be 32 bytes (256 bits).")
    except FileNotFoundError:
        print(f"Error: Key file '{key_filename}' not found.")
        return
    except ValueError as e:
        print(f"Error: {e}")
        return
    except OSError as e:
        print(f"Error reading key file: {e}")
        return

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

def decrypt_file(input_filename, key_filename, output_filename):
    try:
        with open(key_filename, "rb") as key_file:
            key = key_file.read()
            if len(key) != 32:
                raise ValueError("Key must be 32 bytes (256 bits).")
    except FileNotFoundError:
        print(f"Error: Key file '{key_filename}' not found.")
        return
    except ValueError as e:
        print(f"Error: {e}")
        return
    except OSError as e:
        print(f"Error reading key file: {e}")
        return

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
        print("Decryption error: Invalid padding. Incorrect key?")
        return

    try:
        with open(output_filename, "wb") as outfile:
            outfile.write(plaintext)
        print(f"File '{input_filename}' decrypted and saved as '{output_filename}'.")
    except OSError as e:
        print(f"Error writing to output file: {e}")
        return

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python crypto.py <encrypt/decrypt/generate> [<input_file>] <key_file> [<output_file>]")
        sys.exit(1)

    operation = sys.argv[1].lower()
    if operation == "generate":
        key_file = sys.argv[2]
    else:
        input_file = sys.argv[2]
        key_file = sys.argv[3]
        output_file = sys.argv[4] if len(sys.argv) > 4 else "output.bin" # Default output file

    if operation == "encrypt":
        encrypt_file(input_file, key_file, output_file)
    elif operation == "decrypt":
        decrypt_file(input_file, key_file, output_file)
    elif operation == "generate":
        generate_key(key_file)
    else:
        print("Invalid operation. Use 'encrypt' or 'decrypt' or 'generate'.")