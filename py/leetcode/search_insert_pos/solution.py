# coding=utf-8
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return low
