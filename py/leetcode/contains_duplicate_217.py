# coding=utf-8
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) > len(set(nums))
        found = set()
        for n in nums:
            if n in found:
                return True
            found.add(n)
        return False


if __name__ == '__main__':
    sln = Solution()

    assert sln.containsDuplicate([1, 2, 3, 1])
    assert not sln.containsDuplicate([1, 2, 3, 4])
    assert sln.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
