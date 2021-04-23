import re

class person:
	""" This class represents a person object"""
	
	def __init__(self, fname, lname, phone, email):
		"""Constructor"""
		char_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'-")

		if not char_set.issuperset(fname,lname):
			raise ValueError
		regex = re.compile('###-###-####',re.I)
		match = regex.match(phone)
		if not match:
			raise ValueError # TODO custom exception class??
		self._first_name = fname
		self._last_name = lname
		self._phone = phone
		self._email = email