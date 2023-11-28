"""
File: coin_flip_runs.py
Name: Paul
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random


def main():
    """
    :param: Show title and ask for input values.
    :return: The game continues until a certain number of same results is reached.
    """
    print("Let's flip a coin!")
    num_run = int(input("Number of runs: "))  # Ask the user for input
    run = 0
    roll1 = random.randint(1, 2)  # Flip the coin for the first time
    is_in_a_row = False  # Initial switch for consecutive same results
    flips = ''
    if roll1 == 1:  # If the result of the first flip is 1, it's a head
        flip = 'H'
    else:  # Otherwise, it's a tail
        flip = 'T'
    flips += flip  # Add the result to the string
    while run < num_run:  # Flipping until reaching the desired number.
        roll2 = random.randint(1, 2)
        if roll1 == roll2:  # If the result of two rolls is same
            if not is_in_a_row:
                run += 1
                is_in_a_row = True  # Set the switch to True
        else:
            is_in_a_row = False
        roll1 = roll2  # Update the result of the previous flip to be used in the next loop
        if roll1 == 1:
            flip = 'H'
        else:
            flip = 'T'
        flips += flip
    print(flips, end='')  # Print all results on the same line


if __name__ == "__main__":
    main()
