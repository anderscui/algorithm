# coding=utf-8
import unittest

from commons.structs.arrays import DynamicArray


class TestDynamicArrays(unittest.TestCase):
    def test_dynamic_array(self):
        array = DynamicArray()

        self.assertTrue(array.is_empty())

        for i in range(1, 6):
            array.append(i)

        self.assertFalse(array.is_empty())
        # size and capacity
        self.assertEqual(5, len(array))
        self.assertEqual(8, array.capacity)

        # contains
        self.assertIn(3, array)
        self.assertNotIn(6, array)

        # it's iterable for the presence of `__len__` and `__getitem__`?
        self.assertListEqual(list(range(1, 6)), [i for i in array])

        # set item
        array[len(array)-1] = 5

        # array: [1, 2, 3, 4, 5]
        self.assertListEqual([2], array[1:2])
        self.assertListEqual([2, 4], array[1::2])
        self.assertListEqual([3, 4, 5], array[2::])
        self.assertListEqual([1, 2], array[:2])
        self.assertListEqual([3, 4, 5], array[2:])
        self.assertListEqual([], array[2:1])

        i = array.find(3)
        self.assertEqual(2, i)

        # insert
        array.insert(i, 6)
        self.assertListEqual([1, 2, 6, 3, 4, 5], list(array))

        array.insert(len(array), 7)
        self.assertListEqual([1, 2, 6, 3, 4, 5, 7], list(array))

        # pop
        val = array.pop()
        self.assertTrue(7, val)
        self.assertListEqual([1, 2, 6, 3, 4, 5], list(array))

        self.assertRaises(IndexError, DynamicArray().pop)

        # remove
        i = array.remove(6)
        self.assertEqual(2, i)
        self.assertListEqual([1, 2, 3, 4, 5], list(array))

        self.assertRaises(ValueError, lambda: array.remove(10))
