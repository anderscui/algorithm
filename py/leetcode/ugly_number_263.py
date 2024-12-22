# coding=utf-8


class Solution:
    def isUgly(self, n: int) -> bool:
        if n > 0:
            for p in (5, 3, 2):
                while n % p == 0:
                    n /= p
        return n == 1


if __name__ == '__main__':
    sln = Solution()

    assert sln.isUgly(1)
    assert sln.isUgly(6)
    assert not sln.isUgly(14)
