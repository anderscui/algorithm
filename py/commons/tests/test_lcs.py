# coding=utf-8
import unittest

from commons.dynamic_programming.lcs import lcs_lens, lcs, lcs_brute_force, is_sub


class TestLcs(unittest.TestCase):
    def test_lcs_len_table(self):
        s = 'ABCBDAB'
        t = 'BDCABA'
        result = lcs_lens(s, t)
        # print(result)
        self.assertEqual(4, result[len(s)][len(t)])

    def test_lcs(self):
        self.assertEqual('BCBA', lcs('ABCBDAB', 'BDCABA'))
        self.assertEqual('AGACG', lcs('TAGTCACG', 'AGACTGTC'))

    def test_lcs_brute_force(self):
        self.assertEqual('BCBA', lcs_brute_force('ABCBDAB', 'BDCABA'))
        self.assertEqual('AGACG', lcs_brute_force('TAGTCACG', 'AGACTGTC'))

    def test_is_sub(self):
        self.assertTrue(is_sub('ABCBDAB', ''))
        self.assertTrue(is_sub('ABCBDAB', 'BCBA'))
        self.assertFalse(is_sub('ABCBDAB', 'BCBAD'))
