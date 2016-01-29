# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def concat(self):
        l = self
        res = []
        while l:
            res = res + [l.val]
            l = l.next
        return res


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        odd_tail = head
        even_tail = head.next

        while even_tail:
            odd_next = even_tail.next
            if odd_next:
                even_next = odd_next.next
            else:
                even_next = None

            if odd_next:
                even_tail.next = even_next

                odd_next.next = odd_tail.next
                odd_tail.next = odd_next
                odd_tail = odd_next

            even_tail = even_next

        return head
