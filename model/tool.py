"""
Author: Alek Brown
Program: Borrow My Tools
Date: 2022-04-20

this class represents a tool object
"""
import datetime


class Tool:
    """ this class represents a tool object"""

    def __init__(self, sn, t_type, description, brand, price, purchase_date: datetime = datetime.datetime.now(),
                 borrowed: bool = False, tid=None):

        num_set = set('1234567890.')
        char_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYXZ abcdefghijklmnopqrstuvwxyz'-")
        self._purchase_date = None
        if not num_set.issuperset(str(price)) or not char_set.issuperset(
                str(t_type)):
            raise ValueError
        if tid:
            if not num_set.issuperset(str(tid)):
                raise ValueError
        if not isinstance(purchase_date, datetime.datetime):
            try:
                self._purchase_date = datetime.date.fromisoformat(purchase_date)
            except:
                raise TypeError
        if borrowed == 0:
            self._borrowed = False
        elif borrowed == 1:
            self._borrowed = True
        elif borrowed == False:
            self._borrowed = False
        elif borrowed == True:
            self._borrowed = True
        else:
            raise TypeError
        self._tid = tid
        self._sn = sn
        self._tool_type = t_type
        self._description = description
        self._brand = brand
        self._price = price
        if not self._purchase_date:
            self._purchase_date = purchase_date.date()


    @property
    def tool_id(self):
        return self._tid

    @property
    def serial_number(self):
        return self._sn

    @serial_number.setter
    def serial_number(self, sn):
        self._sn = sn

    @property
    def tool_type(self):
        return self._tool_type

    @tool_type.setter
    def tool_type(self, tt):
        self._tool_type = tt

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, desc):
        self._description = desc

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def purchase_date(self):
        return self._purchase_date

    @property
    def borrowed(self):
        return self._borrowed

    @borrowed.setter
    def borrowed(self, borrowed):
        self._borrowed = borrowed

    def __repr__(self):
        return '%s(%s,%s,%s,%s,%s,%s,%s,%s)' % (
            self.__class__.__qualname__, self._tid, self._sn, self._tool_type, self._description, self._brand, self._price,
            self._purchase_date, self._borrowed)

        # TODO fix __repr__ to show tid as last param (include unit tests)
