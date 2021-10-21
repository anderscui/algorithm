# coding=utf-8
import time
import unittest

from commons.searching.seqs import sequential_search, binary_search


class TestUtils(unittest.TestCase):
    def get_small_sorted_nums(self):
        return [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

    def test_sequential_search(self):
        s = self.get_small_sorted_nums()
        target = 50
        i = sequential_search(s, target)
        self.assertEqual(-1, i)

    def test_binary_search(self):
        s = self.get_small_sorted_nums()
        target = 50
        i = binary_search(s, target)
        self.assertEqual(-1, i)

    def test_search_performance(self):
        # should use a much larger list to compare.
        s = self.get_small_sorted_nums()
        target = 50

        n_times = 1000
        start = time.time()
        for _ in range(n_times):
            _ = sequential_search(s, target)
        print('sequential: ', time.time() - start)

        start = time.time()
        for _ in range(n_times):
            _ = binary_search(s, target)
        print('binary: ', time.time() - start)
