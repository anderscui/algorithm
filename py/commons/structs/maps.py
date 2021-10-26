# coding=utf-8
from abc import abstractmethod
from collections import MutableMapping
from random import randrange

from commons.structs.trees import LinkedBinaryTree


class MapBase(MutableMapping):
    class Item:
        __slots__ = 'key', 'value'

        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            return self.key == other.key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self.key < other.key

    def is_empty(self):
        return len(self) == 0


class UnsortedTableMap(MapBase):
    def __init__(self):
        self._table = []

    def __getitem__(self, key):
        for item in self._table:
            if item.key == key:
                return item.value
        raise KeyError('Key error: ' + repr(key))

    def __setitem__(self, key, value):
        for item in self._table:
            if item.key == key:
                item.value = value
                return
        self._table.append(self.Item(key, value))

    def __delitem__(self, key):
        for i in range(len(self._table)):
            item = self._table[i]
            if item.key == key:
                self._table.pop(i)
                return
        raise KeyError('Key error: ' + repr(key))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item.key

    def values(self):
        for item in self._table:
            yield item.value

    def items(self):
        for item in self._table:
            yield item.key, item.value


class HashMapBase(MapBase):
    """Abstract base class for map using hash table with MAD compression."""

    def __init__(self, cap=11, p=109345121):
        self._table = [None] * cap
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)

    def _hash_function(self, key):
        return (hash(key) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, key):
        i = self._hash_function(key)
        return self._bucket_getitem(i, key)

    def __setitem__(self, key, value):
        i = self._hash_function(key)
        self._bucket_setitem(i, key, value)
        if self._n > len(self._table) // 2:
            # number 2^x - 1 is often prime.
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, key):
        i = self._hash_function(key)
        self._bucket_delitem(i, key)
        self._n -= 1

    @abstractmethod
    def _bucket_getitem(self, i, key):
        raise NotImplementedError

    @abstractmethod
    def _bucket_setitem(self, i, key, value):
        raise NotImplementedError

    @abstractmethod
    def _resize(self, param):
        raise NotImplementedError

    @abstractmethod
    def _bucket_delitem(self, i, key):
        raise NotImplementedError


class ChainHashMap(HashMapBase):
    """Hash map impl with spearate chaining for collision resolution."""

    def _resize(self, param):
        # do not need to do anything.
        pass

    def _bucket_getitem(self, i, key):
        bucket = self._table[i]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(key))
        return bucket[key]

    def _bucket_setitem(self, i, key, value):
        if self._table[i] is None:
            self._table[i] = UnsortedTableMap()
        bucket = self._table[i]
        old_size = len(bucket)
        bucket[key] = value
        if len(bucket) > old_size:
            self._n += 1

    def _bucket_delitem(self, i, key):
        bucket = self._table[i]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(key))
        del bucket[key]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key


class ProbeHashMap(HashMapBase):
    _AVAIL = object()  # sentinal marks locations for previous deletions.

    def _resize(self, param):
        # do not need to do anything.
        pass

    def _is_available(self, i):
        return self._table[i] is None or self._table[i] is ProbeHashMap._AVAIL

    def _find_slot(self, i, key):
        first_avail = None
        while True:
            if self._is_available(i):
                if first_avail is None:
                    first_avail = i
                if self._table[i] is None:
                    return False, first_avail
            elif key == self._table[i].key:
                return True, i
            i = (i + 1) % len(self._table)

    def _bucket_getitem(self, i, key):
        found, slot = self._find_slot(i, key)
        if not found:
            raise KeyError('Key Error: ' + repr(key))
        return self._table[slot].value

    def _bucket_setitem(self, i, key, value):
        found, slot = self._find_slot(i, key)
        if found:
            self._table[slot].value = value
        else:
            self._table[slot] = self.Item(key, value)
            self._n += 1

    def _bucket_delitem(self, i, key):
        found, slot = self._find_slot(i, key)
        if not found:
            raise KeyError('Key Error: ' + repr(key))
        self._table[slot] = ProbeHashMap._AVAIL

    def __iter__(self):
        for i in range(len(self._table)):
            if not self._is_available(i):
                yield self._table[i].key


