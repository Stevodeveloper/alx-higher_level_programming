#!/usr/bin/python3
import json
""" function that returns Json representation of an object string """

def to_json_string(my_obj):
	"""
	args:
		my_obj - object to be converterd to Json
	Returns:
		the Json representation of an object string
	"""
	return json.dumps(my_obj)

