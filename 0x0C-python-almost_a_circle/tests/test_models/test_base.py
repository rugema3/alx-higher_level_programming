#!/usr/bin/python3
"""Defines unittests for base."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test case class for testing the Base class.
    """

    def setUp(self):
        """
        Set up method called before each test method.
        Resets the __nb_objects counter before each test.
        """
        Base._Base__nb_objects = 0

    def test_id_generation(self):
        """
        Test if id is correctly generated when not provided.
        Two instances are created, and their ids are checked.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)  # First instance should have id=1
        self.assertEqual(b2.id, 2)  # Second instance should have id=2

    def test_custom_id(self):
        """
        Test if custom id is correctly assigned when provided.
        An instance with a custom id is created, and its id is checked.
        """
        custom_id = 42
        b1 = Base(custom_id)
        self.assertEqual(b1.id, custom_id)

    def test_multiple_instances(self):
        """
        Test if id is correctly generated when creating multiple instances.
        Three instances are created, and their ids are checked.
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_to_json_string_empty_list(self):
        """Test to_json_string with an empty list."""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none_list(self):
        """Test to_json_string with None as the list."""
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_single_dict(self):
        """Test to_json_string with a list containing a single dictionary."""
        data = [{"id": 1, "name": "Alice"}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"id": 1, "name": "Alice"}]')

    def test_to_json_string_multiple_dicts(self):
        """Test to_json_string with a list containing multiple dictionaries."""
        data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        result = Base.to_json_string(data)
        expected = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
