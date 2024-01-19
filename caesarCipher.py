#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation
#Author: Srikanth Dabbiru
#Implement a substitution cipher (Caesar cipher) taking the message as the input
def keygen(x):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    count = 0
    for char in alphabets:
        key[char] = alphabets[(count + x) % len(alphabets)] 
        count += 1
    for char in Alphabets:
        key[char] = Alphabets[(count + x) % len(Alphabets)] 
        count += 1
    return key

def encrypt(cipher, plaintext):
    encrypted = ""
    for i in plaintext:
       if i in cipher:
        encrypted += cipher[i]
       else:    #Keep unknown chars from keygen as-is
        encrypted += i 
    return encrypted

cipher = keygen(3) # Caesar cipher functional requirement of ROT3, You may modify it to suit your needs, for e.g., if you need to implement ROT13 substitution cipher just change the number from 3 to 13
plaintext = input("Enter your message to be encrypted: ")
enc_message = encrypt(cipher, plaintext)
print("Here is your encrypted message: " + enc_message)
