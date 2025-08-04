from queue import Queue


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


def solution(root) -> bool:
    r = []
    queue = Queue()
    node = root
    queue.put((node, 0))
    r.append([node.value])
    while not queue.empty():
        node, l = queue.get()
        while len(r) <= l + 1 and len(children(node)) > 0:
            r.append([])
        for child in children(node):
            queue.put((child, l + 1))

            r[l + 1].append(child.value)
    l = 1
    print(r)
    for level in r:
        if len(level) != l:
            return False
        if level != list(reversed(level)):
            return False
        l *= 2
    return True
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


def test2():
    node4 = Node(1, None, None)
    node3 = Node(1, None, None)
    node2 = Node(1, node4, None)
    node1 = Node(1, node2, node3)
    assert not solution(node1)


def test3():
    node5 = Node(3, None, None)
    node4 = Node(3, None, None)
    node3 = Node(2, None, node5)
    node2 = Node(2, node4, None)
    node1 = Node(0, node2, node3)
    assert solution(node1)


if __name__ == "__main__":
    test()
    test2()
    test3()
