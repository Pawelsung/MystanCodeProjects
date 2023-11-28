"""
File: caesar.py
Name: Paul
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def replace(n):
    """
    :param n: an integer, the number of positions to shift the alphabet
    :return: a string stored the shifted alphabet
    """
    ans = ""
    # for i in range(len(ALPHABET)):
    ans += ALPHABET[len(ALPHABET) - n:] + ALPHABET[0:len(ALPHABET) - n]  # Shift the alphabet by n positions
    return ans


def compare(n, n2):
    """
    :param n: a str representing the shifted alphabet
    :param n2: a str representing the ciphered text
    :return: a str representing the deciphered text
    """
    ans = ""
    for i in range(len(n2)):  # loop according to the length of n2
        new = n.find(n2[i])  # Find the index of the character in n
        if new != -1:  # If found, add the character from the original alphabet to the answer
            ans += ALPHABET[new]
        else:  # If not found, check if there is a special character and add to answer
            if n2[i] == "!":
                ans += "!"
            elif n2[i] == " ":
                ans += " "
    return ans


def main():
    """
    Pre-conditions: User inputs a secret number. Then, a ciphered string.
    Post-conditions: This code shows the deciphered string.
    """
    sec_num = int(input('Secret number: '))  # Get secret number from user input
    new_alp = replace(sec_num)  # Shift the alphabet by the input secret number
    cip_str = input("What's the ciphered string? ").upper()  # Get input and convert it to uppercase
    # cip_str = cip_str.upper()
    result = compare(new_alp, cip_str)  # Replace the ciphered string using the shifted alphabet
    print('The deciphered string is: ' + result)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
