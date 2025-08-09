import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0, size=0):
            self.right = right
            self.left = left
            self.value = value
            self.size = size


def size(node):
    """Gets node size if node exists, else 0"""
    return node.size if node is not None else 0


def update_size(node):
    """Updates size of node by its children. requires correct children sizes.
    CPU - O(1)
    RAM - O(1)"""
    node.size = size(node.left) + size(node.right) + 1


def split(root, k):
    """
    CPU - O(h)
    RAM - O(h)
    where h - tree height
    """
    if size(root) < k:
        return root, None
    elif size(root) == k:
        return root, None
    elif size(root.left) + 1 == k:
        right = root.right
        root.right = None
        update_size(root)
        return root, right
    elif size(root.left) + 1 < k:
        k_to_take_from_right = k - size(root.left) - 1
        left_root, right_root = split(root.right, k_to_take_from_right)
        root.right = left_root
        update_size(root)
        return root, right_root
    elif size(root.left) >= k:
        left_root, right_root = split(root.left, k)
        root.left = right_root
        update_size(root)
        return left_root, root
    else:
        raise Exception("impossible case")


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
