# coding=utf-8
from abc import ABC, abstractmethod

from commons.structs.exceptions import EmptyContainerError


class Queue(ABC):
    @abstractmethod
    def enqueue(self, item):
        raise NotImplementedError

    @abstractmethod
    def dequeue(self):
        raise NotImplementedError

    @abstractmethod
    def first(self):
        raise NotImplementedError

    @abstractmethod
    def is_empty(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __len__(self):
        raise NotImplementedError


class ArrayQueue(Queue):
    def __init__(self):
        self._data = []
        self._size = 0
        self._front = 0

    def enqueue(self, item):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        next_index = (self._front + self._size) % len(self._data)
        self._data[next_index] = item
        self._size += 1

    def dequeue(self):
        self._check_empty()
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return item

    def first(self):
        self._check_empty()
        return self._data[self._front]

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self):
        return self._size

    def _check_empty(self):
        if self.is_empty():
            raise EmptyContainerError('Queue is empty')

    def _resize(self, capacity):
        old_data = self._data
        self._data = [None] * capacity
        cur_index = self._front
        for i in range(self._size):
            self._data[i] = old_data[cur_index]
            cur_index = (cur_index+1) % len(old_data)
        self._front = 0
