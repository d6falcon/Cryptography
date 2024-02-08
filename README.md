# Cryptography

Author: Srikanth Dabbiru

The scripts under this repo are free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation

Implementing various Cryptography methods using Python programming

| Program        | Description          |
| ------------- |:-------------:|
| caesarCipher.py     | Implements Caesar Cipher i.e., ROT3. Keeps unknown chars as-is    |
| caesarDecipher.py     | Implements Decipher mechanism to decrypt message encrypted using Caesar cipher i.e., ROT3. Keeps unknown chars as-is    |
| bruteforceDecipher.py     | Implements a program to perform Cryptanalysis in order to break Caesar cipher taking the cipher-text as the input. This Cryptanalysis program teaches us about the Kerckhoff's principle which is the security of a cryptosystem must lie in the choice of its keys, the algorithm can be known to the public. In the case of Caesar cipher, the security of the system lies in the algorithm being secret which is why it can easily be brute-forced once the algorithm is known. The rationale is that the key space of the Caeasar cipher or a similar Shift cipher is very small, 25 to be precise as there are only 26 letters in the English alphabet.   |
|                                                                                      |
| |This above vulnerability in the Cryptosystem resulted in the evolution of Substitution ciphers. This means we look at increasing the key space by randomizing the alphabets that can be substituted with. The key space in that case would be 26! (26 facotrial = 403291461126605635584000000)   |
| substitutionCipher.py     | Implements Substitution Cipher where key space is same however there is no shift (ROT) implemented, the key gen is random. Keeps unknown chars as-is     |
| substitutionDecipher.py     | Implements Substitution Decipher mechanism to decrypt message encrypted using Substitution cipher with random key. Keeps unknown chars as-is     |