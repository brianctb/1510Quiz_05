from unittest import TestCase
from caculate_pay import calculate_pay


class TestCalculatePay(TestCase):
    def test_zeros(self):
        self.assertEqual(0, calculate_pay(0, 0))  # testing wages and hours are 0

    def test_zero_hour(self):
        self.assertEqual(0, calculate_pay(0, 5))  # testing hour is 0

    def test_zero_wage(self):
        self.assertEqual(0, calculate_pay(5, 0))  # testing wage is 0

    def test_negative(self):
        self.assertEqual(0, calculate_pay(-1, -1))  # testing hours and wages are 0

    def test_negative_hour(self):
        self.assertEqual(0, calculate_pay(-1, 0))  # testing hour is negative

    def test_negative_wage(self):
        self.assertEqual(0, calculate_pay(0, -1))  # testing hour is negative

    def test_regular_wage(self):
        self.assertEqual(217.25, calculate_pay(39.5, 5.5))  # testing regular hours

    def test_regular_wage(self):
        self.assertEqual(222, calculate_pay(40, 5.55))  # testing upper bound regular hours

    def test_overtime(self):
        self.assertEqual(335.5, calculate_pay(50.5, 5.5))  # testing overtime regular hours





