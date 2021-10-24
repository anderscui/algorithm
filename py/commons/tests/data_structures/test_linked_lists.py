# coding=utf-8
import unittest

from commons.structs.exceptions import EmptyContainerError
from commons.structs.linked_lists import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_linked_list(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())

        self.assertRaises(EmptyContainerError, linked_list.remove_first)

        items = list(range(10))
        for item in items:
            linked_list.add_last(item)
        self.assertEqual(len(items), len(linked_list))
        self.assertFalse(linked_list.is_empty())

        # index get
        self.assertEqual(items[-1], linked_list[len(items)-1])

        # remove
        self.assertEqual(items[0], linked_list.remove_first())
        self.assertEqual(len(items)-1, len(linked_list))

        values = []
        for _ in range(len(items)-1):
            values.append(linked_list.remove_first())
        self.assertTrue(linked_list.is_empty())
        self.assertListEqual(items[1:], values)

    def test_linked_list_add_first(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertTrue(linked_list.head is None and linked_list.tail is None)

        linked_list.add_first(1)
        self.assertFalse(linked_list.is_empty())
        self.assertTrue(linked_list.head is not None and linked_list.tail is not None)
        self.assertTrue(linked_list.head is linked_list.tail)

        linked_list.add_first(0)
        self.assertTrue(linked_list.head is not None and linked_list.tail is not None)
        self.assertTrue(linked_list.head is not linked_list.tail)

        linked_list.clear()
        self.assertTrue(linked_list.is_empty())
        self.assertTrue(linked_list.head is None and linked_list.tail is None)

        items = list(range(10))
        for item in items:
            linked_list.add_first(item)
        self.assertListEqual(list(reversed(items)), [val for val in linked_list])

    def test_linked_list_add_last(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertTrue(linked_list.head is None and linked_list.tail is None)

        linked_list.add_last(1)
        self.assertFalse(linked_list.is_empty())
        self.assertTrue(linked_list.head is not None and linked_list.tail is not None)
        self.assertTrue(linked_list.head is linked_list.tail)

        linked_list.add_last(2)
        self.assertTrue(linked_list.head is not None and linked_list.tail is not None)
        self.assertTrue(linked_list.head is not linked_list.tail)

        linked_list.clear()
        self.assertTrue(linked_list.is_empty())
        self.assertTrue(linked_list.head is None and linked_list.tail is None)

        items = list(range(10))
        for item in items:
            linked_list.add_last(item)
        self.assertListEqual(items, [val for val in linked_list])
