# coding=utf-8
from typing import Sequence


def sequential_search(s: Sequence, target):
    for i, item in enumerate(s):
        if item == target:
            return i
    return -1


def binary_search(s: Sequence, target):
    low, high = 0, len(s) - 1
    while low <= high:
        # for each iteration：target 可能的范围已经限定在 low 和 high 之间
        # 如果一直未找到，比如会出现 low > high 的情况
        # 因为只要 len([low, high]) >= 2，每个 iteration 必定会减少
        mid = (low + high) // 2
        if s[mid] == target:
            return mid
        elif s[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
