#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation
#Author: Srikanth Dabbiru
#Implement a substitution cipher (random key) taking the message as the input
import random

def keygen():
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    calpha = list(alphabets)
    cAlpha = list(Alphabets)
    key = {}
    for char in alphabets:
        key[char] = calpha.pop(random.randint(0, len(calpha) - 1)) 
    for char in Alphabets:
        key[char] = cAlpha.pop(random.randint(0, len(cAlpha) - 1)) 
    return key

def encrypt(cipherkey, plaintext):
    encryptedtext = ""
    for i in plaintext:
       if i in cipherkey:
        encryptedtext += cipherkey[i]
       else:    #Keep unknown chars from keygen as-is
        encryptedtext += i 
    return encryptedtext

cipherkey = keygen() # Random char
plaintext = input("Enter your message to be encrypted: ")
enc_message = encrypt(cipherkey, plaintext)
print("Here is your encrypted message: " + enc_message)

# Uncomment below code to perform decipher
# def decrypt_key(ckey):
#     decipherkey = {}
#     for i in ckey:
#         decipherkey[ckey[i]] = i
#     return decipherkey    


# decipherkey = decrypt_key(cipherkey)
# dec_message = encrypt(decipherkey, enc_message)
# print("Here is your decrypted message: " + dec_message)
# print(cipherkey, decipherkey)
