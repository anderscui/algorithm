# coding=utf-8
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        assert len(nums1) == (m + n)
        assert len(nums2) == n
        assert 0 <= m <= 200
        assert 0 <= n <= 200
        assert 0 <= m + n <= 200

        result = []

        i, j = 0, 0
        while i < m and j < n:
            n1 = nums1[i]
            n2 = nums2[j]
            if n1 <= n2:
                result.append(n1)
                i += 1
            else:
                result.append(n2)
                j += 1

        print(i, j)
        if j < n:
            result.extend(nums2[j:n])
        else:
            result.extend(nums1[i:m])

        nums1[:] = result[:]
