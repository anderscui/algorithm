# coding=utf-8
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        if m != n:
            return False

        # check rows
        for i in range(m):
            row = board[i]
            digits = [elem for elem in row if elem != '.']
            if len(digits) != len(set(digits)):
                return False

        # check cols
        for j in range(n):
            col = [board[i][j] for i in range(m)]
            digits = [elem for elem in col if elem != '.']
            if len(digits) != len(set(digits)):
                return False

        # check sub-boards
        sub_m, sub_n = 3, 3
        for sub_i in range(sub_m):
            for sub_j in range(sub_n):
                sub_top_i, sub_top_j = sub_i * sub_m, sub_j * sub_n
                sub_box = [board[sub_top_i+i][sub_top_j+j] for i in range(sub_m) for j in range(sub_n)]
                digits = [elem for elem in sub_box if elem != '.']
                if len(digits) != len(set(digits)):
                    return False

        return True


if __name__ == '__main__':
    sln = Solution()

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert sln.isValidSudoku(board)

    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert not sln.isValidSudoku(board)
