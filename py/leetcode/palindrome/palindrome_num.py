class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        if x < 10:
            return True

        lowest = x % 10
        less = x / 10

        highest = less
        p = 0
        while highest >= 10:
            highest /= 10
            p += 1
        less -= highest * (10 ** p)

        return (lowest == highest) and self.isPalindrome(less)
