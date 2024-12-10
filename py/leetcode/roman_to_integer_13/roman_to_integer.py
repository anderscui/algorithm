# coding=utf-8
class Solution:
    def romanToInt(self, s: str) -> int:
        sym_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        sym_combs = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        i = 0
        val = 0
        while i < len(s):
            if s[i] in 'IXC' and s[i:i+2] in sym_combs:
                val += sym_combs[s[i:i+2]]
                i += 2
            else:
                val += sym_map[s[i]]
                i += 1
        return val


if __name__ == '__main__':
    sln = Solution()
    assert sln.romanToInt('III') == 3
    assert sln.romanToInt('LVIII') == 58
    assert sln.romanToInt('MCMXCIV') == 1994
