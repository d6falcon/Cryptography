#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation
#Author: Srikanth Dabbiru
#Implement a substitution decipher (Caesar cipher) taking the cipher text as the input
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

def decrypt(decipherkey, dec_message):
   decryptedtext = ""
   for i in dec_message:
      if i in decipherkey:
         decryptedtext += decipherkey[i]
      else: #Keep unknown chars from keygen as-is
         decryptedtext += i
   return decryptedtext
         
decipherkey = keygen(26-3) # Caesar cipher functional requirement of ROT3, You may modify it to suit your needs, for e.g., if you need to implement ROT13 substitution cipher just change the number from 3 to 13
encryptedtext = input("Enter your ROT3 message to be decrypted: ")
dec_message = decrypt(decipherkey, encryptedtext)
print("Here is your deciphered message: " + dec_message)
