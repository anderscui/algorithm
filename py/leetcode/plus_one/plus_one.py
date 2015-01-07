class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):

        cur = len(digits) - 1
        carry = 1

        while carry > 0:

            if cur < 0:
                digits = [0] + digits
                cur = 0

            val = digits[cur] + carry
            if val > 9:
                val = 0
                carry = 1
            else:
                carry = 0
            digits[cur] = val

            cur -= 1

        return digits