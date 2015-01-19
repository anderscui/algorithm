class Solution:
    # @return a string
    def convert(self, s, nRows):

        section_size = 2 * nRows - 2
        remainder = len(s) % section_size
        if remainder:
            s += ' ' * (section_size - remainder)
        n_section = len(s) / section_size

        newstr = ''
        start = 0
        sep = ' ' * ((nRows-1) / 2)
        for i in xrange(n_section):
            newstr += s[start:start+nRows] + sep + s[start+nRows] + sep
            start += section_size

        res = ''
        for i in xrange(nRows):
            for j in xrange(n_section):
                if newstr[nRows * j + i] != ' ':
                    res += newstr[nRows * j + i]
        return res