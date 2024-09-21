# coding=utf-8
import unittest

from offer.ch01 import *
from offer.commons import build_int_linked_list


class TestCh01(unittest.TestCase):
    def test_str2int(self):
        self.assertIsNone(str2int(None))
        self.assertIsNone(str2int(''))

        self.assertEqual(0, str2int('0'))
        self.assertEqual(1, str2int('1'))
        self.assertEqual(123, str2int('123'))
        self.assertEqual(123, str2int('00123'))

        self.assertEqual(-123, str2int('-123'))

    def test_find_kth_to_tail(self):
        l = build_int_linked_list([1, 2, 3, 4, 5])

        self.assertEqual(5, find_kth_to_tail(l, 1).value)
        self.assertEqual(3, find_kth_to_tail(l, 3).value)
        self.assertEqual(1, find_kth_to_tail(l, 5).value)
        self.assertIsNone(find_kth_to_tail(l, 0))
        self.assertIsNone(find_kth_to_tail(l, -1))
        self.assertRaises(ValueError, lambda: find_kth_to_tail(l, 6))
