# This file is used to test the calc.py file. This is saved under test_calc.py

# The unittest module has options that will help us test
import unittest
# We import the functions we want to test from the file calc
from calc import add, divide, exponent, multiply, subtract


class CalculatorTest(unittest.TestCase):
    # the (unittest.TestCase) has this class extend the TestCase class
    # contained within the unittest module

    # The test functions must start with test or they will not run.

    def testAdd(self):
        self.assertEqual(4, add(2, 2))
        self.assertEqual(2, add(0, 2))

    def testMultiply(self):
        self.assertEqual(4, multiply(2, 2))
        self.assertEqual(0, multiply(5, 0))
        self.assertEqual(5, multiply(5, 1))

    def testDivide(self):
        self.assertEqual(1, divide(2, 2))
        self.assertEqual(2.5, divide(5, 2))
        self.assertRaises(ZeroDivisionError, divide, 5, 0)

    def testSubtract(self):
        self.assertEqual(0, subtract(2, 2))
        self.assertEqual(5, subtract(5, 0))
        self.assertEqual(4, subtract(5, 1))
        self.assertEqual(-1, subtract(5, 6))

    def testExpontent(self):
        self.assertEqual(4, exponent(2, 2))
        self.assertEqual(1, exponent(5, 0))
        self.assertEqual(5, exponent(5, 1))


# This piece of code looks for any function that extends unittest and
# runs it. So in this case it will run all the functions within the
unittest.main()
