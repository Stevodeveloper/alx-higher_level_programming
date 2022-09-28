#!/usr/bin/python3
""" json-string function"""
import json
def from_json_string(my_str):
	"""
	arg:
		my_str - the json string object to be converted to python objecte
	returns:
		 returns an object (Python data structure) represented by a JSON string
	"""
	return json.loads(my_str)

