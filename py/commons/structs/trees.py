# coding=utf-8
from abc import ABC, abstractmethod
from enum import Enum, unique

from commons.structs.queues import ArrayQueue


class Traversal(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3


class Tree(ABC):
    class Position:
        def element(self):
            raise NotImplementedError

        def __eq__(self, other):
            raise NotImplementedError

        def __ne__(self, other):
            raise NotImplementedError

    @abstractmethod
    def root(self):
        raise NotImplementedError

    @abstractmethod
    def parent(self, pos):
        raise NotImplementedError

    @abstractmethod
    def children_count(self, pos):
        raise NotImplementedError

    @abstractmethod
    def children(self, pos):
        raise NotImplementedError

    @abstractmethod
    def __len__(self):
        raise NotImplementedError

    @abstractmethod
    def positions(self):
        """
        :return Generate an iterator of all positions of a tree.
        """
        raise NotImplementedError

    def __iter__(self):
        for pos in self.positions():
            yield pos.element()

    def is_root(self, pos):
        """
        :return Whether the pos is the root of a tree.
        """
        return self.root() == pos

    def is_leaf(self, pos):
        return self.children_count(pos) == 0

    def is_empty(self) -> bool:
        return len(self) == 0

    def depth(self, pos):
        if self.is_root(pos):
            return 0
        return 1 + self.depth(self.parent(pos))

    def height(self, pos=None):
        if pos is None:
            pos = self.root()
        return self._height(pos)

    def _height(self, pos):
        """
        :return the height of the subtree rooted at `pos`.
        :param pos: root position.
        """
        if self.is_leaf(pos):
            return 0
        return 1 + max(self._height(c) for c in self.children(pos))

    def preorder(self):
        if not self.is_empty():
            for pos in self._preorder(self.root()):
                yield pos

    def _preorder(self, pos):
        yield pos
        for child in self.children(pos):
            for other in self._preorder(child):
                yield other

    def postorder(self):
        if not self.is_empty():
            for pos in self._postorder(self.root()):
                yield pos

    def _postorder(self, pos):
        for child in self.children(pos):
            for other in self._postorder(child):
                yield other
        yield pos

    def breadth_first(self):
        queue = ArrayQueue()
        if not self.is_empty():
            queue.enqueue(self.root())
        while not queue.is_empty():
            pos = queue.dequeue()
            yield pos
            for c in self.children(pos):
                queue.enqueue(c)


class BinaryTree(Tree):
    @abstractmethod
    def left(self, pos):
        raise NotImplementedError

    @abstractmethod
    def right(self, pos):
        raise NotImplementedError

    def sibling(self, pos):
        parent = self.parent(pos)
        if parent is None:
            return None
        elif pos == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, pos):
        if self.left(pos) is not None:
            yield self.left(pos)
        if self.right(pos) is not None:
            yield self.right(pos)


class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
            
    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, pos):
        if not isinstance(pos, self.Position):
            raise TypeError('pos must be proper Position type.')
        if pos._container is not self:
            raise ValueError('pos does not belong to this container.')
        if pos._node._parent is pos._node:
            raise ValueError('pos is no longer valid.')
        return pos._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    @classmethod
    def create_tree_with_root(cls, root_element):
        tree = LinkedBinaryTree()
        tree.add_root(root_element)
        return tree

    def add_root(self, element):
        if self._root is not None:
            raise ValueError('Root exists.')
        self._root = self._Node(element)
        self._size = 1
        return self._make_position(self._root)

    def add_left(self, pos, element):
        node = self._validate(pos)
        if node._left is not None:
            raise ValueError('Left child exists.')

        node._left = self._Node(element, parent=node)
        self._size += 1
        return self._make_position(node._left)

    def add_right(self, pos, element):
        node = self._validate(pos)
        if node._right is not None:
            raise ValueError('Right child exists')

        node._right = self._Node(element, parent=node)
        self._size += 1
        return self._make_position(node._right)

    def replace(self, pos, element):
        """
        Replace element of position `pos'.
        :param pos:
        :param element:
        :return: old element value.
        """
        node = self._validate(pos)
        old_elem = node._element
        node._element = element
        return old_elem

    def delete(self, pos):
        node = self._validate(pos)
        if self.children_count(pos) == 2:
            raise ValueError('pos has two children.')
        child = node._left if node._left is not None else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node  # mark as deleted
        return node._element

    def attach(self, pos, t1, t2):
        """
        Attach trees t1 and t2 as left and right subtrees of external node `pos`.
        :param pos:
        :param t1:
        :param t2:
        """
        node = self._validate(pos)
        if not self.is_leaf(pos):
            raise ValueError('pos must be leaf.')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('tree types must match')

        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
        self._size += len(t1) + len(t2)

    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self._make_position(self._root)

    def parent(self, pos):
        node = self._validate(pos)
        return self._make_position(node._parent)

    def left(self, pos):
        node = self._validate(pos)
        return self._make_position(node._left)

    def right(self, pos):
        node = self._validate(pos)
        return self._make_position(node._right)

    def children_count(self, pos):
        node = self._validate(pos)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def __len__(self):
        return self._size

    def positions(self):
        for pos in self.preorder():
            yield pos

    def inorder(self):
        if not self.is_empty():
            for pos in self._inorder(self.root()):
                yield pos

    def _inorder(self, pos):
        if self.left(pos) is not None:
            for lp in self._inorder(self.left(pos)):
                yield lp
        yield pos
        if self.right(pos) is not None:
            for rp in self._inorder(self.right(pos)):
                yield rp
