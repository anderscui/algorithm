# coding=utf-8
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []

        rows = [[1]]
        while len(rows) < numRows:
            last_row = rows[-1]
            new_elems = [last_row[i] + last_row[i+1] for i in range(len(last_row) - 1)]
            new_row = [1] + new_elems + [1]
            rows.append(new_row)

        return rows


if __name__ == '__main__':
    sln = Solution()

    expected = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    assert sln.generate(5) == expected

    assert sln.generate(1) == [[1]]
    assert sln.generate(2) == [[1], [1, 1]]
