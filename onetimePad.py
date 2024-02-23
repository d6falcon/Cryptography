#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation
#Author: Srikanth Dabbiru
#Implements a one time pad - simple stream cipher

# Uncomment below to test out simple XOR, the foundation of one time pads
# def xor(x, s): # sample xor function
#     print(x, 'xor', s, '=', (x ^ s))  # ^ operates as a xor in python
    
# xor(4, 8) 
# xor(12, 8) # this is the basic logic of XOR function, the above 4 and 8 xor sample results in 12 so if we assume 12 is the cipher and then xor it with the same random key in this case an 8, that results in the original message which is 4 in this case.

import random

class onetimepad:
  def __init__(self): # constructor class
    self.plaintext = input('Enter your message:').encode()
    self.message_length = len(self.plaintext)

  def generate_keystream(self):
    return bytes(random.randrange(0, 250) for _ in range(self.message_length)) #optionally you may use a list here instead of bytes, end of the day your aim is get a random key

  def encrypt(self, cipherkey):
    # minimumlength = min(len(cipherkey), self.message_length) #incase the length of cipher key is different from length of original message then you might want to use this min method and replace the range below - srikanthd.
    return bytes([cipherkey[i] ^ self.plaintext[i] for i in range(self.message_length)])

  def decryptkey(self, ciphertext_length):
    return bytes(random.randrange(0, 250) for _ in range(ciphertext_length))


otp = onetimepad()

cipherkey = otp.generate_keystream()
ciphertext = otp.encrypt(cipherkey)

# here we play the role of attacker and try and guess the keystream by looking at the length of cipher
ciphertext_length = len(ciphertext)
decipherkey = otp.decryptkey(ciphertext_length)
deciphertext = otp.encrypt(decipherkey)

print('Here is the random key:', cipherkey, '\n')
print('Here is the encrypted message:', ciphertext, '\n')
print('Here is the decrypted message:', deciphertext, '\n') # Unable to decrypt hence proving that it is impossible to break OTP eventhough we know the length of cipher text and frequency analysis doesnt work in this case - Unless you have the correct key

# so essentially - lets say Enc is encryption and Dec is the decryption function, Enc(M, K) = C = M XOR K, where K is key used and M is the message, C is the cipher text. Decryption is performed by Dec(C, K) = M = C XOR K = Dec(Enc(M, K), K)

