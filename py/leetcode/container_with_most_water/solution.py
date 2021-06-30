# coding=utf-8
from typing import List


class Solution:
    def maxArea0(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        n = len(height)
        max_area = 0
        for i in range(n):
            for j in range(i+1, n):
                cur_area = (j - i) * min(height[i], height[j])
                if cur_area > max_area:
                    max_area = cur_area
        return max_area

    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        max_area = 0
        l, r = 0, len(height) - 1
        while l < r < len(height):
            cur_area = (r - l) * min(height[l], height[r])
            if cur_area > max_area:
                max_area = cur_area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
