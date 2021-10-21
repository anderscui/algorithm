# coding=utf-8

class EmptyContainerError(Exception):
    """Access an element from an empty container."""
    def __init__(self, message):
        self.message = message
