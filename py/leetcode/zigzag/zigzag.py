class Solution:
    # @return a string
    def convert(self, s, nRows):

        if not s:
            return s

        if nRows <= 1:
            return s

        rows = nRows
        section_size = 2 * rows - 2

        final = ''
        for i in xrange(rows):
            if i == 0 or i == (rows-1):
                j = i
                while j < len(s):
                    final += s[j]
                    j += section_size
            else:
                j = i
                flag = True
                larger_step = 2 * (rows - 1 - i)
                small_step = section_size - larger_step
                while j < len(s):
                    final += s[j]
                    if flag:
                        j += larger_step
                    else:
                        j += small_step
                    flag = not flag

        return final