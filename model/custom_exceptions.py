"""
Author: Alek Brown
Program: Borrow My Tools
Date: 2021-04-22

This file will hold any custom exceptions used in this program
"""


class InvalidEmailError(Exception):
    """This exception is for invalid email formats"""
    pass


class InvalidPhoneError(Exception):
    """This exception is for invalid phone number formats"""
    pass


class InvalidNameError(Exception):
    """This exception is for invalid human name characters"""
    pass
