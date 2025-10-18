import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


class Stack:
    stack = []
    __len__ = stack.__len__

    def __init__(self):
        self.stack = []
        self.__len__ = self.stack.__len__

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            raise IndexError
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def children(node):
    c = []
    if node.left is not None:
        c.append(node.left)
    if node.right is not None:
        c.append(node.right)
    return c


def solution(root) -> int:
    stack = Stack()
    node = root
    stack.push((node, 0))
    max_depth = 0
    while not stack.isEmpty():
        node, node_depth = stack.pop()
        if len(children(node)) == 0:
            max_depth = max(node_depth, max_depth)
        for node in children(node):
            stack.push((node, node_depth + 1))
    #  “ヽ(´▽｀)ノ”
    return max_depth + 1


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5) == 3


if __name__ == "__main__":
    test()
