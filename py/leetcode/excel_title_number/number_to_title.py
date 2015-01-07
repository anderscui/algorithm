class Solution:
    # @return a string
    def convertToTitle(self, num):
        s = []
        i = num
        while i > 0:
            digit = (i - 1) % 26 + ord('A')
            s = [chr(digit)] + s
            i = (i - 1) / 26

        return ''.join(s)