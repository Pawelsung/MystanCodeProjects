"""
File: hailstone.py
Name: Paul
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""
EXIT = -1


def main():
    """
    Pre-conditions: This code starts the title and waits for user's input.
    Post-conditions:
    1. This code analyse the input value to check is an even or odd number.
    2. It follows the formula to make the value calculated each time and prints out the steps.
    3.Then, it prints out the final result.
    """
    print('This program computes Hailstone Sequence')
    n = int(input('Enter a number: '))
    count = 0  # Count loop times
    if n <= 0:  # Initial condition to avoid invalid input.
        print('Incorrect input')
    else:
        while n != 1:
            count += 1  # Store the loop times by adding 1 each time.
            # n_even = int(n/2)
            # n_odd = int(3*n+1)
            if n % 2 == 0:  # if n is an even number
                n = n // 2
                print(str(n*2) + ' is even, so I take half: ' + str(n))

            else:
                n = 3 * n + 1  # if n is an odd number
                print(str((n-1)//3) + ' is odd, so I make 3n+1: ' + str(n))
        print('It took ' + str(count) + ' steps to reach 1.')   # escape loop if input is 1.


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == "__main__":
    main()
