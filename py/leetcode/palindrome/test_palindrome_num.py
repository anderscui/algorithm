from leetcode.palindrome.palindrome_num import Solution, reverse_int

sln = Solution()
assert sln.isPalindrome(0)
assert sln.isPalindrome(1)
assert sln.isPalindrome(33)
assert sln.isPalindrome(121)
assert sln.isPalindrome(1221)

assert not sln.isPalindrome(1000021)

# negative
assert not sln.isPalindrome(-1)


assert reverse_int(-1) is None
assert reverse_int(0) == 0
assert reverse_int(10) == 1
assert reverse_int(10) == 1
assert reverse_int(33) == 33
assert reverse_int(121) == 121
assert reverse_int(1000021) == 1200001
