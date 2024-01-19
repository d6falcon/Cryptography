# Cryptography

Author: Srikanth Dabbiru

The scripts under this repo are free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation

Implementing various Cryptography methods using Python programming

| Program        | Description          |
| ------------- |:-------------:|
| caesarCipher.py     | Implements Caesar Cipher i.e., ROT3. Keeps unknown chars as-is    |
| caesarDecipher.py     | Implements Decipher mechanism to decrypt message encrypted using Caesar cipher i.e., ROT3. Keeps unknown chars as-is    |
| bruteforceDecipher.py     | Implements a brute forcer to break any substitution cipher taking the cipher text as the input. Keeps unknown chars as-is. This brute forcer teaches us about the Kerckhoff's principle which is the security of a cryptosystem must lie in the choice of its keys, the algorithm can be known. In the case of Caesar cipher or any other form of substitution cipher, the security of the system lies in the algorithm being secret which is why it can be broken into.    |