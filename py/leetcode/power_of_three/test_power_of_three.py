from power_of_three import Solution

sln = Solution()
assert sln.isPowerOfThree(1)
assert sln.isPowerOfThree(3)
assert sln.isPowerOfThree(27)
assert sln.isPowerOfThree(3486784401)

assert not sln.isPowerOfThree(-1)
assert not sln.isPowerOfThree(0)
assert not sln.isPowerOfThree(6)
assert not sln.isPowerOfThree(135)
