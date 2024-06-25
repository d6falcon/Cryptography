# Cryptography

Author: Srikanth Dabbiru

The scripts under this repo are free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation

Implementing various Cryptography methods using Python programming

|S.no| Program        | Description          |
| :---: | :-------------: |:-------------:|
|1| `caesarCipher.py`     | Implements Caesar Cipher i.e., ROT3. Keeps unknown chars as-is    |
|2| `caesarDecipher.py`     | Implements Decipher mechanism to decrypt message encrypted using Caesar cipher i.e., ROT3. Keeps unknown chars as-is    |
|3| `bruteforceDecipher.py`     | Implements a program to perform Cryptanalysis in order to break Caesar cipher taking the cipher-text as the input. This Cryptanalysis program teaches us about the Kerckhoff's principle which is the security of a cryptosystem must lie in the choice of its keys, the algorithm can be known to the public. In the case of Caesar cipher, the security of the system lies in the algorithm being secret which is why it can easily be brute-forced once the algorithm is known. The rationale is that the key space of the Caeasar cipher or a similar Shift cipher is very small, 25 to be precise as there are only 26 letters in the English alphabet.   |
|                                                                                      |
| |This above vulnerability in the Cryptosystem resulted in the evolution of Substitution ciphers. This means we look at increasing the key space by randomizing the alphabets that can be substituted with. The key space size in that case would be 26! (26 factorial = 403291461126605635584000000 possible keys may be generated or 88 bit length)   ||
|4| `substitutionCipher.py`     | Implements Substitution Cipher where key space is same however there is no shift (ROT) implemented, the key gen is random. Keeps unknown chars as-is. They are insecure today becuase they can be broken using frequency analysis where for e.g. alphabet 'e' occurs 12.7% of times in any english article (For more on Frequency analysis: https://en.wikipedia.org/wiki/Letter_frequency)   |
|5| `frequencyAnalysis.py`     | Implements Frequency Analysis to break any Substitution Cipher. Absolute value is used to compare the english alphabet frequency and the calculated frequency from the cipher text.   |
|6| `onetimePad.py`     | Implements One Time Pad. It is a simple example of stream cipher however technically its not a full blown stream cipher which are used commonly between client/server communication. The one time pads are known to be unbreakable or in other words impossible to break unless the key used to encrypt is known. Welcome to the world of Secure Comms! However, there are problems around using this kind such as the key stream needs to be as long as the message that needs to be encrypted! With the amount of data sent in the modern world the implementation of one time pad is unfathomable.  |
|7| `streamCipher.py`     | Stream Ciphers are similar to one time pads except the number is randomly generated here. Stream ciphers do not have the same problem with key stream such as the one time pads because of the implementation of LCG. Typical use cases in Mobile Phones. Bit by bit XOR function applied.|
|8| `blockCipher.py`    | Block Ciphers are 8bytes in size per block. Therefore, in this case the encryption works block by block instead of bit by bit. Most common cipher is the DES (56-bit) that was designed and developed by IBM. Russians developed a similar cipher called GOST however the bit size was 256-bit. |
