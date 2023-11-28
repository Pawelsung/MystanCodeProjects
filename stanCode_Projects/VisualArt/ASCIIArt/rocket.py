"""
File: rocket.py
Name: Paul
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 10
# SIZE determines rocket size.


def head(n1):
    # This function prints the head of the rocket.
    data = n1
    for i in range(data):  # Loop through each row
        for j in range(data - i):  # Print spaces to center the head
            print(" ", end="")
        for j in range(i + 1):  # Print the head pattern
            print("/", end="")
        for j in range(i + 1):
            print("\\", end="")
        print("")


def belt(n2):
    # This function prints the belt of the rocket
    for i in range(1):  # Print the left edge of the belt
        print("+", end="")
        for j in range(2*n2):  # Print the belt pattern
            print("=", end="")   # Print the right edge of the belt
        print("+", end="")
    print("")


def upper(n3):
    # This function prints the upper body of the rocket
    data = n3
    for i in range(data):
        print("|", end="")  # Print the left edge of the upper body
        for j in range(data - i - 1):  # Print spaces to center the upper body pattern
            print(".", end="")
        for j in range(i + 1):  # Print the upper body pattern
            print("/\\", end="")
        for j in range(data - i - 1):  # Print spaces to center the upper body pattern
            print(".", end="")
        print("|")  # Print the right edge of the upper body


def lower(n4):
    # This function prints the lower body of the rocket
    data = n4
    for i in range(data):
        print("|", end="")  # Print the left edge of the lower body
        for j in range(i):  # Print spaces to center the lower body pattern
            print(".", end="")
        for j in range(data - i):  # Print the lower body pattern
            print("\\/", end="")
        for j in range(i):  # Print spaces to center the lower body pattern
            print(".", end="")
        print("|", end="")  # Print the right edge of the lower body
        print("")


def main():
    """
    Pre-conditions: SIZE must be defined as a positive integer value.
    Post-conditions: Prints a rocket of size SIZE to the console.
    """
    data = SIZE
    head(data)
    belt(data)
    upper(data)
    lower(data)
    belt(data)
    head(data)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
