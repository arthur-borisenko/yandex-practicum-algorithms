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


def s(root, cf):
    res = []
    stack = Stack()
    node = root
    stack.push(node)
    while not stack.isEmpty():
        node = stack.pop()
        if node is None:
            yield None
            continue
        yield node.value
        for node in cf(node):
            stack.push(node)
    return res


def normal_cf(node):
    return [node.left, node.right]


def reversed_cf(node):
    return [node.right, node.left]


def children(node):
    c = []
    if node.left is not None:
        c.append(node.left)
    if node.right is not None:
        c.append(node.right)
    return c


def solution(root) -> bool:
    if root.left is None and root.right is None:
        return True
    elif root.left is None or root.right is None:
        return False
    else:
        return list(s(root.left, normal_cf)) == list(s(root.right, reversed_cf))
    #  “ヽ(´▽｀)ノ”


def test():
    node1 = Node(3, None, None)
    node2 = Node(4, None, None)
    node3 = Node(4, None, None)
    node4 = Node(3, None, None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)


if __name__ == "__main__":
    test()
