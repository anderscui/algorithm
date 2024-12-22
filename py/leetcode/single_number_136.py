# coding=utf-8
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # found = set()
        # for n in nums:
        #     if n not in found:
        #         found.add(n)
        #     else:
        #         found.remove(n)
        # return list(found)[0]
        result = 0
        for n in nums:
            result ^= n
        return result


if __name__ == '__main__':
    sln = Solution()

    assert sln.singleNumber([2, 2, 1]) == 1
    assert sln.singleNumber([4, 1, 2, 1, 2]) == 4
    assert sln.singleNumber([1]) == 1
