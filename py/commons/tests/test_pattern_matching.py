# coding=utf-8
import time
import unittest

from commons.texts.pattern_matching import find_brute_force, find_boyer_moore, find_kmp


class TestPatternMatching(unittest.TestCase):
    def test_brute_force(self):
        t = 'hello world'
        self.assertEqual(6, find_brute_force(t, 'world'))
        self.assertEqual(-1, find_brute_force(t, 'xor'))

        # empty pattern
        self.assertEqual(0, find_brute_force('', ''))
        self.assertEqual(0, find_brute_force('a', ''))

        # empty text
        self.assertEqual(-1, find_brute_force('', 'a'))

    def test_brute_force_performance(self):
        t = 'hello world' * 1000
        p = 'dlrow' * 100
        self.assertEqual(-1, find_brute_force(t, p))

        start = time.time()
        for _ in range(1000):
            _ = find_brute_force(t, p)
        elapsed = time.time() - start
        print(elapsed)

        self.assertEqual(-1, t.find(p))
        start = time.time()
        for _ in range(1000):
            _ = t.find(p)
        elapsed = time.time() - start
        print(elapsed)

    def test_boyer_moore(self):
        t = 'hello world'
        self.assertEqual(6, find_boyer_moore(t, 'world'))
        self.assertEqual(-1, find_boyer_moore(t, 'xor'))

        self.assertEqual(-1, find_boyer_moore('abbacd', 'daba'))
        self.assertEqual(2, find_boyer_moore('abbaba', 'baba'))

        # empty pattern
        self.assertEqual(0, find_boyer_moore('', ''))
        self.assertEqual(0, find_boyer_moore('a', ''))

        # empty text
        self.assertEqual(-1, find_boyer_moore('', 'a'))

    def test_boyer_moore_performance(self):
        t = 'hello world' * 1000
        p = 'dlrow' * 100
        self.assertEqual(-1, find_boyer_moore(t, p))

        start = time.time()
        for _ in range(1000):
            _ = find_boyer_moore(t, p)
        elapsed = time.time() - start
        print(elapsed)

        self.assertEqual(-1, t.find(p))
        start = time.time()
        for _ in range(1000):
            _ = t.find(p)
        elapsed = time.time() - start
        print(elapsed)

    def test_kmp(self):
        t = 'hello world'
        self.assertEqual(6, find_kmp(t, 'world'))
        self.assertEqual(-1, find_kmp(t, 'xor'))

        self.assertEqual(-1, find_kmp('abbacd', 'daba'))
        self.assertEqual(2, find_kmp('abbaba', 'baba'))

        # empty pattern
        self.assertEqual(0, find_kmp('', ''))
        self.assertEqual(0, find_kmp('a', ''))

        # empty text
        self.assertEqual(-1, find_kmp('', 'a'))

    def test_kmp_performance(self):
        t = 'ABC ABCDAB ABCDABCDABDE'
        p = 'ABCDABD'
        expected = 15
        self.assertEqual(expected, find_kmp(t, p))

        start = time.time()
        for _ in range(100000):
            _ = find_kmp(t, p)
        elapsed = time.time() - start
        print(elapsed)

        self.assertEqual(expected, t.find(p))
        start = time.time()
        for _ in range(100000):
            _ = t.find(p)
        elapsed = time.time() - start
        print(elapsed)
