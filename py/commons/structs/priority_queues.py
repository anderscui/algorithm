# coding=utf-8
from abc import abstractmethod
from collections.abc import Iterable

from commons.structs.exceptions import EmptyContainerError
from commons.structs.positional_lists import PositionalList


class PriorityQueueBase:
    class Item:
        __slots__ = 'key', 'value'

        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __lt__(self, other):
            return self.key < other.key

    def is_empty(self):
        return len(self) == 0

    @abstractmethod
    def add(self, key, value):
        raise NotImplementedError

    @abstractmethod
    def min(self):
        raise NotImplementedError

    @abstractmethod
    def remove_min(self):
        raise NotImplementedError

    @abstractmethod
    def __len__(self):
        raise NotImplementedError


class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self.Item(key, value))

    def min(self):
        min_pos = self._find_min()
        item = min_pos.element()
        return item.key, item.value

    def remove_min(self):
        min_pos = self._find_min()
        item = self._data.delete(min_pos)
        return item.key, item.value

    def _find_min(self):
        """
        Finds the position of the minimum node, complexity: O(n)
        :return:
        """
        if self.is_empty():
            raise EmptyContainerError('Priority queue is empty.')

        min_pos = self._data.first()
        cur = self._data.after(min_pos)
        while cur is not None:
            if cur.element() < min_pos.element():
                min_pos = cur
            cur = self._data.after(cur)
        return min_pos


class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        new_element = self.Item(key, value)
        cur = self._data.last()
        while cur is not None and new_element < cur.element():
            cur = self._data.before(cur)
        if cur is None:
            self._data.add_first(new_element)
        else:
            self._data.add_after(cur, new_element)

    def min(self):
        if self.is_empty():
            raise EmptyContainerError('Priority queue is empty.')
        element = self._data.first().element()
        return element.key, element.value

    def remove_min(self):
        if self.is_empty():
            raise EmptyContainerError('Priority queue is empty.')
        element = self._data.delete(self._data.first())
        return element.key, element.value


class HeapPriorityQueue(PriorityQueueBase):
    def __init__(self, contents: Iterable = ()):
        self._data = [self.Item(k, v) for k, v in contents]
        if len(self._data) > 1:
            self._heapify()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.append(self.Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise EmptyContainerError('Priority queue is empty.')
        item = self._data[0]
        return item.key, item.value

    def remove_min(self):
        if self.is_empty():
            raise EmptyContainerError('Priority queue is empty.')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return item.key, item.value

    def _parent_index(self, i):
        return (i-1) // 2

    def _left_index(self, i):
        return 2 * i + 1

    def _right_index(self, i):
        return 2 * i + 2

    def _has_left(self, i):
        return self._left_index(i) < len(self._data)

    def _has_right(self, i):
        return self._right_index(i) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, i):
        parent_index = self._parent_index(i)
        if i > 0 and self._data[i] < self._data[parent_index]:
            self._swap(i, parent_index)
            self._upheap(parent_index)

    def _downheap(self, i):
        if self._has_left(i):
            left_index = self._left_index(i)
            min_child_index = left_index
            if self._has_right(i):
                right_index = self._right_index(i)
                if self._data[right_index] < self._data[left_index]:
                    min_child_index = right_index
            if self._data[min_child_index] < self._data[i]:
                self._swap(i, min_child_index)
                self._downheap(min_child_index)

    def _heapify(self):
        start = self._parent_index(len(self)-1)
        for i in range(start, -1, -1):
            self._downheap(i)
