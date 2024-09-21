# coding=utf-8
from typing import Optional

from offer.commons import ListNode


def str2int(s: Optional[str]) -> Optional[int]:
    if s is None or not s or s == '-':
        return None

    negative = s[0] == '-'
    if negative:
        s = s[1:]

    i = 0
    for c in s:
        i = i * 10 + int(c)
    return -i if negative else i


def find_kth_to_tail(list_head: ListNode, k: int):
    if list_head is None or k < 1:
        return None

    first, second = list_head, list_head
    for _ in range(k-1):
        first = first.next
        if first is None:
            raise ValueError('the list does not have enough nodes.')

    while first.next is not None:
        first = first.next
        second = second.next
    return second
