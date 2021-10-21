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
        mid = (low + high) // 2
        if s[mid] == target:
            return mid
        elif s[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
