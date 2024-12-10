class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        # if x < 10:
        #     return True
        #
        # str_val = str(x)
        # n_digits = len(str_val)
        # for i in range(n_digits // 2 + 1):
        #     if str_val[i] != str_val[n_digits-1-i]:
        #         return False
        # return True

        reversed_val = 0
        remained = x
        while remained > 0:
            digit = remained % 10
            reversed_val = reversed_val * 10 + digit
            remained = remained // 10
        return reversed_val == x


def reverse_int(i: int):
    if i < 0:
        return None

    # i is positive
    reversed_val = 0
    remained = i
    while remained > 0:
        digit = remained % 10
        reversed_val = reversed_val * 10 + digit
        remained = remained // 10
    return reversed_val
