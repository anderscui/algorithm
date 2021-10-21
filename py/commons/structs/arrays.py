# coding=utf-8
import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._store = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, index):
        if isinstance(index, int):
            self._check_index(index)
            return self._store[index]
        elif isinstance(index, slice):
            result = []
            start = index.start if index.start is not None else 0
            if start < 0 or start >= self._n:
                start = 0

            stop = index.stop if index.stop is not None else self._n
            if stop < 0 or stop >= self._n:
                stop = self._n

            step = index.step if index.step is not None else 1
            if step <= 0:
                step = 1

            while start < stop:
                result.append(self._store[start])
                start += step

            return result

    def __setitem__(self, index, value):
        self._check_index(index)
        self._store[index] = value

    def __contains__(self, item):
        return self.find(item) >= 0

    def __str__(self):
        return '[' + ', '.join([str(item) for item in self]) + ']'

    def find(self, item):
        for i in range(self._n):
            if self._store[i] == item:
                return i
        return -1

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._store[self._n] = obj
        self._n += 1

    def insert(self, index, obj):
        if index == self._n:
            self.append(obj)
            return

        self._check_index(index)
        if self._n == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self._n, index, -1):
            self._store[i] = self._store[i-1]
        self._store[index] = obj
        self._n += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty array')
        obj = self._store[self._n-1]
        self._store[self._n-1] = None
        self._n -= 1
        return obj

    def remove(self, item):
        i = self.find(item)
        if i < 0:
            raise ValueError('remove(item): item not in array')

        for j in range(i, self._n - 1):
            self._store[j] = self._store[j+1]
        self._store[self._n-1] = None
        self._n -= 1
        return i

    @property
    def capacity(self):
        return self._capacity

    def is_empty(self):
        return self._n == 0

    def _check_index(self, index):
        if index < 0 or index >= self._n:
            raise IndexError('Invalid index')

    def _resize(self, capacity):
        new_store = self._make_array(capacity)
        for i in range(self._n):
            new_store[i] = self._store[i]
        self._store = new_store
        self._capacity = capacity

    def _make_array(self, capacity):
        # ctypes.py_object: <class '_ctypes.PyCSimpleType'>
        # capacity * ctypes.py_object: <class '_ctypes.PyCArrayType'>
        return (capacity * ctypes.py_object)()
