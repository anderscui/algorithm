# coding=utf-8
import unittest

from commons.structs.exceptions import EmptyContainerError
from commons.structs.positional_lists import PositionalList
from commons.structs.priority_queues import UnsortedPriorityQueue, SortedPriorityQueue, HeapPriorityQueue


class TestPriorityQueues(unittest.TestCase):
    def test_priority_queue(self, queue):

        if queue.is_empty():
            queue.add(5, 'A')
            queue.add(9, 'C')
            queue.add(3, 'B')
            queue.add(7, 'D')

        self.assertEqual(4, len(queue))
        self.assertEqual((3, 'B'), queue.min())

        self.assertEqual((3, 'B'), queue.remove_min())
        self.assertEqual((5, 'A'), queue.remove_min())
        self.assertEqual(2, len(queue))

        self.assertEqual((7, 'D'), queue.remove_min())
        self.assertEqual((9, 'C'), queue.remove_min())
        self.assertTrue(queue.is_empty())

        self.assertRaises(EmptyContainerError, queue.min)
        self.assertRaises(EmptyContainerError, queue.remove_min)

    def test_unsorted_priority_queue(self):
        self.test_priority_queue(UnsortedPriorityQueue())

    def test_sorted_priority_queue(self):
        self.test_priority_queue(SortedPriorityQueue())

    def test_heap_priority_queue(self):
        self.test_priority_queue(HeapPriorityQueue())

    def test_heap_priority_queue_heapify(self):
        queue = HeapPriorityQueue([(5, 'A'), (9, 'C'), (3, 'B'), (7, 'D')])
        self.test_priority_queue(queue)
