# coding=utf-8
import unittest

from leetcode.merge_sorted_array.solution import Solution


class TestSolution(unittest.TestCase):
    def test_left_right(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3

        s = Solution()
        s.merge(nums1, m, nums2, n)
        self.assertListEqual(nums1, [1, 2, 2, 3, 5, 6])
        self.assertListEqual(nums2, [2, 5, 6])

    def test_right_left(self):
        nums1 = [2, 5, 6, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3

        s = Solution()
        s.merge(nums1, m, nums2, n)
        self.assertListEqual(nums1, [1, 2, 2, 3, 5, 6])
        self.assertListEqual(nums2, [1, 2, 3])

    def test_empty_right(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0

        s = Solution()
        s.merge(nums1, m, nums2, n)
        self.assertListEqual(nums1, [1])
        self.assertListEqual(nums2, [])

    def test_empty_left(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1

        s = Solution()
        s.merge(nums1, m, nums2, n)
        self.assertListEqual(nums1, [1])
        self.assertListEqual(nums2, [1])

    def test_both_empty(self):
        nums1 = []
        m = 0
        nums2 = []
        n = 0

        s = Solution()
        s.merge(nums1, m, nums2, n)
        self.assertListEqual(nums1, [])
        self.assertListEqual(nums2, [])
