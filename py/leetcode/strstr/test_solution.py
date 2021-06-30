# coding=utf-8
import unittest

from leetcode.strstr.solution import Solution


class TestSolution(unittest.TestCase):
    def test_basic(self):
        s = Solution()

        haystack, needle = "hello", "ll"
        self.assertEqual(s.strStr(haystack, needle), 2)

        haystack, needle = "hello", "la"
        self.assertEqual(s.strStr(haystack, needle), -1)

        haystack, needle = "hello", ""
        self.assertEqual(s.strStr(haystack, needle), 0)

        haystack, needle = "", ""
        self.assertEqual(s.strStr(haystack, needle), 0)
