# coding=utf-8
import unittest

from commons.structs.exceptions import EmptyContainerError
from commons.structs.stacks import ArrayStack


class TestStacks(unittest.TestCase):
    def test_array_stack(self):
        stack = ArrayStack()
        self.assertTrue(stack.is_empty())

        self.assertRaises(EmptyContainerError, stack.top)

        items = list(range(10))
        for item in items:
            stack.push(item)
        self.assertEqual(len(items), len(stack))
        self.assertFalse(stack.is_empty())

        self.assertEqual(items[-1], stack.top())

        self.assertEqual(items[-1], stack.pop())
        self.assertEqual(items[-2], stack.top())
        self.assertEqual(len(items) - 1, len(stack))

    def test_array_stack_order(self):
        stack = ArrayStack()
        items = list(range(10))
        for item in items:
            stack.push(item)

        values = []
        for _ in range(len(stack)):
            values.append(stack.pop())

        self.assertListEqual(list(reversed(items)), values)


