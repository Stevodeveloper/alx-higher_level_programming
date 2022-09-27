#!/usr/bin/python3
""" file reading function printing the contents to stdout"""

def read_file(filename=""):
	"""the file has an encoding utf-8"""
	with open(filename, encoding="utf-8") as f:
		print(f.read(), end="")

