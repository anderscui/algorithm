# coding=utf-8


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # words = s.rsplit(maxsplit=1)
        # return len(words[-1]) if words else 0
        n = len(s)
        for i in range(n-1, -1, -1):
            if s[i] == ' ':
                continue
            j = i - 1
            while j >= 0 and s[j] != ' ':
                j -= 1
            return i - j
        return 0


if __name__ == '__main__':
    sln = Solution()

    s = 'Hello World'
    assert sln.lengthOfLastWord(s) == 5

    s = '   fly me   to   the moon  '
    assert sln.lengthOfLastWord(s) == 4

    s = 'luffy is still joyboy'
    assert sln.lengthOfLastWord(s) == 6
