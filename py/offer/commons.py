# coding=utf-8
from typing import Optional, List


class ListNode:
    def __init__(self, value, next_node: Optional['ListNode']):
        self.value = value
        self.next = next_node


class BinaryTreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def build_int_linked_list(values: List[int]):
    if not values:
        return None

    head = ListNode(values[0], next_node=None)
    cur = head
    for value in values[1:]:
        next_node = ListNode(value, next_node=None)
        cur.next = next_node
        cur = next_node
    return head
