"""
File: factorial.py
Name: Paul
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    Pre-conditions: Showing instructions and waiting for user entering values.
    Post-conditions: This code calculates the input number and print the result answer till entering -100.
    """
    print('Welcome to stanCode factorial master!')
    data = int(input('Give me a number, and I will list the answer of factorial:'))  # wait for user input
    if data == EXIT:
        print('- - - - - - See ya! - - - - - -')
    else:
        while True:
            if data == EXIT:  # escape the loop
                print('- - - - - - See ya! - - - - - -')
                break
            else:
                fac = 1   # set 1
                k = 1  # set number initiates from 1
                for i in range(data-1):  # input data-1 as loop times
                    k += 1  # each loop  does k+1
                    fac *= k  # save result into fac for next loop
                print(fac)  # print result
            data = int(input('Give me a number, and I will list the answer of factorial:'))  # wait for user input


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
