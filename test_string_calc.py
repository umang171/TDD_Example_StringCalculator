import unittest
from string_calculator import stringCalculator


class testCalculator(unittest.TestCase):
    def setUp(self):
        self.obj = stringCalculator()

    def test_StringIsEmpty(self):
        self.assertEqual(self.obj.add(" "), 0)

    def test_StringIsOneNumber(self):
        self.assertEqual(self.obj.add("4"), 4)

    def test_StringIsTwoNumber(self):
        self.assertEqual(self.obj.add("3,4"), 7)

    def test_StringIsMoreThanTwoNumber(self):
        self.assertEqual(self.obj.add("1,2,3"), 6)

    def test_StringwithNewLine(self):
        self.assertEqual(self.obj.add("1,2\n3"), 6)
