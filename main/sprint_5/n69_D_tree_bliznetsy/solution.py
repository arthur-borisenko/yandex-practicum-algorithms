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


def dfs(root):
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
        for node in [node.left, node.right]:
            stack.push(node)
    return res


import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root1, root2) -> bool:
    return list(dfs(root1)) == list(dfs(root2))
    #  “ヽ(´▽｀)ノ”


def test():
    node1 = Node(1, None, None)
    node2 = Node(2, None, None)
    node3 = Node(3, node1, node2)

    node4 = Node(1, None, None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)

    assert solution(node3, node6)


if __name__ == "__main__":
    test()
