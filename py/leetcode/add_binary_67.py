# coding=utf-8


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        m, n = len(a), len(b)
        cnt = max(m, n)
        if n < m:
            b = '0' * (m-n) + b

        result = []
        carry = 0
        for i in range(cnt-1, -1, -1):
            o1 = int(a[i])
            o2 = int(b[i])
            val = o1 + o2 + carry
            cur_val = val % 2
            carry = val // 2
            result.append(str(cur_val))
        if carry > 0:
            result.append(str(carry))
        return ''.join(reversed(result))


if __name__ == '__main__':
    sln = Solution()

    assert sln.addBinary('11', '1') == '100'
    assert sln.addBinary('1010', '1011') == '10101'
