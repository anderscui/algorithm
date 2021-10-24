# coding=utf-8
from commons.structs.linked_lists import DoublyLinkedBase


class PositionalList(DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return self.node.element

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self.node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, pos):
        if not isinstance(pos, self.Position):
            raise TypeError('pos must be proper Position type.')
        if pos.container is not self:
            raise ValueError('pos does not belong to this container.')
        if pos.node.next is None:
            raise ValueError('pos is no longer valid.')
        return pos.node

    def _make_position(self, node):
        if node is self.header or node is self.trailer:
            return None
        return self.Position(self, node)

    def insert_between(self, element, predecessor, successor):
        node = super().insert_between(element, predecessor, successor)
        return self._make_position(node)

    def first(self):
        return self._make_position(self.header.next)

    def last(self):
        return self._make_position(self.trailer.prev)

    def before(self, pos):
        node = self._validate(pos)
        return self._make_position(node.prev)

    def after(self, pos):
        node = self._validate(pos)
        return self._make_position(node.next)

    def __iter__(self):
        cur = self.first()
        while cur is not None:
            yield cur.element()
            cur = self.after(cur)

    def add_first(self, element):
        return self.insert_between(element, self.header, self.header.next)

    def add_last(self, element):
        return self.insert_between(element, self.trailer.prev, self.trailer)

    def add_before(self, pos, element):
        node = self._validate(pos)
        return self.insert_between(element, node.prev, node)

    def add_after(self, pos, element):
        node = self._validate(pos)
        return self.insert_between(element, node, node.next)

    def delete(self, pos):
        node = self._validate(pos)
        return self.delete_node(node)

    def replace(self, pos, element):
        node = self._validate(pos)
        old_element = node.element
        node.element = element
        return old_element
