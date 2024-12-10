# coding=utf-8
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m, n = len(matrix), len(matrix[0])
        # # local row
        # low, high = 0, m - 1
        # # mid = (low + high) // 2 # 不需要，按题目假设，下面 mid 必有值
        # # high - low >= 2，至少有三个元素，该循环不会结束，因此只要考虑1、2的情况
        # while low <= high:
        #     mid = (low + high) // 2
        #     if matrix[mid][0] == target:
        #         return True
        #     elif matrix[mid][0] > target:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        # # 上面循环停止时，必有 high < mid，此时应在 mid - 1 行；否则应在 mid 行
        # row_index = mid - 1 if high < mid else mid
        # if row_index < 0 or row_index >= m:
        #     return False
        #
        # row = matrix[row_index]
        # low, high = 0, len(row) - 1
        # while low <= high:
        #     mid = (low + high) // 2
        #     if row[mid] == target:
        #         return True
        #     elif row[mid] > target:
        #         high -= 1
        #     else:
        #         low += 1
        # return False

        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) // 2
            row, col = mid // n, mid % n
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                low = mid + 1
            else:
                high = mid - 1
        return False


if __name__ == '__main__':
    sln = Solution()

    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert sln.searchMatrix(m, 1)
    assert sln.searchMatrix(m, 3)
    assert sln.searchMatrix(m, 20)
    assert sln.searchMatrix(m, 23)
    assert sln.searchMatrix(m, 60)

    assert not sln.searchMatrix(m, 13)
    assert not sln.searchMatrix(m, -10)
    assert not sln.searchMatrix(m, 100)
