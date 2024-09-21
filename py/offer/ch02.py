# coding=utf-8
from typing import List

from offer.commons import ListNode, BinaryTreeNode


def find_in_sorted_matrix(matrix: List[List[int]], n: int):
    found = False
    if matrix and matrix[0]:
        n_rows = len(matrix)

        row = 0
        col = len(matrix[0]) - 1
        while row < n_rows and col >= 0:
            if matrix[row][col] == n:
                found = True
                break
            elif matrix[row][col] > n:
                col -= 1
            else:
                row += 1
    return found


def reverse_linked_list(head: ListNode):
    stack = []
    cur = head
    while cur is not None:
        stack.append(cur)
        cur = cur.next
    for i in range(len(stack)-1, -1, -1):
        yield stack[i].value


def reverse_linked_list_recursively(head: ListNode):
    """
    2.3.3：递归可能会导致栈溢出
    :param head:
    :return:
    """
    if head is None:
        return
    for value in reverse_linked_list_recursively(head.next):
        yield value
    yield head.value


def rebuild_binary_tree(preorder_values: List[int], inorder_values: List[int]):
    def rebuild(preorder, preorder_start, preorder_end, inorder, inorder_start, inorder_end):
        # assert (preorder_end - preorder_start) == (inorder_end - inorder_start)
        if preorder_end < preorder_start:
            return None

        root_value = preorder[preorder_start]
        i_inorder = inorder_values.index(root_value, inorder_start, inorder_end+1)
        # print(root_value, i_inorder, preorder[preorder_start:preorder_end+1], inorder[inorder_start:inorder_end+1])
        left_inorder_len = i_inorder - inorder_start
        # right_inorder_len = inorder_end - i_inorder
        root = BinaryTreeNode(root_value, rebuild(preorder, preorder_start+1, preorder_start+left_inorder_len,
                                                  inorder, inorder_start, i_inorder-1),
                                          rebuild(preorder, preorder_start+left_inorder_len+1, preorder_end,
                                                  inorder, i_inorder+1, inorder_end))
        return root

    return rebuild(preorder_values, 0, len(preorder_values)-1, inorder_values, 0, len(inorder_values)-1)
