# Substitution Cipher Encryption Program

import random
import string

chars: list[str] = list(" " + string.punctuation + string.digits + string.ascii_letters)
key: list[str] = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

# ENCRYPT
plain_text: str = input("Enter a message to encrypt: ")
cipher_text: str = ""
print()

for letter in plain_text:
    index: int = chars.index(letter)
    cipher_text += key[index]

print(f"Original message : {plain_text}")
print(f"Encrypted Message: {cipher_text}")
print()

# DECRYPT
cypher_text: str = input("Enter a message to decrypt: ")
plain_text_text: str = ""
print()

for letter in cipher_text:
    rev_index: int = key.index(letter)
    plain_text_text += chars[rev_index]

print(f"Encrypted Message: {cipher_text}")
print(f"Original message : {plain_text}")
