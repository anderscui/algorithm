# coding=utf-8
from typing import List

from statsmodels.sandbox.distributions.sppatch import expect


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_col_zero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        first_col_zero = True
                    else:
                        matrix[0][j] = 0

        # print(first_col_zero)
        # print(matrix)

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(1, n):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(0, m):
                matrix[i][0] = 0


if __name__ == '__main__':
    sln = Solution()

    m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sln.setZeroes(m)
    expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    assert m == expected

    m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sln.setZeroes(m)
    expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    assert m == expected

    m = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
    # print(m)
    sln.setZeroes(m)
    expected = [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert m == expected
