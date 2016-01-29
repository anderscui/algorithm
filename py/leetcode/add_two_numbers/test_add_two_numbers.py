
from add_two_numbers import Solution, ListNode, show


def build_num_list(l):
    # nl = ListNode(l[0])
    nl = None
    for i in xrange(len(l)):
        new_node = ListNode(l[i])
        new_node.next = nl
        nl = new_node

    return nl


# n1 = build_num_list([3, 4, 2])
# show(n1)
#
# n2 = build_num_list([4, 6, 5])
# show(n2)


sln = Solution()

print('342 + 465')
h1 = build_num_list([3, 4, 2])
h2 = build_num_list([4, 6, 5])
print(sln.addTwoNumbers(h1, h2).concat())

print('123 + 213')
h1 = build_num_list([1, 2, 3])
h2 = build_num_list([2, 1, 3])
print(sln.addTwoNumbers(h1, h2).concat())

print('12 + 212')
h1 = build_num_list([1, 2])
h2 = build_num_list([2, 1, 2])
print(sln.addTwoNumbers(h1, h2).concat())

print('5 + 5')
h1 = build_num_list([5])
h2 = build_num_list([5])
print(sln.addTwoNumbers(h1, h2).concat())