class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implemented with a binary search tree."""

    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element().key

        def value(self):
            return self.element().value

    def __getitem__(self, key):
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(key))
        else:
            pos = self._subtree_search(self.root(), key)
            self._rebalance_access(pos)
            if key != pos.key():
                raise KeyError('Key Error: ' + repr(key))
            return pos.value()

    def __setitem__(self, key, value):
        if self.is_empty():
            leaf = self.add_root(self.Item(key, value))
        else:
            pos = self._subtree_search(self.root(), key)
            if pos.key() == key:
                pos.element().value = value
                self._rebalance_access(pos)
                return
            else:
                item = self.Item(key, value)
                if pos.key() < key:
                    leaf = self.add_right(pos, item)
                else:
                    leaf = self.add_left(pos, item)
        self._rebalance_insert(leaf)

    def __delitem__(self, key) -> None:
        if not self.is_empty():
            pos = self._subtree_search(self.root(), key)
            if pos.key() == key:
                self.delete(pos)
                return
            self._rebalance_access(pos)
        raise KeyError('Key Error: ' + repr(key))

    def __iter__(self):
        pos = self.first()
        while pos is not None:
            yield pos.key()
            pos = self.after(pos)

    def first(self):
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, pos):
        self._validate(pos)
        if self.left(pos):
            return self._subtree_last_position(self.left(pos))
        else:
            cur = pos
            above = self.parent(cur)
            while above is not None and cur == self.left(above):
                cur = above
                above = self.parent(cur)
            return above

    def after(self, pos):
        self._validate(pos)
        if self.right(pos):
            return self._subtree_first_position(self.right(pos))
        else:
            cur = pos
            above = self.parent(cur)
            while above is not None and cur == self.right(above):
                cur = above
                above = self.parent(cur)
            return above

    def find_position(self, key):
        if self.is_empty():
            return None
        pos = self._subtree_search(self.root(), key)
        self._rebalance_access(pos)
        return pos

    def find_min(self):
        if self.is_empty():
            return None
        pos = self.first()
        return pos.key(), pos.value

    def find_ge(self, key):
        if self.is_empty():
            return None
        else:
            pos = self.find_position(key)
            if pos.key() < key:
                pos = self.after(pos)
            return pos.key(), pos.value() if pos is not None else None

    def find_range(self, start, stop):
        if not self.is_empty():
            if start is None:
                pos = self.first()
            else:
                pos = self.find_position(start)
                if pos.key() < start:
                    pos = self.after(pos)
            while pos is not None and (stop is None or pos.key() < stop):
                yield pos.key(), pos.value()
                pos = self.after(pos)

    def delete(self, pos):
        self._validate(pos)
        if self.left(pos) and self.right(pos):
            replacement = self._subtree_last_position(self.left(pos))
            self.replace(pos, replacement.element())
            pos = replacement
        # now pos has at most one child.
        parent = self.parent(pos)
        super().delete(pos)
        self._rebalance_delete(parent)

    def _subtree_first_position(self, pos):
        cur = pos
        while self.left(cur) is not None:
            cur = self.left(cur)
        return cur

    def _subtree_last_position(self, pos):
        cur = pos
        while self.right(cur) is not None:
            cur = self.right(cur)
        return cur

    def _subtree_search(self, pos, key):
        if pos.key() == key:
            return pos
        elif pos.key() > key:
            if self.left(pos) is not None:
                return self._subtree_search(self.left(pos), key)
        else:
            if self.right(pos) is not None:
                return self._subtree_search(self.right(pos), key)
        return pos

    def _rebalance_access(self, pos):
        pass

    def _rebalance_insert(self, pos):
        pass

    def _rebalance_delete(self, pos):
        pass

    def _relink(self, parent, child, make_left_child):
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, pos):
        x = pos._node
        y = x._parent  # assume this exists
        z = y._parent  # this could be None
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)  # x -> direct child of z

        # rotate x and y, including transfer of middle subtree
        if x == y._left:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)

    def _restructure(self, x):
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x


class AvlTreeMap(TreeMap):
    """Sorted map implemented with an AVL tree."""

    class _Node(TreeMap._Node):
        """Node class for AVL to maintain height values."""
        __slots__ = '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0

        def left_height(self):
            return self._left._height if self._left is not None else 0

        def right_height(self):
            return self._right._height if self._right is not None else 0

    def _recompute_height(self, pos):
        pos._node._height = 1 + max(pos._node.left_height(), pos._node.right_height())

    def _is_balanced(self, pos):
        return abs(pos._node.left_height() - pos._node.right_height()) <= 1

    def _tail_child(self, pos, favor_left=False):
        if pos._node.left_height() + (1 if favor_left else 0) > pos._node.right_height():
            return self.left(pos)
        else:
            return self.right(pos)

    def _tail_grandchild(self, pos):
        child = self._tail_child(pos)
        alignment = (child == self.left(pos))
        return self._tail_child(child, alignment)

    def _rebalance(self, pos):
        while pos is not None:
            old_height = pos._node._height
            if not self._is_balanced(pos):
                pos = self._restructure(self._tail_grandchild(pos))
                self._recompute_height(self.left(pos))
                self._recompute_height(self.right(pos))
            self._recompute_height(pos)
            if pos._node._height == old_height:  # has height changed?
                pos = None  # no further changes needed
            else:
                pos = self.parent(pos)

    def _rebalance_delete(self, pos):
        self._rebalance(pos)

    def _rebalance_insert(self, pos):
        self._rebalance(pos)
