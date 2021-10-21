# coding=utf-8
from typing import List, Sequence


def merge_sorted_lists(l1: List, l2: List, target: List):
    """
    :param l1: first sorted list
    :param l2: second sorted list
    :param target: target list to combine into
    """
    i, j = 0, 0
    while i + j < len(target):
        if j == len(l2) or (i < len(l1) and l1[i] <= l2[j]):
            target[i+j] = l1[i]
            i += 1
        else:
            target[i+j] = l2[j]
            j += 1


def is_sorted(s: Sequence) -> bool:
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            return False
    return True


def is_unique(s: Sequence, key=None) -> bool:
    if key is None:
        key = lambda x: x

    found = set()
    for item in s:
        item_key = key(item)
        if item_key in found:
            return False
        found.add(item_key)
    return True
