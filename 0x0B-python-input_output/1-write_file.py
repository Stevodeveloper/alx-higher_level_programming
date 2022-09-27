#!/usr/bin/python3
""" defining a function writing to a file """

def write_file(filename="", text=""):
	""" with a utf-8
	
	args:
		filename- name of the file to be written to
		text - contents to be in the file
	returns:
		the number of characters written to the file
	"""
	with open(filename, mode = "w", encoding="utf-8") as f:
		return f.write(text)

