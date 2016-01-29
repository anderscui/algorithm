from odd_even_linked_list import Solution, ListNode

sln = Solution()

# empty list
head = None
assert sln.oddEvenList(head) is None

# one element
head = ListNode(1)
new_head = sln.oddEvenList(head)
assert new_head
assert new_head.val == 1
assert new_head.next is None

# two elements
head = ListNode(1)
head.next = ListNode(2)
new_head = sln.oddEvenList(head)
assert new_head.concat() == [1, 2]


def get_range_linked_list(n):
    head = ListNode(1)
    cur = head
    for i in xrange(2, n+1):
        cur.next = ListNode(i)
        cur = cur.next

    return head

# three elements
head = get_range_linked_list(3)
new_head = sln.oddEvenList(head)
assert new_head.concat() == [1, 3, 2]

# five elements
head = get_range_linked_list(5)
new_head = sln.oddEvenList(head)
assert new_head.concat() == [1, 3, 5, 2, 4]

# six elements
head = get_range_linked_list(6)
new_head = sln.oddEvenList(head)
assert new_head.concat() == [1, 3, 5, 2, 4, 6]

