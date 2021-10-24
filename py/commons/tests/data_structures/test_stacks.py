# coding=utf-8
import unittest

from commons.structs.exceptions import EmptyContainerError
from commons.structs.stacks import Stack, ArrayStack, LinkedListStack


class TestStacks(unittest.TestCase):
    def _test_stack(self, stack: Stack):
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

    def _test_stack_order(self, stack: Stack):
        self.assertTrue(stack.is_empty())

        items = list(range(10))
        for item in items:
            stack.push(item)

        values = []
        for _ in range(len(stack)):
            values.append(stack.pop())

        self.assertListEqual(list(reversed(items)), values)

    def test_array_stack(self):
        self._test_stack(ArrayStack())

    def test_array_stack_order(self):
        self._test_stack_order(ArrayStack())

    def test_linked_list_stack(self):
        self._test_stack(LinkedListStack())

    def test_linked_list_stack_order(self):
        self._test_stack_order(LinkedListStack())
