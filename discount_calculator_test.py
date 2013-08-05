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
