# coding=utf-8
import unittest

from leetcode.longest_common_prefix.solution import Solution


class TestSolution(unittest.TestCase):
    def test_basic(self):
        s = Solution()

        strs = ['flower', 'flow', 'flight']
        self.assertEqual(s.longestCommonPrefix(strs), 'fl')

        strs = ['dog', 'racecar', 'car']
        self.assertEqual(s.longestCommonPrefix(strs), '')
