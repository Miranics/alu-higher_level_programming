#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_list_with_duplicates(self):
        self.assertEqual(max_integer([1, 2, 2, 3, 3]), 3)

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_argument(self):
        self.assertIsNone(max_integer())

    def test_all_same_elements(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

if __name__ == '__main__':
    unittest.main()

