#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation
#Author: Srikanth Dabbiru
#Implements a stream cipher. It is similar to a one time pad except the number is randomly generated. For random generation, we use something called LCG (linear congruential generator) - generate random keys but each time the function is run it generates the same set of random keys thus solving the problem that one time pads had


class keyStream:    #define a class with key stream needed, default the seed by 1 if not called at line 17
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
    
# work in progress...

# declare a message
# encrypt
# decrypt


# explain problem(s) with stream cipher:
   # No Authenticity - intercepting and changing the original message
   # Key reuse
   # Low entropy