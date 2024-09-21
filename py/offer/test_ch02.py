# coding=utf-8
import unittest

from offer.ch02 import *
from offer.commons import *


class TestCh02(unittest.TestCase):
    def test_str2int(self):
        matrix = [[1, 2, 8, 9],
                  [2, 4, 9, 12],
                  [4, 7, 10, 13],
                  [6, 8, 11, 15]]
        self.assertTrue(find_in_sorted_matrix(matrix, 7))
        self.assertTrue(find_in_sorted_matrix(matrix, 1))
        self.assertTrue(find_in_sorted_matrix(matrix, 15))
        self.assertFalse(find_in_sorted_matrix(matrix, 20))

    def test_reverse_linked_list(self):
        values = [1, 2, 3, 4, 5]
        l = build_int_linked_list(values)
        reversed_l = list(reverse_linked_list(l))
        self.assertListEqual(list(reversed(values)), reversed_l)

        values = []
        l = build_int_linked_list(values)
        self.assertTrue(len(list(reverse_linked_list(l))) == 0)

        reversed_l = list(reverse_linked_list_recursively(l))
        self.assertListEqual(list(reversed(values)), reversed_l)

    def test_rebuild_binary_tree(self):
        preorder = [1, 2, 4, 7, 3, 5, 6, 8]
        inorder = [4, 7, 2, 1, 5, 3, 8, 6]
        rebuilt = rebuild_binary_tree(preorder, inorder)
        print(rebuilt)
