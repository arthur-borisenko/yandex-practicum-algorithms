import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def children(node):
    c = []
    if node.left is not None:
        c.append(node.left)
    if node.right is not None:
        c.append(node.right)
    return c


class Stack:
    """Basic list-based unknown-size stack - supports push, pop, peek, iterate from top."""

    def __init__(self):
        self._len = 0
        self._data = []

    def push(self, item):
        if len(self._data) == self._len:
            self._data.append(item)
        else:
            self._data[self._len] = item
        self._len += 1

    def pop(self):
        if self._len == 0:
            raise IndexError("Stack underflow")
        res = self.peek()
        self._len -= 1
        return res

    def peek(self):
        if self._len == 0:
            raise IndexError("Attempted to get element of empty stack")
        return self._data[self._len - 1]

    def empty(self):
        return self._len == 0

    def __bool__(self):
        return len(self) > 0

    def __iter__(self):
        class _Iterator:
            def __init__(self, stack):
                self._stack = stack
                self._index = stack._len - 1

            def __next__(self):
                if self._index < 0:
                    raise StopIteration
                res = self._stack._data[self._index]
                self._index -= 1
                return res

        return _Iterator(self)

    def __len__(self):
        return self._len


def dfs(root):
    stack = Stack()
    node = root
    stack.push(node)
    while not stack.empty():
        node = stack.pop()
        yield node.value
        for node in children(node):
            stack.push(node)


def solution(root) -> int:
    return max(dfs(root))


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == "__main__":
    test()
