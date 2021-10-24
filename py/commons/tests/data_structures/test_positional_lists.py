# coding=utf-8
import unittest

from commons.structs.positional_lists import PositionalList


class TestLinkedList(unittest.TestCase):
    def test_positional_list(self):
        pl = PositionalList()
        self.assertTrue(pl.is_empty())

        p = pl.add_last(8)
        self.assertTrue(pl.first().node is p.node)

        q = pl.add_after(p, 5)
        self.assertTrue(pl.before(q).node is p.node)

        r = pl.add_before(q, 3)
        self.assertEqual(3, r.element())

        self.assertTrue(pl.after(p).node is r.node)
        self.assertIsNone(pl.before(p))

        s = pl.add_first(9)
        self.assertListEqual([9, 8, 3, 5], list(pl))

        self.assertEqual(5, pl.delete(pl.last()))
        self.assertListEqual([9, 8, 3], list(pl))

        pl.replace(p, 7)
        self.assertListEqual([9, 7, 3], list(pl))
