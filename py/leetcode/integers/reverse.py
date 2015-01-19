class Solution:
    # @return an integer
    def reverse(self, x):

        # range def
        maxint = 2147483647
        minint = -2147483648

        sign = 1
        if x < 0:
            sign = -1

        reversed_x = sign * float(str(abs(x))[::-1])
        print(reversed_x)

        if reversed_x > maxint or reversed_x < minint:
            return 0
        else:
            return int(reversed_x)