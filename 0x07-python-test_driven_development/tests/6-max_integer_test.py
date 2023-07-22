#!/usr/bin/python3
"""6-max_integer_test module."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define TestMaxInteger class."""

    def test_valid_input(self):
        """Test with valid input."""
        a = max_integer([1, 2, 3, 4])
        self.assertEqual(a, 4)

        b = max_integer([2, 3, 6, 1])
        self.assertEqual(b, 6)

    def test_invalid_input(self):
        """Test with invalid input. non-integers."""
        with self.assertRaises(TypeError):
            max_integer(2, '3', '9')

    def test_max_at_begining(self):
        """Test max at the begining of a list."""
        a = max_integer([10, 3, 7, 2])
        self.assertEqual(a, 10)

    def test_max_at_end(self):
        """Test when max is at the end of a list."""
        a = max_integer([2, 4, 3, 9])
        self.assertEqual(a, 9)

    def test_max_in_middle(self):
        """Test when the max num is in the middle of the list."""
        a = max_integer([2, 3, 10, 4, 9])
        self.assertEqual(a, 10)

    def test_one_negative_included(self):
        """Test when at least one negative is included in the list."""
        a = max_integer([2, -3, 6, 1])
        self.assertEqual(a, 6)

    def test_only_negatives(self):
        """Test when the list contains only negatives."""
        a = max_integer([-2, -20, -1, -100])
        self.assertEqual(a, -1)

    def test_one_element(self):
        """Test only one element in a list."""
        a = max_integer([10])
        self.assertEqual(a, 10)

    def test_empty_list(self):
        """Test an empty list."""
        a = max_integer([])
        self.assertEqual(a, None)


if __name__ == '__main__':
    unittest.main()
