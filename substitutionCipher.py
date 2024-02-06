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

def encrypt(cipher, plaintext):
    encrypted = ""
    for i in plaintext:
       if i in cipher:
        encrypted += cipher[i]
       else:    #Keep unknown chars from keygen as-is
        encrypted += i 
    return encrypted

cipher = keygen() # Random char
plaintext = input("Enter your message to be encrypted: ")
enc_message = encrypt(cipher, plaintext)
print("Here is your encrypted message: " + enc_message)
