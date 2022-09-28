#!/usr/bin/python3
""" writes an object to a file using json representation """
import json
def save_to_json_file(my_obj, filename):
	""" save sto json file
	args:
		my_obj - objject to be saved
		filename - name of the destination file where the object will be saved
	"""
	with open(filename, mode = "w") as f:
		a = json.dumps(my_obj)
		f.write(a)

