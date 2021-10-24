# coding=utf-8
import unittest

from commons.sorting.sorting import merge_sort, quick_sort, \
    selection_sort, insertion_sort, bubble_sort, heap_sort


class TestSorting(unittest.TestCase):
    def get_small_num_list(self):
        return [85, 24, 63, 45, 17, 50, 31, 96, 50]

    def test_merge_sort(self):
        l = self.get_small_num_list()
        merge_sort(l)
        self.assertListEqual(sorted(l), l)

    def test_quick_sort(self):
        l = self.get_small_num_list()
        result = quick_sort(l)
        self.assertListEqual(sorted(l), result)

    def test_selection_sort(self):
        l = self.get_small_num_list()
        selection_sort(l)
        self.assertListEqual(sorted(l), l)

    def test_insertion_sort(self):
        l = self.get_small_num_list()
        insertion_sort(l)
        self.assertListEqual(sorted(l), l)

    def test_bubble_sort(self):
        l = self.get_small_num_list()
        bubble_sort(l)
        self.assertListEqual(sorted(l), l)

    def test_heap_sort(self):
        l = self.get_small_num_list()
        result = heap_sort(l)
        self.assertListEqual(sorted(l), result)
