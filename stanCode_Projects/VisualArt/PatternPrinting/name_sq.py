"""
File: name_sq.py
Name: Paul
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def re_arrange(n1):
    """
    :param n1: A name that user's input
    :return: None
    """
    print(n1)  # print the first row of full name
    for i in range(1, len(n1) - 1):
        print(n1[i] + " " * (len(n1)-2) + n1[len(n1)-i-1])  # Print characters starting from second character of input
    for i in range(len(n1)):
        print(n1[len(n1)-1-i], end='')  # Print the full name in reverse


def main():
    """
    Pre-conditions: Wait for user input.
    Post-conditions: Print a name in square.
    """
    print('This program prints a name in a square pattern!')
    name = input("Name: ")  # prompts user for input
    re_arrange(name)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
