# coding=utf-8
from collections import Counter
from collections.abc import Iterable
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


def dedup(items):
    found = set()
    for item in items:
        if item not in found:
            yield item
            found.add(item)


def max_value(*args, key=None):
    if len(args) == 0:
        raise TypeError('max expected 1 argument, got 0')
    if key is not None and not callable(key):
        raise TypeError('key should be callable')

    items = args
    if len(args) == 1:
        if isinstance(args[0], Iterable):
            items = args[0]
        else:
            raise TypeError('first arg should be iterable.')

    # print('items', items)
    # max_elem = items[0]
    # max_item_key = items[0] if not key else key(items[0])
    max_elem, max_item_key = None, None
    for item in items:
        cur_key = item if not key else key(item)
        if max_item_key is None or cur_key > max_item_key:
            max_elem, max_item_key = item, cur_key
    if max_item_key is None:
        raise TypeError('max() arg is an empty sequence')
    return max_elem


def count_items(items):
    return Counter(items)
