import unittest
from string_calculator import stringCalculator


class testCalculator(unittest.TestCase):
    def setUp(self):
        self.obj = stringCalculator()

    def test_StringIsEmpty(self):
        self.assertEqual(self.obj.add(" "), 0)
