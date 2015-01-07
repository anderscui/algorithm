class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        res = 0

        i = len(s) - 1
        pos = -1
        while i >= 0:
            pos += 1
            ch = s[i]
            val = (ord(ch) - ord('A') + 1) * (26 ** pos)
            res += val

            i -= 1

        return res