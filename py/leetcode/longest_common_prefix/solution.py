# coding=utf-8
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        min_len = min([len(s) for s in strs])
        i = 0
        while i <= min_len - 1 and len(set(s[i] for s in strs)) == 1:
            i += 1
        return strs[0][:i]
