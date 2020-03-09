import sys
from string import ascii_uppercase, ascii_lowercase
from math import gcd

upper = ascii_uppercase
lower = ascii_lowercase


#Ceaser cipher
def caesar_encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper() and char.isalpha():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower() and char.isalpha():
            result += chr((ord(char) + s - 97) % 26 + 97)
        elif char == ' ':
            result += ' '
        else:
            result += char

    return result


def caesar_decrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper() and char.isalpha():
            result += chr((ord(char) + 65 - s) % 26 + 65)
        elif char.islower() and char.isalpha():
            char = char.upper()
            char = chr((ord(char) + 65 - s) % 26 + 65)
            char = char.lower()
            result += char
        elif char == ' ':
            result += ' '
        else:
            result += char

    return result


#Affine Cipher
def affine_encrypt(plain_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError('a and 26 are not coprime. Please try again.')

    out = ''

    for char in plain_text:

        if char.isalpha() and char.isupper():
            y = ((a * upper.index(char)) + b) % 26
            out += upper[y]
        elif char.isalpha() and char.islower():
            y = ((a * lower.index(char)) + b) % 26
            out += lower[y]
        elif char == ' ':
            out += ' '
        else:
            out += char

    return out.strip()


def affine_decrypt(ciphered_text, a, b):
    m = 26
    if gcd(a, 26) != 1:
        raise ValueError('a and 26 are not coprime. Please try again.')

    out = ''
    n = 1
    count = 1

    while True:
        if a * n > m * count:
            if a * n == (m * count) + 1:
                break
            count += 1
        n += 1

    for char in ciphered_text:
        if char.isalpha() and char.isupper():
            d = int((n * (upper.index(char) - b)) % m)
            out += upper[d]
        elif char.isalpha() and char.islower():
            d = int((n * (lower.index(char) - b)) % m)
            out += lower[d]
        elif char == ' ':
            out += ' '
        else:
            out += char

    return out

# Vigenere Cipher
# This function generates the key
def generateKey(string, key):
    count = 0
    for char in string:
        if char.isalpha():
            count += 1

    key = list(key)
    if count == len(key):
        return (key)
    else:
        for i in range(count -
                       len(key)):
            key.append(key[i % len(key)])

    return ("".join(key))


def vigenere_encrypt(string, key):
    cipher_text = []

    j = 0
    for i in range(len(string)):
        if string[i].isalpha() and string[i].isupper():

            if key[j].isupper():
                k = upper.index(key[j])
            else:
                k = lower.index(key[j])

            x = (upper.index(string[i]) + k) % 26
            j = j + 1
            x += ord('A')
            cipher_text.append(chr(x))

        elif string[i].isalpha() and string[i].islower():
            if key[j].isupper():
                k = upper.index(key[j])
            else:
                k = lower.index(key[j])

            x = (lower.index(string[i]) + k) % 26
            j = j + 1
            x += ord('a')
            cipher_text.append(chr(x))
        else:
            cipher_text.append(string[i])
    return ("".join(cipher_text))


def vigenere_decrypt(cipher_text, key):
    orig_text = []
    j = 0
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha() and cipher_text[i].isupper():

            if key[j].isupper():
                k = upper.index(key[j])
            else:
                k = lower.index(key[j])

            x = (upper.index(cipher_text[i]) - k + 26) % 26
            j = j + 1
            x += ord('A')
            orig_text.append(chr(x))

        elif cipher_text[i].isalpha() and cipher_text[i].islower():
            if key[j].isupper():
                k = upper.index(key[j])
            else:
                k = lower.index(key[j])

            x = (lower.index(cipher_text[i]) - k + 26) % 26
            j = j + 1
            x += ord('a')
            orig_text.append(chr(x))
        else:
            orig_text.append(cipher_text[i])

    return ("".join(orig_text))


def main():

    inputfile = sys.argv[3]
    outputfile = sys.argv[4]
    file1 = open(inputfile, "r")
    text = file1.read()

    if sys.argv[1] == "shift":
        if sys.argv[2] == "encrypt":
            s = int(sys.argv[5])
            file1 = open(outputfile, "w")
            file1.write(caesar_encrypt(text, s))
            file1.close()
        elif sys.argv[2] == "decrypt":
            s = int(sys.argv[5])
            file1 = open(outputfile, "w")
            file1.write(caesar_decrypt(text, s))
            file1.close()
        else:
            print("Incorrect format of input please refer to the readme file")

    elif sys.argv[1] == "affine":
        if sys.argv[2] == "encrypt":
            a = int(sys.argv[5])
            b = int(sys.argv[6])
            file1 = open(outputfile, "w")
            file1.write(affine_encrypt(text, a, b))
            file1.close()
        elif sys.argv[2] == "decrypt":
            a = int(sys.argv[5])
            b = int(sys.argv[6])
            file1 = open(outputfile, "w")
            file1.write(affine_decrypt(text, a, b))
            file1.close()
        else:
            print("Incorrect format of input please refer to the readme file")

    elif sys.argv[1] == "vigenere":
        if sys.argv[5].isalpha():

            if sys.argv[2] == "encrypt":
                keyword = sys.argv[5]
                key = generateKey(text, keyword)
                file1 = open(outputfile, "w")
                file1.write(vigenere_encrypt(text, key))
                file1.close()
            elif sys.argv[2] == "decrypt":
                keyword = sys.argv[5]
                key = generateKey(text, keyword)
                file1 = open(outputfile, "w")
                file1.write(vigenere_decrypt(text, key))
                file1.close()
            else:
                print("Incorrect format of input please refer to the readme file")
        else:
            print("Key must consist of alphabetic letters")
    else:
        print("Incorrect format of input please refer to the readme file")


if __name__ == '__main__':
    main()
