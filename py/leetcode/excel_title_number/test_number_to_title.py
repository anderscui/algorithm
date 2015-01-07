
from number_to_title import Solution

sln = Solution()
assert sln.convertToTitle(0) == ''
assert sln.convertToTitle(1) == 'A'
assert sln.convertToTitle(2) == 'B'
assert sln.convertToTitle(26) == 'Z'

assert sln.convertToTitle(27) == 'AA'
assert sln.convertToTitle(28) == 'AB'

assert sln.convertToTitle(703) == 'AAA'
assert sln.convertToTitle(729) == 'ABA'
