# coding=utf-8
from commons.structs.exceptions import EmptyContainerError


class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, value):
        new_node = LinkedListNode(value, self.head)
        self.head = new_node
        if self.is_empty():
            self.tail = new_node
        self.size += 1

    def add_last(self, value):
        new_node = LinkedListNode(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def remove_first(self):
        self._check_empty()

        old_head = self.head
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None

        return old_head.value

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if isinstance(index, int):
            self._check_index(index)
            cur_node = self.head
            for _ in range(index):
                cur_node = cur_node.next
            return cur_node.value

    def is_empty(self):
        return self.size == 0

    def _check_empty(self):
        if self.is_empty():
            raise EmptyContainerError('LinkedList is empty')

    def _check_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Invalid index')


class DoublyLinkedBase:
    class Node:
        __slots__ = 'element', 'prev', 'next'
        
        def __init__(self, element, prev=None, _next=None):
            self.element = element
            self.prev = prev
            self.next = _next

    def __init__(self):
        self.header = self.Node(None)
        self.trailer = self.Node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_between(self, element, predecessor, successor):
        new_node = self.Node(element, predecessor, successor)
        predecessor.next = new_node
        successor.prev = new_node
        self.size += 1
        return new_node

    def delete_node(self, node: Node):
        prev = node.prev
        _next = node.next
        prev.next = _next
        _next.prev = prev
        self.size -= 1

        element = node.element
        node.element = node.prev = node.next = None
        return element
