#!/usr/bin/python3
""" function that returns Json representation of an object string """
import json
def to_json_string(my_obj):
	"""
	args:
		my_obj - object to be converterd to Json
	Returns:
		the Json representation of an object string
	"""
	return json.dumps(my_obj)

