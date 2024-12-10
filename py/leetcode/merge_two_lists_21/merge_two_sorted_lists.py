# coding=utf-8
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_left, cur_right = list1, list2
        merged = ListNode(val=-1, next=None)
        cur_merged = merged
        while cur_left is not None and cur_right is not None:
            val_left, val_right = cur_left.val, cur_right.val
            if val_left <= val_right:
                cur_merged.next = cur_left
                cur_left = cur_left.next
            else:
                cur_merged.next = cur_right
                cur_right = cur_right.next
            cur_merged = cur_merged.next

        while cur_left is not None:
            cur_merged.next = cur_left
            cur_merged = cur_merged.next
            cur_left = cur_left.next

        while cur_right is not None:
            cur_merged.next = cur_right
            cur_merged = cur_merged.next
            cur_right = cur_right.next

        return merged.next


def build_list(vals):
    head = ListNode()
    cur = head
    for val in vals:
        new_node = ListNode(val, next=None)
        cur.next = new_node
        cur = cur.next
    return head.next


def get_list_values(node: Optional[ListNode]):
    vals = []
    cur = node
    while cur is not None:
        vals.append(cur.val)
        cur = cur.next
    return vals


def show_list(node: Optional[ListNode]):
    print(f'values: {get_list_values(node)}')


if __name__ == '__main__':
    sln = Solution()

    l1, l2 = build_list([1, 2, 4]), build_list([1, 3, 4])
    m = sln.mergeTwoLists(l1, l2)
    assert get_list_values(m) == [1,1,2,3,4,4]

    l1, l2 = build_list([]), build_list([])
    m = sln.mergeTwoLists(l1, l2)
    assert get_list_values(m) == []

    l1, l2 = build_list([]), build_list([0])
    m = sln.mergeTwoLists(l1, l2)
    assert get_list_values(m) == [0]

    l1, l2 = build_list([1, 1, 3]), build_list([5, 5, 6])
    m = sln.mergeTwoLists(l1, l2)
    assert get_list_values(m) == [1, 1, 3, 5, 5, 6]
