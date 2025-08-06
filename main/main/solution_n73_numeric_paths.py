import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
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


def s1(root):
    res = []
    stack = Stack()
    node = root
    stack.push((node, str(node.value)))
    while not stack.isEmpty():
        node, np = stack.pop()
        if node.left is None and node.right is None:
            res.append(np)
        for node in children(node):
            stack.push((node, np + str(node.value)))
    return res


def solution(root) -> int:
    return sum(map(int, s1(root)))
    #  “ヽ(´▽｀)ノ”


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275


if __name__ == "__main__":
    test()
