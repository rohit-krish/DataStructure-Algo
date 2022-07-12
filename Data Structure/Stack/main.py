# OVERFLOW UNDERFLOW

# we can implement stack using list but its a dynamic array so won't be so efficient

from collections import deque


class Stack:
    def __init__(self) -> None:
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
