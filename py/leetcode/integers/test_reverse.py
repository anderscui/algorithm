from reverse import Solution

sln = Solution()

assert sln.reverse(0) == 0
assert sln.reverse(1) == 1
assert sln.reverse(123) == 321

assert sln.reverse(-123) == -321

# zeros
assert sln.reverse(1000) == 1
assert sln.reverse(-1000) == -1

# overflow
assert sln.reverse(2147483647) == 0
assert sln.reverse(1000000003) == 0

assert sln.reverse(-2147483647) == 0
assert sln.reverse(-1000000003) == 0