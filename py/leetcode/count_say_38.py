# coding=utf-8
from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        parts = []
        for g in groupby(self.countAndSay(n-1)):
            g_ch = g[0]
            g_len = len(list(g[1]))
            parts.append(f'{g_len}{g_ch}')
        return ''.join(parts)


if __name__ == '__main__':
    sln = Solution()

    assert sln.countAndSay(1) == '1'
    assert sln.countAndSay(2) == '11'
    assert sln.countAndSay(3) == '21'
    assert sln.countAndSay(4) == '1211'
    assert sln.countAndSay(5) == '111221'
    print(sln.countAndSay(30))
