# coding=utf-8
import unittest

from commons.commons.iterable import merge_sorted_lists, is_unique


class TestUtils(unittest.TestCase):
    def test_merge_lists(self):
        l1 = [1, 3, 4]
        l2 = [2, 5, 6, 7]
        target = [None] * (len(l1) + len(l2))
        merge_sorted_lists(l1, l2, target)
        self.assertListEqual(list(range(1, 8)), target)

        l1 = []
        l2 = [1, 2, 3]
        target = [None] * (len(l1) + len(l2))
        merge_sorted_lists(l1, l2, target)
        self.assertListEqual(list(range(1, 4)), target)

        l1, l2, target = [], [], []
        merge_sorted_lists(l1, l2, target)
        self.assertListEqual([], target)

    def test_is_unique(self):
        self.assertTrue(is_unique([]))
        self.assertTrue(is_unique([1]))
        self.assertTrue(is_unique([1, 2]))
        self.assertTrue(is_unique(list(range(1, 100, 2))))
        self.assertFalse(is_unique([1, 2, 2]))
