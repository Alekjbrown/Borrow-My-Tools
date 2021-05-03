"""
Author: Alek Brown
Program: Borrow My Tools
Date: 2022-04-20

this class represents a tool object
"""
import datetime


class Tool:
    """ this class represents a tool object"""

    def __init__(self, tid, sn, t_type, description, brand, price, purchase_date: datetime = datetime.datetime.now(),
                 borrowed: bool = False):

        num_set = set('1234567890.')
        char_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYXZ abcdefghijklmnopqrstuvwxyz'-")
        if not num_set.issuperset(str(tid)) or not num_set.issuperset(str(price)) or not char_set.issuperset(
                str(t_type)):
            raise ValueError
        if not isinstance(purchase_date, datetime.date) or not isinstance(borrowed, bool):
            raise TypeError
        self._tid = tid
        self._sn = sn
        self._tool_type = t_type
        self._description = description
        self._brand = brand
        self._price = price
        self._purchase_date = purchase_date
        self._borrowed = borrowed

    @property
    def tool_id(self):
        return self._tid

    @property
    def serial_number(self):
        return self._sn

    @property
    def tool_type(self):
        return self._tool_type

    @property
    def description(self):
        return self._description

    @property
    def brand(self):
        return self._brand

    @property
    def price(self):
        return self._price

    @property
    def purchase_date(self):
        return self._purchase_date

    @property
    def borrowed(self):
        return self._borrowed

    def __repr__(self):
        return '%s(%s,%s,%s,%s,%s,%s,%s,%s)' % (
            self.__class__.__qualname__, self._tid, self._sn, self._tool_type, self._description, self._brand, self._price,
            self._purchase_date, self._borrowed)
