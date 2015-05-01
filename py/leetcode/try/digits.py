
def highest(n):
    h = n
    while h >= 10:
        h /= 10

    return h


if __name__ == '__main__':
    assert highest(0) == 0
    assert highest(1) == 1
    assert highest(10) == 1
    assert highest(21) == 2
    assert highest(321) == 3