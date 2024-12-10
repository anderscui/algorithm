# coding=utf-8


class Solution:
    def isValid(self, s: str) -> bool:
        open_ps_chars = '([{'
        # close_ps_cars = ')]}'
        close_ps_map = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        open_ps = []
        for c in s:
            if c in open_ps_chars:
                open_ps.append(c)
            elif c in close_ps_map:
                if not open_ps:
                    return False
                last_open = open_ps.pop(-1)
                if last_open != close_ps_map[c]:
                    return False
        return len(open_ps) == 0


if __name__ == '__main__':
    sln = Solution()

    inputs = '()'
    assert sln.isValid(inputs)

    inputs = '()[]{}'
    assert sln.isValid(inputs)

    inputs = '([])'
    assert sln.isValid(inputs)

    inputs = '(]'
    assert not sln.isValid(inputs)

    inputs = '(([])'
    assert not sln.isValid(inputs)

    inputs = ']()'
    assert not sln.isValid(inputs)

    inputs = ''
    assert sln.isValid(inputs)
