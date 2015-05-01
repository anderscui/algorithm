
from palindrome_num import Solution

sln = Solution()
assert sln.isPalindrome(0)
assert sln.isPalindrome(1)
assert sln.isPalindrome(33)
assert sln.isPalindrome(121)
assert sln.isPalindrome(1221)

assert not sln.isPalindrome(1000021)

# negative
assert not sln.isPalindrome(-1)

