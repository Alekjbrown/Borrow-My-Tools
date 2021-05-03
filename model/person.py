"""
Author: Alek Brown
Program: Borrow My Tools
Date: 2022-04-20

this class represents a person object
"""
import re
from custom_exceptions import *


class Person:
	""" This class represents a person object"""
	def __init__(self, fname, lname, phone, email):
		"""Constructor"""
		char_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'-")

		if not char_set.issuperset(fname, lname):
			raise InvalidNameError
		regex = re.compile('[0-9]{3}-[0-9]{3}-[0-9]{4}', re.I)
		match = regex.match(phone)
		if not match:
			raise InvalidPhoneError
		self._first_name = fname
		self._last_name = lname
		self._phone = phone
		self._email = email

	@property
	def first_name(self):
		return self._first_name

	@property
	def last_name(self):
		return self._last_name

	@property
	def phone_number(self):
		return self._phone

	@property
	def email(self):
		return self._email

	def update_email(self, email):
		regex = re.compile('^[A-Z0-9._%+-]+@[A-Z0-9.-]+[.][A-Z]{2,63}$')
		if regex.match(email):
			self._email = email

	def update_phone(self, phone):
		regex = re.compile('[0-9]{3}-[0-9]{3}-[0-9]{4}', re.I)
		if regex.match(phone):
			self._phone = phone

	def __repr__(self):
		return '%s(%s,%s,%s,%s)' % (self.__class__.__qualname__, self._first_name, self._last_name, self._phone,
									self._email)
