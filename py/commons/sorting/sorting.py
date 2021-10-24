# coding=utf-8
from collections.abc import Iterable
from heapq import heappush, heappop
from typing import List

from commons.commons.iterable import merge_sorted_lists


def merge_sort(s: List):
    """
    Sort the elements of list `s`.
    :param s: a `sortable` list
    """

    n = len(s)
    if n < 2:
        return

    mid = n // 2
    left = s[:mid]  # copy left half
    right = s[mid:]  # copy right half
    merge_sort(left)
    merge_sort(right)
    merge_sorted_lists(left, right, s)


def quick_sort(s: List):
    if len(s) < 2:
        return s

    less, equal, greater = [], [], []
    pivot = s[0]
    for x in s:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return quick_sort(less) + equal + quick_sort(greater)


def heap_sort(s: Iterable):
    h = []
    for val in s:
        heappush(h, val)
    return [heappop(h) for _ in range(len(h))]


def selection_sort(s: List):
    n = len(s)
    for i in range(n - 1):
        next_min = i
        for j in range(i+1, n):
            if s[j] < s[next_min]:
                next_min = j
        if i != next_min:
            s[i], s[next_min] = s[next_min], s[i]


def insertion_sort(s: List):
    n = len(s)
    for i in range(1, n):
        cur = s[i]
        j = i - 1
        while j >= 0 and s[j] > cur:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = cur


def bubble_sort(s: List):
    n = len(s)
    for i in range(1, n):
        swapped = False
        for j in range(1, n - i + 1):
            if s[j-1] > s[j]:
                s[j-1], s[j] = s[j], s[j-1]
                swapped = True
        if not swapped:
            break
