# coding=utf-8
from abc import ABC, abstractmethod

from commons.structs.exceptions import EmptyContainerError


class Stack(ABC):
    @abstractmethod
    def push(self, item):
        raise NotImplementedError

    @abstractmethod
    def pop(self):
        raise NotImplementedError

    @abstractmethod
    def top(self):
        raise NotImplementedError

    @abstractmethod
    def is_empty(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __len__(self):
        raise NotImplementedError


class ArrayStack(Stack):
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        self._check_empty()
        return self._data.pop()

    def top(self):
        self._check_empty()
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def _check_empty(self):
        if self.is_empty():
            raise EmptyContainerError('Stack is empty')
