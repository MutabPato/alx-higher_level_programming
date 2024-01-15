#!/usr/bin/python3

"""
A unittest module
"""


import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """
    Test Rectangle
    """

    def test_init_with_values(self):
        rect = Rectangle(10, 20, 2, 3, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_init_defaults(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_area(self):
        rect = Rectangle(8, 4)
        self.assertEqual(rect.area(), 32)

    def test_display(self):
        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with self.assertLogs() as logs:
            rect.display()
        self.assertEqual(logs.output, [expected_output])

    def test_str(self):
        rect = Rectangle(5, 7, 1, 2, 3)
        expected_str = "[Rectangle] (3) 1/2 - 5/7"
        self.assertEqual(str(rect), expected_str)

    def test_update(self):
        rect = Rectangle(5, 5, 1, 1, 1)
        rect.update(2, 10, 20, 3, 4)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        rect = Rectangle(4, 6, 2, 1, 7)
        expected_dict = {'x': 2, 'y': 1, 'width': 4, 'height': 6, 'id': 7}
        self.assertEqual(rect.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
