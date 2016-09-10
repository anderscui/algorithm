# LCS: Longest Common Subsequence
# LCS here is different from LC Substring...

# application: text similarity


def lcs(x, y):
    m = len(x) + 1
    n = len(y) + 1
    C = [[0 for j in range(n)] for i in range(m)]
    B = [['' for j in range(n)] for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if x[i-1] == y[j-1]:
                C[i][j] = C[i-1][j-1]+1
                B[i][j] = 'TL'
            elif C[i-1][j] >= C[i][j-1]:
                C[i][j] = C[i-1][j]
                B[i][j] = 'T'
            else:
                C[i][j] = C[i][j-1]
                B[i][j] = 'L'

    # for i in range(m):
    #     print(C[i])
    # print()
    # for i in range(m):
    #     print(B[i])

    return C, B


def show_lcs(x, y, c, b, m, n):
    if m == 0 or n == 0:
        return

    if b[m][n] == 'TL':
        print(x[m-1])
        show_lcs(x, y, c, b, m-1, n-1)
    elif b[m][n] == 'T':
        show_lcs(x, y, c, b, m-1, n)
    else:
        show_lcs(x, y, c, b, m, n-1)


def show(x, y, c, b):
    m = len(c)
    n = len(c[0])
    show_lcs(x, y, c, b, m-1, n-1)


X = 'ABCBDAB'
Y = 'BDCABA'
matrix = lcs(X, Y)
show(X, Y, matrix[0], matrix[1])


## LIS: Longest Increasing Subsequences
X = [5, 6, 7, 1, 2, 8]
Y = sorted(X)
matrix = lcs(X, Y)
show(X, Y, matrix[0], matrix[1])
