"""
Author: Alek Brown
Program: Borrow My Tools
Date: 2022-04-20

this class represents a tool object
"""
from datetime import datetime

class Tool:
	""" this class represents a tool object"""
	
	def __init__(self, tid, sn, t_type, description, brand, price, purchase_date: datetime, borrowed: bool = False):

		num_set = set('1234567890.')
		if not num_set.issuperset(tid):
			raise ValueError
		if not purchase_date.isinstance(datetime):
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
		return self.tool_id
		
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
		return '%s(%s,%s,%s,%s,%s,%s,%s,%s)' % (self.__qualname__, self._tid, self._sn, self._tool_type,self._description,self._brand,self._price,self._purchase_date,self._borrowed)
