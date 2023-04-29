"""
Sample Tests
"""


from django.test import SimpleTestCase

from app import calc


class ClassTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        expected = 2

        res = calc.add(1, 1)

        self.assertEqual(expected, res)

    def test_subtract_numbers(self):
        numOne, numTwo = 1, 2

        expected = numTwo - numOne

        res = calc.subtract(numTwo, numOne)

        self.assertEqual(res, expected)
