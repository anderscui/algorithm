# coding=utf-8
import sys
from array import array

import unittest


class TestArrays(unittest.TestCase):
    def test_array_usage(self):
        data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] * 100

        # use compact array
        primes = array('i', data)
        print(primes)
        # 4064: 64 + 1000 * 4, each type uses extra 64 bytes.
        self.assertEqual(4064, sys.getsizeof(primes))

        # use built-in list
        primes2 = list(data)
        print(primes2)
        self.assertEqual(8056, sys.getsizeof(primes2))

    def test_dynamic_list(self):
        data = []
        n = 1000
        previous_size = 0
        for i in range(n):
            length = len(data)
            size = sys.getsizeof(data)
            if size != previous_size:
                print(f'length: {length}, size: {size}')
            previous_size = size
            data.append(None)
