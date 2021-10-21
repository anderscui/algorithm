# coding=utf-8
import unittest

from commons.dynamic_programming.matrices import matrix_chain


class TestMatrices(unittest.TestCase):
    def test_matrix_chain(self):
        # (AB)C < A(BC)
        d = (2, 10, 50, 20)
        result = matrix_chain(d)
        self.assertEqual(3000, result[0][-1])
