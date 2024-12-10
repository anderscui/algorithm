# coding=utf-8
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # unique_vals = sorted(set(nums))
        # nums[:len(unique_vals)] = unique_vals
        # return len(unique_vals)

        if not nums:
            return 0

        cur_val = nums[0]
        cur_pos = 1
        for i in range(1, len(nums)):
            if nums[i] == cur_val:
                continue

            nums[cur_pos] = nums[i]
            cur_pos += 1
            cur_val = nums[i]
        return cur_pos


if __name__ == '__main__':
    sln = Solution()

    nums = [1, 1, 2]
    n_unique = sln.removeDuplicates(nums)
    assert n_unique == 2
    assert nums[:n_unique] == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    n_unique = sln.removeDuplicates(nums)
    assert n_unique == 5
    assert nums[:n_unique] == [0, 1, 2, 3, 4]
