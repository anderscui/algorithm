# coding=utf-8


class Node:
    def __init__(self, value):
        self._children = {}
        self._value = value

    def _add_child(self, char, value, overwrite=False):
        child = self._children.get(char)
        if child is None:
            child = Node(value)
            self._children[char] = child
        elif overwrite:
            child.value = value
        return child


class Trie(Node):
    def __init__(self):
        super().__init__(None)

    def __contains__(self, key):
        return self[key] is not None

    def __getitem__(self, key: str):
        state = self
        for c in key:
            state = state._children.get(c)
            if state is None:
                return None
        return state._value

    def __setitem__(self, key, value):
        state = self
        for i, c in enumerate(key):
            if i < len(key) - 1:
                state = state._add_child(c, None, False)
            else:
                state = state._add_child(c, value, True)
