"""
File: number_checker.py
Name: Paul
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    Pre-conditions: This code starts the title and waits for user's input.
    Post-conditions:
    1. While entering the data, this code calculates the total of the factors.
    2. Compare the result and input data and print the final result.
    """
    print('Welcome to the number checker!')
    data = int(input('Enter a value (n>1):'))  # wait for user input
    while True:
        if data == EXIT:  # escape the loop
            print('Have a good one!')
            break
        else:
            n = 1  # set initial factor as 1
            plus = 0  # set all factors summing up result as 0
            while n < data:  # loop when factor value is below input data
                if data % n == 0:  # data divided by factor must be even, then collect n.
                    plus += n  # plus all factors
                n += 1  # loop n each time +1
            if plus == data:  # check plus if is equal to input
                print(str(data) + ' is a perfect number.')
            elif plus > data:  # check plus if is bigger than input
                print(str(data) + ' is an abundant number).')
            else:  # check plus if is smaller input
                print(str(data) + ' is a deficient number.')
        data = int(input('Enter a value (n>1):'))  # wait for user input


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
