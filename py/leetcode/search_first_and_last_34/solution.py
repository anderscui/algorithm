# coding=utf-8
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                break
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        if nums[mid] == target:
            left = mid
            while left > 0 and nums[left-1] == target:
                left -= 1
            right = mid
            while right < len(nums) - 1 and nums[right+1] == target:
                right += 1
        else:
            left, right = -1, -1

        return [left, right]
