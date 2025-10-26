import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if not LOCAL:
    from node import Node

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def insert(root, key) -> Node:
    """CPU - O(h)
    RAM - O(1)"""
    r = root
    while root is not None:
        if key < root.value:
            if root.left is not None:
                root = root.left
            else:
                root.left = Node(value=key)
                return r
        elif key >= root.value:
            if root.right is not None:
                root = root.right
            else:
                root.right = Node(value=key)
                return r
    return Node(value=key)


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == "__main__":
    test()
