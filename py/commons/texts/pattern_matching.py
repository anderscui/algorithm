# str: find/index/count, partition/split/replace


def find_brute_force(text: str, pattern: str):
    """Return the lowest index of `text` at which substr `pattern` begins, or else -1."""

    n, m = len(text), len(pattern)
    for i in range(n-m+1):
        k = 0
        while k < m and pattern[k] == text[i+k]:
            k += 1
        if k == m:
            return i
    return -1


def find_boyer_moore(text: str, pattern: str):
    """Return the lowest index of `text` at which substr `pattern` begins, or else -1."""

    n, m = len(text), len(pattern)
    if m == 0:
        return 0

    lasts = {}
    for k in range(m):
        lasts[pattern[k]] = k

    i, k = m-1, m-1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = lasts.get(text[i], -1)
            i += m - min(k, j+1)
            k = m - 1

    return -1


def find_kmp(text: str, pattern: str):
    """Return the lowest index of `text` at which substr `pattern` begins, or else -1."""

    def compute_fails():
        m = len(pattern)
        fails = [0] * m
        j = 1
        k = 0
        while j < m:
            if pattern[j] == pattern[k]:
                fails[j] = k + 1
                j += 1
                k += 1
            elif k > 0:
                k = fails[k-1]
            else:
                j += 1
        return fails

    n, m = len(text), len(pattern)
    if m == 0:
        return 0

    fails = compute_fails()
    j = 0  # text
    k = 0  # pattern
    while j < n:
        if text[j] == pattern[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fails[k - 1]
        else:
            j += 1
    return -1
