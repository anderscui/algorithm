class Solution:
    # @return an integer
    def atoi(self, str):

        # range def
        maxlen = 10
        maxint = 2147483647
        minint = -2147483648

        # strip
        s = str.strip()

        # empty
        if not s:
            return 0

        # sign
        sign = 1
        first = s[0]
        if first == '+':
            s = s[1:]
        elif first == '-':
            sign = -1
            s = s[1:]

        if not s or (not s[0].isdigit()):
            return 0

        end = 0
        for i in xrange(1, len(s)):
            if s[i].isdigit():
                end = i
            else:
                break
        s = s[:end+1]

        if len(s) > maxlen:
            if sign > 0:
                return maxint
            else:
                return minint
        else:
            fp = sign * float(s)
            if fp > maxint:
                return maxint
            elif fp < minint:
                return minint
            else:
                return int(fp)
