# coding=utf-8
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i+1, min(n, i+k+1)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        found = {}
        for i in range(len(nums)):
            if nums[i] in found and abs(i - found[nums[i]]) <= k:
                return True
            found[nums[i]] = i
        return False


if __name__ == '__main__':
    sln = Solution()

    nums = [1, 2, 3, 1]
    k = 3
    assert sln.containsNearbyDuplicate(nums, k)

    nums = [1, 0, 1, 1]
    k = 1
    assert sln.containsNearbyDuplicate(nums, k)

    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    assert not sln.containsNearbyDuplicate(nums, k)

    nums = [99, 99]
    k = 2
    assert sln.containsNearbyDuplicate(nums, k)
