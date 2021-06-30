# coding=utf-8


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        i = 0
        m, n = len(needle), len(haystack)
        while i <= n - m:
            if haystack[i:i+m] == needle:
                return i
            i += 1
        return -1
