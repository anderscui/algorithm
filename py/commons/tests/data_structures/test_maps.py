# coding=utf-8
import unittest

from commons.structs.maps import MapBase, UnsortedTableMap, ChainHashMap, ProbeHashMap, TreeMap, AvlTreeMap


class TestMaps(unittest.TestCase):
    def _test_map(self, m: MapBase):
        self.assertTrue(m.is_empty())

        data = [('K', 2), ('B', 4), ('U', 2), ('V', 8), ('K', 9)]
        for k, v in data:
            m[k] = v

        self.assertEqual(4, len(m))
        self.assertEqual(4, m['B'])

        self.assertRaises(KeyError, lambda: m['X'])

        # get default
        self.assertIsNone(m.get('F'))
        self.assertEqual(5, m.get('F', 5))
        self.assertEqual(9, m.get('K', 5))

        # delete
        del m['V']
        self.assertEqual(3, len(m))
        m.pop('K')
        self.assertEqual(2, len(m))

        self.assertListEqual(['B', 'U'], sorted(m.keys()))
        self.assertListEqual([2, 4], sorted(m.values()))
        self.assertListEqual([('B', 4), ('U', 2)], sorted(m.items()))

        # setdefault
        m.setdefault('B', 1)
        self.assertEqual(4, m['B'])
        m.setdefault('A', 1)
        self.assertEqual(1, m['A'])

    def test_unsorted_table_map(self):
        self._test_map(UnsortedTableMap())

    def test_chain_hash_map(self):
        self._test_map(ChainHashMap())

    def test_probe_hash_map(self):
        self._test_map(ProbeHashMap())

    def test_tree_map(self):
        self._test_map(TreeMap())

    def test_avl_tree_map(self):
        self._test_map(AvlTreeMap())
