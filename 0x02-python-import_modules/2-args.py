#!/usr/bin/python3
if __name__ == "__main__":
	from sys import argv
	counter = len(argv)
	
	if counter == 2:
		print('{} argument:'.format(counter - 1))
	elif counter < 2:
		print('{} arguments.'.format(counter - 1))
	else:
		print('{} arguments:'.format(counter - 1))

	for i in range(1, counter):
		print('{}: {}'.format(i, argv[i]))
