"""
File: narcissistic_checker.py
Name: Paul
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def count_digits(n):
    # count the digits of input data.
    n_digits = 0  # set digits staring from 0
    while n > 0:  # while input data > 0, then loop
        n_digits += 1  # digits plus 1 each loop
        n //= 10  # check the digits number by dividing data by 10 each loop
    return n_digits


def sum_digits(n, n2):
    # count the total of all the digits.
    total = 0  # set total starting from 1
    while n > 0:  # while input data > 0, then loop
        digits = n % 10  # find the digit value by dividing 10 and see the remainder.
        total += digits ** n2
        n //= 10  # remove the last digit.
    return total


def main():
    """
    Pre-conditions: This code starts with the title and waits for user's input.
    Post-conditions:
    1. The code checks if the entered value is a narcissistic number and shows the result to user.
    2. The code continues to prompt the user for input until the user enters -100.
    """
    print('Welcome to the narcissistic number checker!')
    data = int(input('Enter a integer value:'))  # wait for user input

    while data != EXIT:  # escape the loop
        n_digits = count_digits(data)  # store the value from count_digits
        store_sum_digits = sum_digits(data, n_digits)  # store the value from sum_digits
        if store_sum_digits == data:
            print(str(data), 'is a narcissistic number.')
        else:
            print(str(data), 'is a not narcissistic number.')
        data = int(input('Enter a integer value:'))  # wait for user input
    print('Have a good one!')


if __name__ == '__main__':
    main()
