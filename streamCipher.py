#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation
#Author: Srikanth Dabbiru
#Implements a stream cipher. It is similar to a one time pad except the number is randomly generated therefore, the XOR functions still apply such as below. For random generation, we use something called LCG (linear congruential generator) - generate random keys but each time the function is run it generates the same set of random keys thus solving the problem that one time pads had

# Uncomment below to test out simple XOR, the foundation of one time pads
# def xor(x, s): # sample xor function
#     print(x, 'xor', s, '=', (x ^ s))  # ^ operates as a xor in python
    
# xor(4, 8) 
# xor(12, 8) # this is the basic logic of XOR function, the above 4 and 8 xor sample results in 12 so if we assume 12 is the cipher and then xor it with the same random key in this case an 8, that results in the original message which is 4 in this case.

class keyStream:    #define a class with key stream needed, default the seed by 1 if not called at line 25
    def __init__(self, key=1):
        self.next = key
        
    def random(self):
        self.next = (1103515245*self.next + 12345) % 2**31  # this is LCG implementation that generates and solves one time pad problem
        return self.next
    
    def generate_keystream(self):
        return self.random() % 1024  # returns random numbers between 0 to 1024
    
key = keyStream(15) # insert any seed value here to generate same set of random numbers
for i in range(10):
    print(key.generate_keystream())
    
    