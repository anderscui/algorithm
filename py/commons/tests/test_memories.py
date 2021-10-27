# coding=utf-8
import sys
import unittest
from queue import PriorityQueue


class TestTries(unittest.TestCase):
    def test_ref_counts(self):
        pq = PriorityQueue()
        self.assertEqual(2, sys.getrefcount(pq))
