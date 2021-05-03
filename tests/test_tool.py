import unittest
from model.tool import Tool
from datetime import datetime


class PersonTestCase(unittest.TestCase):

    def setUp(self) -> None:
        """ setup for tests"""
        self.t = Tool(1, '1A2B3C', 'Hand', '10mm Socket', 'Mac', 8.97, datetime.now(), False)
        self.tr = Tool(2, '1A2B3C', 'Hand', '10mm Socket', 'Mac', 8.97)

    def tearDown(self) -> None:
        """ tear-down for tests"""
        del self.t
        del self.tr

    def test_valid_initial_value_required_attributes(self):
        """ test object creation with only required attributes"""
        self.assertEqual(2, self.tr.tool_id)
        self.assertEqual('1A2B3C', self.tr.serial_number)
        self.assertEqual('Hand', self.tr.tool_type)
        self.assertEqual('10mm Socket', self.tr.description)
        self.assertEqual('Mac', self.tr.brand)
        self.assertEqual(8.97, self.tr.price)

    def test_valid_object_all_attributes(self):
        """ test object creation with all attributes"""
        self.assertEqual(1, self.t.tool_id)
        self.assertEqual('1A2B3C', self.t.serial_number)
        self.assertEqual('Hand', self.t.tool_type)
        self.assertEqual('10mm Socket', self.t.description)
        self.assertEqual('Mac', self.t.brand)
        self.assertEqual(8.97, self.t.price)
        self.assertEqual(self.t.purchase_date, self.t.purchase_date)
        self.assertEqual(False, self.t.borrowed)

    def test_object_not_created_invalid_t_type(self):
        """ test object failed creation for invalid tool type"""
        with self.assertRaises(ValueError):
            t1 = Tool(1, '1A2B3C', 2, '10mm Socket', 'Mac', 8.97, datetime.now(), False)

    def test_object_not_created_invalid_price(self):
        """ test object failed creation for invalid price"""
        with self.assertRaises(ValueError):
            t1 = Tool(1, '1A2B3C', 'Hand', '10mm Socket', 'Mac', 'INVALID ENTRY', datetime.now(), False)

    def test_object_not_created_invalid_date(self):
        """ test object failed creation for invalid date"""
        with self.assertRaises(TypeError):
            t1 = Tool(1, '1A2B3C', 'Hand', '10mm Socket', 'Mac', 8.97, '2-2-2021', False)

    def test_object_not_created_invalid_borrowed_bool(self):
        """ test object failed creation for invalid borrowed boolean"""
        with self.assertRaises(TypeError):
            t1 = Tool(1, '1A2B3C', 'Hand', '10mm Socket', 'Mac', 8.97, datetime.now(), 'FAIL')

    def test_repr(self):
        self.assertEqual("Tool(1,1A2B3C,Hand,10mm Socket,Mac,8.97," + str(datetime.now().ctime()) + ",False)", self.t.__repr__())


if __name__ == '__main__':
    unittest.main()

    # self._tid = tid
    # self._sn = sn
    # self._tool_type = t_type
    # self._description = description
    # self._brand = brand
    # self._price = price
    # self._purchase_date = purchase_date
    # self._borrowed = borrowed
