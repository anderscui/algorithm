from collections import defaultdict
import datetime


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):

        num_calc = 0

        num = sorted(num)

        sln = []
        cnt = len(num)

        calculated_a = defaultdict(bool)
        upper = cnt
        i = 0
        while i < upper:
            a = num[i]
            if calculated_a[a]:
                # i += 1
                # continue
                print(a, 'calculated')

            print(a)
            j = i + 1
            upper2 = cnt

            while j < upper2:
                b = num[j]
                s2 = a + b

                last = num[upper2 - 1]
                if (s2 + last) < 0:
                    j += 1
                    continue

                for k in range(j + 1, cnt):
                    c = num[k]
                    s3 = s2 + c
                    num_calc += 1
                    if s3 == 0:
                        triplet = [a, b, c]
                        if len(sln) == 0 or triplet != sln[-1]:
                            sln.append(triplet)
                    elif s3 > 0:
                        upper = k
                        upper2 = k
                        # print(sln)
                        # print(a, b, c)
                        break

                j += 1

            calculated_a[a] = True
            i += 1

        print(num_calc)
        return sln


if __name__ == '__main__':
    start = datetime.datetime.now()
    S = [-5,14,1,-2,11,11,-10,3,-6,0,3,-4,-9,-13,-8,-7,9,8,-7,11,12,-7,4,-7,-1,-5,13,1,-2,8,-13,0,-1,3,13,-13,-1,10,5,1,-13,-15,12,-7,-13,-11,-7,3,13,1,0,2,1,11,10,8,-8,1,-14,-3,-6,-12,12,0,6,2,2,-9,-3,14,-1,-9,14,-4,-1,8,-8,7,-4,12,-14,3,-9,2,0,-13,-13,-1,3,-12,11,4,-9,8,11,5,-5,-10,3,-1,-11,-13,5,-12,-10,11,11,-3,-5,14,-13,-4,-5,-7,6,2,-13,0,8,-3,4,4,-14,2]
    # print(sorted(S))
    solution = Solution()
    sln = solution.threeSum(S)
    print(len(sln))
    assert len(sln) == 466
    # print(solution.threeSum(S))
    print(datetime.datetime.now() - start)