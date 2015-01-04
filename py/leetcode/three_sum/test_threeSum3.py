import datetime
from threeSum3 import Solution

solution = Solution()

S = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(S))
S1 = [-1, 0, 2]
print(solution.threeSum(S1))
S2 = [-1, 1]
print(solution.threeSum(S2))
S3 = [0, 0, 0]
print(solution.threeSum(S3))

S5 = [1, 2, -2, -1]
print(solution.threeSum(S5))
S6 = [3, 0, -2, -1, 1, 2]
print(solution.threeSum(S6))


start = datetime.datetime.now()
S7 = [-5,14,1,-2,11,11,-10,3,-6,0,3,-4,-9,-13,-8,-7,9,8,-7,11,12,-7,4,-7,-1,-5,13,1,-2,8,-13,0,-1,3,13,-13,-1,10,5,1,-13,-15,12,-7,-13,-11,-7,3,13,1,0,2,1,11,10,8,-8,1,-14,-3,-6,-12,12,0,6,2,2,-9,-3,14,-1,-9,14,-4,-1,8,-8,7,-4,12,-14,3,-9,2,0,-13,-13,-1,3,-12,11,4,-9,8,11,5,-5,-10,3,-1,-11,-13,5,-12,-10,11,11,-3,-5,14,-13,-4,-5,-7,6,2,-13,0,8,-3,4,4,-14,2]
# print(sorted(S7))
sln = solution.threeSum(S7)
print(len(sln))
# assert len(sln) == 466
print(sorted(sln))
print(datetime.datetime.now() - start)

# start = datetime.datetime.now()
# S8 = [7,5,-8,-6,-13,7,10,1,1,-4,-14,0,-1,-10,1,-13,-4,6,-11,8,-6,0,0,-5,0,11,-9,8,2,-6,4,-14,6,4,-5,0,-12,12,-13,5,-6,10,-10,0,7,-2,-5,-12,12,-9,12,-9,6,-11,1,14,8,-1,7,-13,8,-11,-11,0,0,-1,-15,3,-11,9,-7,-10,4,-2,5,-4,12,7,-8,9,14,-11,7,5,-15,-15,-4,0,0,-11,3,-15,-15,7,0,0,13,-7,-12,9,9,-3,14,-1,2,5,2,-9,-3,1,7,-12,-3,-1,1,-2,0,12,5,7,8,-7,7,8,7,-15]
# print(sorted(S8))
# sln = solution.threeSum(S8)
# print(len(sln))
# assert len(sln) == 466
# # print(solution.threeSum(S8))
# print(datetime.datetime.now() - start)