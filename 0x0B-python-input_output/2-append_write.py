#!/usr/bin/python3
""" function for appending text """

def append_write(filename="", text=""):
	""" the target file has an encoding="utf-8"
	args:
		filename - name of the destination file in which the text is t be added and appended
		text - text to be appended
	returns:
		number of characers to be appended
	"""
	with open(filename, "a", encoding="utf-8") as f:
		return f.write(text)

