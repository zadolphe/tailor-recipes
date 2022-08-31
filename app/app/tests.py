"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class  CalcTests(SimpleTestCase):
    "Test the calc module "

    def test_add_numbers(self):
        "test adding numbers together"
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        "subtracting numbers from each other"
        sub_result = calc.subtract(6, 4)

        self.assertEqual(sub_result, 2)
        