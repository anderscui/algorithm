# coding=utf-8
import unittest

from leetcode.remove_duplicates_from_sorted_83.solution import Solution


class TestSolution(unittest.TestCase):
    def test_basic(self):
        s = Solution()

        head = s.buildList([1, 1, 2])
        deduped = s.deleteDuplicates(head)
        self.assertEqual(s.getValues(deduped), [1, 2])

        head = s.buildList([1, 1, 2, 3, 3])
        deduped = s.deleteDuplicates(head)
        self.assertEqual(s.getValues(deduped), [1, 2, 3])
