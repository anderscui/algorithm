class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)

        # initialize
        dist = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            dist[i][0] = i
        for j in range(n+1):
            dist[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):

                d1 = dist[i-1][j] + 1
                d2 = dist[i][j-1] + 1
                d3 = dist[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    d3 += 1
                dist[i][j] = min(d1, d2, d3)

        return dist[m][n]