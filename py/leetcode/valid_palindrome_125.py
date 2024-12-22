# coding=utf-8


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while j > i and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    sln = Solution()

    s = "A man, a plan, a canal: Panama"
    assert sln.isPalindrome(s)

    s = "race a car"
    assert not sln.isPalindrome(s)

    s = ' \t'
    assert sln.isPalindrome(s)

    print(sln.isPalindrome(',.'))
