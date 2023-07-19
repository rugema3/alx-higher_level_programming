#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from tests.test_models.test_base import TestBase  # Importing tests of the base class here.

class TestRectangle(unittest.TestCase):
    """Test case class for testing the Rectangle class."""
    
    def test_attributes_present(self):
        """Test when all arguments are present."""
        b = Rectangle(4, 5, 10, 20, 1)
        self.assertIsNotNone(b.width)
        self.assertIsNotNone(b.height)
        self.assertIsNotNone(b.x)
        self.assertIsNotNone(b.y)
        self.assertIsNotNone(b.id)


    def test_attribute_absent(self):
        """Test when no argument provided at all."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_argument(self):
        """Test only one argument."""
        with self.assertRaises(TypeError):
            Rectangle(4)

    def test_two_arguments(self):
        """Test two arguments."""
        b = Rectangle(4, 5)
        self.assertEqual(b.width, 4)
        self.assertEqual(b.height, 5)
        self.assertEqual(b.x, 0)
        self.assertEqual(b.y, 0)
        self.assertIsNotNone(b.id)

    def test_three_arguments(self):
        """Test case when only 3 arguments are provides.
        By default, the x and y values should be zero.
        Also the value of id should not be empty.
        """
        b = Rectangle(4, 5, 10)
        self.assertEqual(b.width, 4)
        self.assertEqual(b.height, 5)
        self.assertEqual(b.x, 10)
        self.assertEqual(b.y, 0)
        self.assertIsNotNone(b.id)

    def test_four_arguments(self):
        """Test four arguments."""
        b = Rectangle(4, 5, 6, 7)
        self.assertEqual(b.width, 4)
        self.assertEqual(b.height, 5)
        self.assertEqual(b.x, 6)
        self.assertEqual(b.y, 7)
        self.assertIsNotNone(b.id)

    def test_excess_arguments(self):
        """Test excess arguments.
        We are testing when the arguments are more than 5. 
        We are only allowed to work with 5 arguments according
        to the definition of our class.
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_non_int_width(self):
        """Test when a non-integer is parssed as an argument."""
        with self.assertRaises(TypeError):
            Rectangle('2', 2, 4)

        with self.assertRaises(NameError):
            Rectangle(width, 3, 5, 5)


    def test_non_int_height(self):
        """Test when the height value is not an integer."""
        with self.assertRaises(TypeError):
            Rectangle(2, '2', 4)

        with self.assertRaises(NameError):
            Rectangle(2, height, 4)

    def test_float(self):
        """Test float width or height."""
        with self.assertRaises(TypeError):
            Rectangle(2.3, 4, 4)

        with self.assertRaises(TypeError):
            Rectangle(2, 3.5, 5)

    def test_zero_width_and_height(self):
        """Test when either height or width is zero."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 4)

        with self.assertRaises(ValueError):
            Rectangle(2, 0, 4)

        with self.assertRaises(ValueError):
            Rectangle(0, 0, 2, 4)

    def test_negative_width_or_height(self):
        """Test when either width or height is less than zero."""

        with self.assertRaises(ValueError):
            Rectangle(-2, 3, 8)

        with self.assertRaises(ValueError):
            Rectangle(2, -3, 4)

    def test_x_or_y_negative(self):
        """Test when either x or y is negative."""
        with self.assertRaises(ValueError):
            Rectangle(2, 3, -2, 3)

        with self.assertRaises(ValueError):
            Rectangle(2, 3, 4, -3)

    def test_custom_id(self):
        """Test a custom_id."""
        custom_id = 42
        r = Rectangle(5, 7, 7, 5, custom_id)
        self.assertEqual(r.id, custom_id)

    def test_width_getter(self):
        """Test the wedth getter."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(1, r.width)

    def test_width_setter(self):
        """Test the width setter."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 20
        self.assertEqual(20, r.width)


    def test_height_getter(self):
        """Test the height getter."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)


    def test_height_setter(self):
        """Test the height setter."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        """Test the x getter."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        """Test the x setter."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        """Test the y getter."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        """Test the y setter."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.y = 20
        self.assertEqual(20, r.y)




if __name__ == '__main__':
    unittest.main()

