from unittest import TestCase
from caculate_pay import calculate_pay


class TestCalculatePay(TestCase):
    def test_zeros(self):
        self.assertEqual(0, calculate_pay(0, 0))

    def test_zero_hour(self):
        self.assertEqual(0, calculate_pay(0, 5))

    def test_zero_wage(self):
        self.assertEqual(0, calculate_pay(5, 0))

    def test_negative_hour(self):
        self.assertEqual(0, calculate_pay(-1, 0))

    def test_negative_wage(self):
        self.assertEqual(0, calculate_pay(0, -1))

    def test_regular_wage(self):
        self.assertEqual(0, calculate_pay(40, 40))

    def test_regular_wage(self):
        self.assertEqual(0, calculate_pay(39.5,5.5 ))

