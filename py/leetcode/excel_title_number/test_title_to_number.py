
from title_to_number import Solution

sln = Solution()
assert sln.titleToNumber('') == 0
assert sln.titleToNumber('A') == 1
assert sln.titleToNumber('B') == 2
assert sln.titleToNumber('Z') == 26
assert sln.titleToNumber('AA') == 27
assert sln.titleToNumber('AB') == 28

assert sln.titleToNumber('AAA') == 703
assert sln.titleToNumber('ABA') == 729