
from comp_version_num import Solution

sln = Solution()
assert sln.compareVersion('0.1', '1.1') == -1
assert sln.compareVersion('1.1', '1.2') == -1
assert sln.compareVersion('1.2', '13.37') == -1

assert sln.compareVersion('0.1', '0.1') == 0
assert sln.compareVersion('1.2', '1.1') == 1

assert sln.compareVersion('1.2', '1.1.2') == 1
assert sln.compareVersion('1.2', '1.2.1') == -1
assert sln.compareVersion('1.5', '1.10') == -1

assert sln.compareVersion('1', '1.1') == -1
assert sln.compareVersion('1', '1.0') == 0
assert sln.compareVersion('1.0.0', '1.0') == 0
