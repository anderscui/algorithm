import sys
from atoi import Solution

sln = Solution()
assert sln.atoi("0") == 0
assert sln.atoi("1") == 1
assert sln.atoi("10") == 10

assert sln.atoi("-1") == -1
assert sln.atoi("+123") == 123
assert sln.atoi("1.1") == 1

assert sln.atoi(" -0012a42") == -12
assert sln.atoi(" -0012.12") == -12

# invalid inputs
assert sln.atoi("") == 0
assert sln.atoi("  ") == 0
assert sln.atoi(" \t\b") == 0
assert sln.atoi("abc") == 0
assert sln.atoi("a123") == 0
assert sln.atoi("++1") == 0
assert sln.atoi("-+1") == 0

# range tests
assert sln.atoi("2147483647") == sys.maxint
assert sln.atoi("2147483648") == sys.maxint
assert sln.atoi("112147483648") == sys.maxint

assert sln.atoi("-2147483647") == (-sys.maxint)
assert sln.atoi("-2147483648") == (-sys.maxint - 1)
assert sln.atoi("-2147483650") == (-sys.maxint - 1)
assert sln.atoi("-214748365000") == (-sys.maxint - 1)



