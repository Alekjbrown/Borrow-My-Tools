"""
Author: Alek Brown
Program: Borrow My Tools
Date: 2021-04-04

This unittest suite runs against the person object
"""

import unittest
from model.person import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        """ setup for tests"""
        self.p = Person('Ali', 'Brown', '515-771-5940', 'alekjbrown@live.com', 1)
        self.pr = Person('Alek', 'Brown', id=2)

    def tearDown(self) -> None:
        """ tear-down for tests"""
        del self.p
        del self.pr

    def test_valid_initial_value_required_attributes(self):
        """ test object creation with only required attributes"""
        self.assertEqual(2, self.pr.id)
        self.assertEqual('Alek', self.pr.first_name)
        self.assertEqual('Brown', self.pr.last_name)

    def test_valid_object_all_attributes(self):
        """ test object creation with all attributes"""
        self.assertEqual(1, self.p.id)
        self.assertEqual('Ali', self.p.first_name)
        self.assertEqual('Brown', self.p.last_name)
        self.assertEqual('515-771-5940', self.p.phone_number)
        self.assertEqual('alekjbrown@live.com', self.p.email)

    def test_object_not_created_invalid_id(self):
        """ test object failed creation for invalid tool type"""
        with self.assertRaises(InvalidIdError):
            p1 = Person('Ali', 'Brown', id='A')

    def test_object_not_created_invalid_fname(self):
        """ test object failed creation for invalid price"""
        with self.assertRaises(InvalidNameError):
            p1 = Person('34', 'Brown', id=1)

    def test_object_not_created_invalid_lname(self):
        """ tet object failed creation for invalid date"""
        with self.assertRaises(InvalidNameError):
            p1 = Person('Ali', '66', id=1)

    def test_object_not_created_invalid_phone(self):
        """ test object failed creation for invalid borrowed boolean"""
        with self.assertRaises(InvalidPhoneError):
            p1 = Person('Ali', 'Brown', '515771-5940', id=1)

    def test_object_not_created_invalid_email(self):
        # TODO create email validation in person class
        assert True == False

    def test_repr(self):
        """ test object __repr__ method"""
        # self.assertEqual("Tool(1,1A2B3C,Hand,10mm Socket,Mac,8.97," + str(datetime.now().ctime()) + ",False)", self.t.__repr__())


if __name__ == '__main__':
    unittest.main()
