# coding=utf-8


class Solution:
    def get_next_ugly(self, known_ugly: list):
        cur_max = known_ugly[-1]
        possible = []
        # 可能的下一个必然来自于已知的数乘以某一个素数，且只可能是其中的第一个
        for p in [2, 3, 5]:
            for i in known_ugly:
                if i * p > cur_max:
                    possible.append(i * p)
                    break
        return min(possible)

    def nthUglyNumber(self, n: int) -> int:
        if n <= 1:
            return 1

        collected = [1]
        while len(collected) < n:
            next_ugly = self.get_next_ugly(collected)
            collected.append(next_ugly)
            if len(collected) == n:
                return next_ugly


if __name__ == '__main__':
    import time

    sln = Solution()

    start = time.time()

    assert sln.nthUglyNumber(10) == 12
    assert sln.nthUglyNumber(1) == 1
    assert sln.nthUglyNumber(421) == 393660
    # assert sln.nthUglyNumber(1000) == 51200000

    print(time.time() - start)
