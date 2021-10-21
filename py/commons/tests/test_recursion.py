# coding=utf-8
import unittest

from commons.recursion.basic import factorial, draw_ruler, disk_usage


class TestUtils(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(1, factorial(0))
        self.assertEqual(1, factorial(1))
        self.assertEqual(120, factorial(5))

    def test_draw_ruler(self):
        draw_ruler(3, 3)

    def test_disk_usage(self):
        disk_usage('/Users/andersc/Downloads/books')
