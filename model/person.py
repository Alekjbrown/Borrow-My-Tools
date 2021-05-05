"""
Author: Alek Brown
Program: Borrow My Tools
Date: 2022-04-20

this class represents a person object
"""
import re


class InvalidEmailError(Exception):
    """This exception is for invalid email formats"""
    pass


class InvalidPhoneError(Exception):
    """This exception is for invalid phone number formats"""
    pass


class InvalidNameError(Exception):
    """This exception is for invalid human name characters"""
    pass


class InvalidIdError(Exception):
    """This exception is for invalid id characters"""
    pass


class Person:
    """ This class represents a person object"""

    def __init__(self, fname, lname, phone='', email='', id=0):
        """Constructor"""
        char_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'-")
        num_set = set('0123456789')

        if not char_set.issuperset(fname) or not char_set.issuperset(lname):
            raise InvalidNameError
        regex = re.compile('[0-9]{3}-[0-9]{3}-[0-9]{4}', re.I)
        match = regex.match(phone)
        if phone:
            if not match:
                raise InvalidPhoneError
        if not num_set.issuperset(str(id)):
            raise InvalidIdError
        self._id = id
        self._first_name = fname
        self._last_name = lname
        self._phone = phone
        self._email = email

    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def phone_number(self):
        return self._phone

    @phone_number.setter
    def phone_number(self, phone):
        self._phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

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
        # TODO fix __repr__ to show id as last param (include unittests)
