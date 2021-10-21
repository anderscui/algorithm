# coding=utf-8

def lcs_lens(s, t):
    n, m = len(s), len(t)
    C = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                C[i+1][j+1] = C[i][j] + 1
            else:
                C[i+1][j+1] = max(C[i][j+1], C[i+1][j])
    return C


def lcs(s, t):
    L = lcs_lens(s, t)
    solution = []
    i, j = len(s), len(t)
    while L[i][j] > 0:
        if s[i-1] == t[j-1]:
            solution.append(s[i-1])
            i -= 1
            j -= 1
        elif L[i-1][j] >= L[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(solution))


def is_sub(text, pattern):
    m, n = len(text), len(pattern)

    if n > m:
        return False

    i, j = 0, 0
    while j < n:
        while i < m and text[i] != pattern[j]:
            i += 1
        if i >= m:
            break
        j += 1

    return j == n


def lcs_brute_force(s, t):
    def sub_texts(text):
        if len(text) == 0:
            return []
        if len(text) == 1:
            return ['', text]

        posts = sub_texts(text[1:])
        return posts + [text[0] + post for post in posts]

    if len(s) > len(t):
        s, t = t, s

    subs = [sub for sub in sub_texts(s) if sub]
    subs = sorted(subs, key=lambda text: len(text), reverse=True)
    for sub in subs:
        if is_sub(t, sub):
            return sub
    return ''
