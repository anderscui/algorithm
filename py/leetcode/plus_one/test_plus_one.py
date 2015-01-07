from plus_one import Solution

sln = Solution()
assert sln.plusOne([0]) == [1]
assert sln.plusOne([5]) == [6]
assert sln.plusOne([0, 9]) == [1, 0]
assert sln.plusOne([9]) == [1, 0]

assert sln.plusOne([0, 9, 9]) == [1, 0, 0]
assert sln.plusOne([9, 9]) == [1, 0, 0]