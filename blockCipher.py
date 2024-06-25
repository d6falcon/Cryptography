#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation. # This is a Simple DES-like function (not secure, just for demonstration)
#Author: Srikanth Dabbiru
#Implements a block cipher.
import random

def des_encrypt(block, key):
    random.seed(key)
    return bytearray([b ^ random.randint(0, 255) for b in block])

def des_decrypt(block, key):
    random.seed(key)
    return bytearray([b ^ random.randint(0, 255) for b in block])

# Double DES encryption
def double_des_encrypt(plaintext, key1, key2):
    return des_encrypt(des_encrypt(plaintext, key1), key2)

# Double DES decryption
def double_des_decrypt(ciphertext, key1, key2):
    return des_decrypt(des_decrypt(ciphertext, key2), key1)

# Meet-in-the-middle attack on Double DES
def meet_in_the_middle_attack(plaintext, ciphertext):
    # Dictionary to store the intermediate values
    intermediate_dict = {}
    
    # Generate all possible keys (for simplicity, keys are in range(256))
    for k1 in range(256):
        intermediate_value = des_encrypt(plaintext, k1)
        intermediate_dict[bytes(intermediate_value)] = k1
    
    for k2 in range(256):
        intermediate_value = des_decrypt(ciphertext, k2)
        if bytes(intermediate_value) in intermediate_dict:
            k1 = intermediate_dict[bytes(intermediate_value)]
            return k1, k2
    
    return None, None

def main():
    # Example usage
    plaintext = bytearray("hello".encode('utf-8'))
    key1 = 22
    key2 = 89

    # Encrypt the plaintext using double DES
    ciphertext = double_des_encrypt(plaintext, key1, key2)
    print(f"Ciphertext: {ciphertext}")

    # Perform meet-in-the-middle attack
    recovered_key1, recovered_key2 = meet_in_the_middle_attack(plaintext, ciphertext)
    
    if recovered_key1 is not None and recovered_key2 is not None:
        print(f"Recovered keys: Key1={recovered_key1}, Key2={recovered_key2}")
        # Verify the keys
        decrypted_text = double_des_decrypt(ciphertext, recovered_key1, recovered_key2)
        print(f"Decrypted text: {decrypted_text.decode('utf-8')}")
    else:
        print("Failed to recover the keys")

if __name__ == "__main__":
    main()
