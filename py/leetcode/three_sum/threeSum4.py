import datetime


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):

        num_calc = 0

        num = sorted(num)

        sln = []
        cnt = len(num)

        i = 0
        for i in range(cnt):
            a = num[i]

            for j in range(i + 1, cnt):
                b = num[j]

                for k in range(j + 1, cnt):
                    c = num[k]
                    s3 = a + b + c

                    num_calc += 1

                    if s3 == 0:
                        triplet = [a, b, c]
                        if len(sln) == 0 or triplet != sln[-1]:
                            sln.append(triplet)
                    elif s3 > 0:
                        break

        print(num_calc)
        return sln


if __name__ == '__main__':
    # S = [-1, 0, 1, 2, -1, -4]
    # solution = Solution()
    # print(solution.threeSum(S))
    #
    # S1 = [-1, 0, 2]
    # solution = Solution()
    # print(solution.threeSum(S1))
    #
    # S2 = [-1, 1]
    # solution = Solution()
    # print(solution.threeSum(S2))
    #
    # start = datetime.datetime.now()
    # S3 = [-13, 10, 11, -3, 8, 11, -4, 8, 12, -13, 5, -6, -4, -2, 12, 11, 7, -7, -3, 10, 12, 13, -3, -2, 6, -1, 14, 7
    #         , -13, 8, 14, -10, -4, 10, -6, 11, -2, -3, 4, -13, 0, -14, -3, 3, -9, -6, -9, 13, -6, 3, 1, -9, -6, 13, -4, -15
    #         , -11, -12, 7, -9, 3, -2, -12, 6, -15, -10, 2, -2, -6, 13, 1, 9, 14, 5, -11, -10, 14, -5, 11, -6, 6, -3, -8
    #         , -15, -13, -4, 7, 13, -1, -9, 11, -13, -4, -15, 9, -4, 12, -4, 1, -9, -5, 9, 8, -14, -1, 4, 14]
    # print(sorted(S3))
    # solution = Solution()
    # print(solution.threeSum(S3))
    # print(datetime.datetime.now() - start)

    # start = datetime.datetime.now()
    # S4 = [-9, 14, -7, -8, 9, 1, -10, -8, 13, 12, 6, 9, 3, -3, -15, -15, 1, 8, -7, -4, -6, 8, 2, -10, 8, 11, -15, 3, 0,
    #       -11, -1, -1, 10, 0, 6, 5, -14, 3, 12, -15, -7, -5, 9, 11, -1, 1, 3, -15, -5, 11, -12, -4, -4, -2, -6, -10, -6,
    #       -6, 0, 2, -9, 14, -14, -14, -9, -1, -2, -7, -12, -13, -15, -4, -3, 1, 14, 3, -12, 3, 3, -10, -9, -1, -7, 3,
    #       12, -6, 0, 13, 4, -15, 0, 2, 6, 1, 3, 13, 8, -13, 13, 11, 11, 13, 14, -6]
    # solution = Solution()
    # # print(solution.threeSum(S4))
    # print(datetime.datetime.now() - start)
    #
    # S5 = [1, 2, -2, -1]
    # print(sorted(S5))
    # solution = Solution()
    # print(solution.threeSum(S5))

    # S6 = [3, 0, -2, -1, 1, 2]
    # print(sorted(S6))
    # solution = Solution()
    # print(solution.threeSum(S6))

    start = datetime.datetime.now()
    S7 = [-5,14,1,-2,11,11,-10,3,-6,0,3,-4,-9,-13,-8,-7,9,8,-7,11,12,-7,4,-7,-1,-5,13,1,-2,8,-13,0,-1,3,13,-13,-1,10,5,1,-13,-15,12,-7,-13,-11,-7,3,13,1,0,2,1,11,10,8,-8,1,-14,-3,-6,-12,12,0,6,2,2,-9,-3,14,-1,-9,14,-4,-1,8,-8,7,-4,12,-14,3,-9,2,0,-13,-13,-1,3,-12,11,4,-9,8,11,5,-5,-10,3,-1,-11,-13,5,-12,-10,11,11,-3,-5,14,-13,-4,-5,-7,6,2,-13,0,8,-3,4,4,-14,2]
    # print(sorted(S7))
    solution = Solution()
    sln = solution.threeSum(S7)
    assert len(sln) == 466
    # print(solution.threeSum(S7))
    print(datetime.datetime.now() - start)