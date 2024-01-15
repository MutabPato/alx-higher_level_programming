#!/usr/bin/python3
"""
A test file
"""


import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """
    Test base
    """

    def test_init_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string(self):
        data = [{'key': 'value'}, {'number': 42}]
        result = Base.to_json_string(data)
        expected_result = '[{"key": "value"}, {"number": 42}]'
        self.assertEqual(result, expected_result)

    def test_to_json_string_with_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

if __name__ == '__main__':
    unittest.main()
