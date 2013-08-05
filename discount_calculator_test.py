import unittest
from discount_calculator import DiscountCalculator


class DiscountCalculatorTests(unittest.TestCase):

    def setUp(self):
        self.discount_calculator = DiscountCalculator()

    def test_ten_percent_discount(self):
        result = self.discount_calculator.calculate(100, 10, 'percent')
        self.assertEqual(10.0, result)

    def test_twenty_percent_discount(self):
        result = self.discount_calculator.calculate(75, 20, 'percent')
        self.assertEqual(15.0, result)

    def test_five_dollar_discount(self):
        result = self.discount_calculator.calculate(250, 5, 'absolute')
        self.assertEqual(5, result)

    def test_invalid_discount_type(self):
        self.assertRaises(
            ValueError, self.discount_calculator.calculate, 250, 5, 'bears')

    def test_float_percentage_discount(self):
        result = self.discount_calculator.calculate(250.0, 5.0, 'percent')
        self.assertEqual(12.5, result)

    def test_float_absolute_discount(self):
        result = self.discount_calculator.calculate(33.0, 28.0, 'absolute')
        self.assertEqual(28.0, result)
