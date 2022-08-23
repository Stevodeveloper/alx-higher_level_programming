#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastdigit = number % 10

if number >= 0:
	if lastdigit > 5:
		print("Last digit of {} is {} and is greator than 5".format(number, lastdigit))
	elif lastdigit == 0:
		print("Last digit of {} is {} and is 0".format(number, lastdigit))
	else:
		print("Last digit of {} is {} and is less than 6 and not 0".format(number, lastdigit))
else:
	lastdigneg = -number
	if ((lastdigneg % 10) == 0):
		print("Last digit of {} is {} and is 0".format(number, -(lastdigneg % 10)))
	else:
		print("Last digit of {} is {} and is less than 6 and not 0".format(number, -(lastdigneg % 10)))
