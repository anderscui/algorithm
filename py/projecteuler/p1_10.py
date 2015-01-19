primes = [2, 3, 5, 7, 11, 13, 17, 19]


def primes_range(start, end):
    return [p for p in primes if start <= p <= end]


def factors(n):
    fs = [0 for p in primes]
    if n < 2:
        return fs

    for i, p in enumerate(primes):
        if n < p:
            break
        while n >= p and n % p == 0:
            fs[i] += 1
            n /= p

    return fs


def p5(n):
    all_factors = [factors(i) for i in xrange(2, n+1)]
    product = 1
    for i in xrange(len(primes)):
        fi = [f[i] for f in all_factors]
        product *= primes[i] ** max(fi)

    return product


if __name__ == '__main__':
    print(factors(2))
    print(factors(6))
    print(factors(8))
    print(factors(10))
    print(factors(20))
    print(factors(66))

    print(p5(10))
    print(p5(20))