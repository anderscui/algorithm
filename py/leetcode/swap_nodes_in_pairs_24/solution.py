# coding=utf-8
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def buildPairs(self, values: List[int]):
        if not values:
            return None

        head = ListNode(values[0], next=None)
        cur = head
        for value in values[1:]:
            next_node = ListNode(value, next=None)
            cur.next = next_node
            cur = next_node
        return head

    def showPairs(self, head: ListNode):
        cur = head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print()

    def getValues(self, head: ListNode):
        values = []
        cur = head
        while cur is not None:
            values.append(cur.val)
            cur = cur.next
        return values

    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        pair_next = head.next.next
        cur = head
        head = head.next
        head.next = cur
        cur.next = self.swapPairs(pair_next)
        return head

    def swapPairs1(self, head: ListNode) -> ListNode:
        cur_node, next_node, prev_node = head, None, None
        new_head = head
        is_first_pair = True
        while cur_node:
            next_node = cur_node.next
            if cur_node and next_node:
                pair_next = next_node.next
                if is_first_pair:
                    new_head = next_node
                    is_first_pair = False
                next_node.next = cur_node
                if prev_node:
                    prev_node.next = next_node
                cur_node.next = pair_next
                prev_node = cur_node
                cur_node = pair_next
            else:
                cur_node = None

        return new_head

    def swapPairs0(self, head: ListNode) -> ListNode:
        cur_node, next_node, prev_node = head, None, None
        new_head = head
        if cur_node:
            next_node = cur_node.next
        if cur_node and next_node:
            pair_next = next_node.next
            new_head = next_node
            next_node.next = cur_node
            cur_node.next = pair_next
            prev_node = cur_node
            cur_node = pair_next

        while cur_node:
            next_node = cur_node.next
            if cur_node and next_node:
                pair_next = next_node.next
                # new_head = next_node
                next_node.next = cur_node
                prev_node.next = next_node  #
                cur_node.next = pair_next
                prev_node = cur_node
                cur_node = pair_next
            else:
                cur_node = None

        return new_head
