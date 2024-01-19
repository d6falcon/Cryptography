#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation
#Author: Srikanth Dabbiru
#Implement a brute forcer to break any substitution cipher taking the cipher text as the input
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

def decrypt(decipher, dec_message):
   decrypted = ""
   for i in dec_message:
      if i in decipher:
         decrypted += decipher[i]
      else: #Keep unknown chars from keygen as-is
         decrypted += i
   return decrypted
         
encryptedtext = input("Enter your message to be decrypted: ")
for n in range(26): # Roll through all the keys for the alphabet length to discover which ROT method was used as the algorithm to encrypt
    decipher = keygen(26-n)
    dec_message = decrypt(decipher, encryptedtext)
    print("ROT" + str(n) + ":" + " " + dec_message)

print("Look through above keys to find plain text. The corresponding ROT method is the algorithm used to encrypt")