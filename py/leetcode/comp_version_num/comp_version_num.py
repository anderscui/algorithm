# 0.1 < 1.1 < 1.2 < 13.37

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = [int(p) for p in version1.split('.')]
        v2 = [int(p) for p in version2.split('.')]

        while len(v1) > 1 and v1[-1] == 0:
            v1.pop(-1)
        while len(v2) > 1 and v2[-1] == 0:
            v2.pop(-1)

        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        else:
            return 0