"""
File: quadratic_solver.py
Name: Paul
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Pre-conditions: Showing instructions and waiting for user entering values.
	Post-conditions:
	1. User enters a, b, c values.
	2. a, b, c values go into formulation.
	3. Print out results according to the inputs.
	"""
	print('This is stanCode Quadratic Solver! ')
	print('Please enter a, b, c values. ')
	a = float(input('Enter a: '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))

	discriminant = b*b-4*a*c
	
	if discriminant < 0:
		print('There are no real roots.')
	else:
		# discriminant not <0 then calculate the sqrt
		sqrt = math.sqrt(discriminant)
		x1 = (-b+sqrt)/(2*a)
		x2 = (-b-sqrt)/(2*a)

		if discriminant > 0:
			print('There are two real roots.')
			print('Two roots:', (x1, x2))

		else:
			print('There is one real root.')
			print('One root:', x1)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
