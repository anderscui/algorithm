# coding=utf-8
import unittest

from commons.structs.exceptions import EmptyContainerError
from commons.structs.queues import ArrayQueue


class TestQueues(unittest.TestCase):
    def test_array_queue(self):
        queue = ArrayQueue()
        self.assertTrue(queue.is_empty())

        self.assertRaises(EmptyContainerError, queue.first)

        items = list(range(10))
        for item in items:
            queue.enqueue(item)
        self.assertEqual(len(items), len(queue))
        self.assertFalse(queue.is_empty())

        self.assertEqual(items[0], queue.first())
        self.assertEqual(items[0], queue.dequeue())
        self.assertEqual(items[1], queue.first())
        self.assertEqual(len(items) - 1, len(queue))

    def test_array_queue_order(self):
        queue = ArrayQueue()
        items = list(range(10))
        for item in items:
            queue.enqueue(item)

        values = []
        for _ in range(len(queue)):
            values.append(queue.dequeue())

        self.assertListEqual(items, values)
