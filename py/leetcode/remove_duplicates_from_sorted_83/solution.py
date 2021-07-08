# coding=utf-8
from typing import List


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        while cur is not None:
            if prev is None or cur.val != prev.val:
                prev = cur
                cur = cur.next
            else:
                cur = cur.next
                prev.next = cur
        return head

    def deleteDuplicates0(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        new_head = None
        new_cur = None
        while cur is not None:
            if prev is None or cur.val != prev.val:
                if new_head is None:
                    new_head = ListNode(cur.val)
                    new_cur = new_head
                else:
                    next_node = ListNode(cur.val)
                    new_cur.next = next_node
                    new_cur = next_node
            prev = cur
            cur = cur.next
        return new_head

    @staticmethod
    def getValues(head: ListNode):
        values = []
        cur = head
        while cur is not None:
            values.append(cur.val)
            cur = cur.next
        return values

    @staticmethod
    def buildList(values: List[int]):
        if not values:
            return None

        head = ListNode(values[0], next=None)
        cur = head
        for value in values[1:]:
            next_node = ListNode(value, next=None)
            cur.next = next_node
            cur = next_node
        return head
