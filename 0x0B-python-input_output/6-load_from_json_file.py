#!/usr/bin/python3
""" loads object from file """
from json import loads

def load_from_json_file(filename):
	"""
	args:
		filename - the json file name
	"""
	with open(filename, mode = "r") as f:
		return loads(f.read())

