# coding=utf-8
import unittest

from leetcode.search_first_and_last_34.solution import Solution


class TestSolution(unittest.TestCase):
    def test_basic(self):
        s = Solution()

        nums, target = [5, 7, 7, 8, 8, 10], 8
        self.assertListEqual(s.searchRange(nums, target), [3, 4])

        nums, target = [5, 7, 7, 8, 8, 10], 6
        self.assertListEqual(s.searchRange(nums, target), [-1, -1])

        nums, target = [], 0
        self.assertListEqual(s.searchRange(nums, target), [-1, -1])
