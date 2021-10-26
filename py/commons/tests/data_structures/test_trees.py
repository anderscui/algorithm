# coding=utf-8
import unittest

from commons.structs.trees import Tree, BinaryTree, LinkedBinaryTree


class TestTrees(unittest.TestCase):
    def test_linked_binary_tree(self):
        tree = LinkedBinaryTree()
        self.assertTrue(tree.is_empty())

        root = tree.add_root(1)
        self.assertFalse(tree.is_empty())
        self.assertEqual(1, len(tree))

        left = tree.add_left(root, 2)
        right = tree.add_right(root, 3)
        self.assertEqual(3, len(tree))

        tree.replace(left, 0)

        tree.attach(right,
                    LinkedBinaryTree.create_tree_with_root(4),
                    LinkedBinaryTree.create_tree_with_root(5))

        pre_order_elems = [elem for elem in tree]
        self.assertListEqual([1, 0, 3, 4, 5], pre_order_elems)

        post_oder_elems = [pos.element() for pos in tree.postorder()]
        self.assertListEqual([0, 4, 5, 3, 1], post_oder_elems)

        in_order_elems = [pos.element() for pos in tree.inorder()]
        self.assertListEqual([0, 1, 4, 3, 5], in_order_elems)

        breadth_first_elems = [pos.element() for pos in tree.breadth_first()]
        self.assertListEqual([1, 0, 3, 4, 5], breadth_first_elems)

        self.assertRaises(ValueError, lambda: tree.delete(right))
