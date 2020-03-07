# Assignment 1
This is a complete python program to encrypt and decrypt classical ciphers:

-Shift Cipher

-Affine Cipher

-Vigenere Cipher

# The Program is callable from command line as follows:
◦ First argument is the cipher type [“shift”,”affine”,”vigenere”].

◦ Second argument is the operation type [“encrypt”, “decrypt”].

◦ The Third argument is the input file.

◦ The fourth argument is the output file.

◦ The last argument is the the list of encryption keys required for the cipher.(S for Shift - A,B for Affine - Key for Vigenere)

# Examples calls from terminal:
```
py -3 solution.py affine encrypt input.txt output.txt 17 20
py -3 solution.py affine decrypt input.txt output.txt 17 20
py -3 solution.py shift encrypt input.txt output.txt 4
py -3 solution.py shift decrypt input.txt output.txt 4
py -3 solution.py vigenere encrypt input.txt output.txt AYUSH
py -3 solution.py vigenere decrypt input.txt output.txt AYUSH
```
