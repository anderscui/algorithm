def show(l):
    while l:
        print(l.val)
        l = l.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def concat(self):
        l = self
        res = []
        while l:
            res = [l.val] + res
            l = l.next
        return ''.join(str(c) for c in res)


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        n1 = n2 = []
        while l1:
            n1 = [l1.val] + n1
            l1 = l1.next
        while l2:
            n2 = [l2.val] + n2
            l2 = l2.next

        cnt = max(len(n1), len(n2))
        if len(n1) < cnt:
            for i in xrange(cnt - len(n1)):
                n1 = [0] + n1

        if len(n2) < cnt:
            for i in xrange(cnt - len(n2)):
                n2 = [0] + n2

        nums = []
        i = cnt - 1
        carry = 0
        while carry > 0 or i >= 0:

            if i < 0:
                nums = [carry] + nums
                carry = 0
                continue

            s = n1[i] + n2[i] + carry
            carry = s / 10
            s %= 10
            nums = [s] + nums

            i -= 1

        nl = None
        for i in xrange(len(nums)):
            new_node = ListNode(nums[i])
            new_node.next = nl
            nl = new_node

        return nl