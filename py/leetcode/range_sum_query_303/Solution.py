class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.table = {}

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        # recursive: [i, j] = [i, j-1] + nums[j]
        end = j+1 if j != -1 else len(self.nums)
        print('calculating ({0}:{1})'.format(i, end))
        if not (i, end) in self.table:
            self.table[(i, end)] = sum(self.nums[i: end])
        return self.table[(i, end)]

