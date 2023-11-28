"""
File: triangular_checker.py
Name: Paul
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    Pre-conditions: This code starts the title and waits for user's input.
    Post-conditions:
    1. The code checks if the entered value is a triangular number and informs the user.
    2. The code continues to prompt the user for input until the user enters -100.
    """
    print('Welcome to the triangular number checker!')
    data = int(input('Enter a value:'))  # wait for user input
    while data != EXIT:  # escape the loop
        n = 1  # set n = 1
        while n * (n + 1) / 2 <= data:  # Check if triangular number is less than or equal to the input data
            if data == n * (n + 1) / 2:  # If it is equal to data, it is a triangular number
                print(str(data) + ' is a triangular number.')
                break
            n += 1
        else:  # the input data is not a triangular number
            print(str(data) + ' is not a triangular number.')
        data = int(input('Enter a value:'))  # wait for user input
    print('Have a good one!')

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    main()
