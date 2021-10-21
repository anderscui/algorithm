# coding=utf-8
import unittest

from commons.texts.trie import Trie


class TestTries(unittest.TestCase):
    def _get_small_en_trie(self):
        trie = Trie()
        words = ['A', 'to', 'tea', 'ted', 'ten', 'i', 'in', 'inn']
        for word in words:
            trie[word] = word
        return trie

    def test_basic(self):
        trie = self._get_small_en_trie()
        assert 'tea' in trie
        assert 'a' not in trie
