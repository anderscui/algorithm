import datetime


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        # num = sorted(num)
        sln = []
        cnt = len(num)
        for i in range(cnt):
            a = num[i]
            for j in range(i + 1, cnt):
                b = num[j]
                for k in range(i + 2, cnt):
                    c = num[k]
                    if a + b + c == 0:
                        triplet = sorted([a, b, c])
                        if triplet not in sln:
                            sln.append(triplet)
        return sln


if __name__ == '__main__':
    S = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.threeSum(S))

    S1 = [-1, 0, 2]
    solution = Solution()
    print(solution.threeSum(S1))

    S2 = [-1, 1]
    solution = Solution()
    print(solution.threeSum(S2))

    start = datetime.datetime.now()
    S3 = [-5,14,1,-2,11,11,-10,3,-6,0,3,-4,-9,-13,-8,-7,9,8,-7,11,12,-7,4,-7,-1,-5,13,1,-2,8,-13,0,-1,3,13,-13,-1,10,5,1,-13,-15,12,-7,-13,-11,-7,3,13,1,0,2,1,11,10,8,-8,1,-14,-3,-6,-12,12,0,6,2,2,-9,-3,14,-1,-9,14,-4,-1,8,-8,7,-4,12,-14,3,-9,2,0,-13,-13,-1,3,-12,11,4,-9,8,11,5,-5,-10,3,-1,-11,-13,5,-12,-10,11,11,-3,-5,14,-13,-4,-5,-7,6,2,-13,0,8,-3,4,4,-14,2]
    solution = Solution()
    print(solution.threeSum(S3))
    print(datetime.datetime.now() - start)