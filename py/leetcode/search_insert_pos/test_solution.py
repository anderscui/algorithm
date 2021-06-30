# coding=utf-8
import unittest

from leetcode.search_insert_pos.solution import Solution


class TestSolution(unittest.TestCase):
    def test_basic(self):
        s = Solution()

        nums, target = [1, 3, 5, 6], 5
        self.assertEqual(s.searchInsert(nums, target), 2)

        nums, target = [1, 3, 5, 6], 2
        self.assertEqual(s.searchInsert(nums, target), 1)

        nums, target = [1, 3, 5, 6], 7
        self.assertEqual(s.searchInsert(nums, target), 4)

        nums, target = [1, 3, 5, 6], 0
        self.assertEqual(s.searchInsert(nums, target), 0)

        nums, target = [1], 0
        self.assertEqual(s.searchInsert(nums, target), 0)

        nums, target = [], 0
        self.assertEqual(s.searchInsert(nums, target), 0)
