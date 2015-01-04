

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        #sorted_num = sorted(num)
        sln = []
        cnt = len(num)
        for i in range(cnt):
            a = num[i]
            for j in range(i+1, cnt):
                b = num[j]
                for k in range(i+2, cnt):
                    c = num[k]
                    if a + b + c == 0:
                        sln.append(tuple(sorted([a, b, c])))

        return set(sln)


if __name__ == '__main__':
    S = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.threeSum(S))