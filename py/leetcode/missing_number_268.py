# coding=utf-8
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = set(i for i in range(len(nums)+1))
        actual = set(nums)
        missing = expected - actual
        return list(missing)[0] if missing else -1


if __name__ == '__main__':
    sln = Solution()

    assert sln.missingNumber([3, 0, 1]) == 2
    assert sln.missingNumber([0, 1]) == 2
    assert sln.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
