import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0, size=0):
            self.right = right
            self.left = left
            self.value = value
            self.size = size


def direction(node, k):
    if node.size < k:
        return "NE"
    elif node.size == k:
        return "stop"
    elif node.left is not None and node.left.size >= k:
        return "left"
    else:
        return "right"


def _split(parent_root, parent, root, k):
    node = root
    if direction(node, k) == "NE":
        return root, None
    elif direction(node, k) == "stop":
        if parent is None:
            return root, None
        else:
            if parent.left == root:
                parent.left = None
            else:
                parent.right = None
            return node, parent_root
    elif direction(node, k) == "left":
        return _split(parent_root, node, node.left, k)
    else:
        return _split(parent_root, node, node.right, k)


def split(root, k):
    stack = Stack()
    pass


def test():
    node1 = Node(None, None, 3, 1)
    node2 = Node(None, node1, 2, 2)
    node3 = Node(None, None, 8, 1)
    node4 = Node(None, None, 11, 1)
    node5 = Node(node3, node4, 10, 3)
    node6 = Node(node2, node5, 5, 6)
    left, right = split(node6, 4)
    assert left.size == 4
    assert right.size == 2


if __name__ == "__main__":
    test()
