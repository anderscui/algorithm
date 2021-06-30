# coding=utf-8
import unittest

from leetcode.swap_nodes_in_pairs_24.solution import Solution


class TestSolution(unittest.TestCase):
    def test_basic(self):
        s = Solution()

        head = s.buildPairs([1, 2, 3, 4])
        s.showPairs(head)
        swapped = s.swapPairs(head)
        s.showPairs(swapped)
        self.assertListEqual(s.getValues(swapped), [2, 1, 4, 3])

        head = s.buildPairs([1, 2, 3, 4, 5, 6])
        swapped = s.swapPairs(head)
        self.assertListEqual(s.getValues(swapped), [2, 1, 4, 3, 6, 5])

        head = s.buildPairs([1, 2, 3, 4, 5])
        swapped = s.swapPairs(head)
        self.assertListEqual(s.getValues(swapped), [2, 1, 4, 3, 5])

        head = s.buildPairs([1])
        swapped = s.swapPairs(head)
        self.assertListEqual(s.getValues(swapped), [1])

        head = s.buildPairs([])
        swapped = s.swapPairs(head)
        self.assertListEqual(s.getValues(swapped), [])
