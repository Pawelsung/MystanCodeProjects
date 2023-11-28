"""
File: prime_checker.py
Name: Paul
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	Pre-conditions: This code starts the title and waits for user's input.
	Post-conditions:
	1. This code analyse the input value to check if is a prime number.
	2. Each time the use enters the value, it prints out the result.
	3. Escape the function by entering EXIT number.
	"""
	print('Welcome to the prime checker!')
	while True:
		prime = int(input('Enter a value (n>1):'))  # wait for user input

		if prime == EXIT:  # escape the loop
			print('Have a good one!')
			break
		if prime > 1:  # prime condition is above num 1.
			i = 2  # i is a variable used for dividing the input, starting by 2.
			while i < prime:  # condition to make i always smaller than input
				if prime % i == 0:  # prime rule: only can be divided by num 1 and itself
					print(str(prime) + ' is not a prime number.')
					break
				i += 1  # adding 1 each loop and store to i
			else:
				print(str(prime) + ' is a prime number.')
		else:
			print(str(prime) + ' is not a prime number.')

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
	main()
