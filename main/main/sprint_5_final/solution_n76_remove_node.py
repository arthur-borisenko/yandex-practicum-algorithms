from typing import Optional
import os


LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value

else:
    from node import Node


def find_key(root, key):
    node = root
    parent = None
    while node:
        if key < node.value:
            parent = node
            node = node.left
        elif key == node.value:
            return parent, node
        else:
            parent = node
            node = node.right
    return None, None


def get_rightest_node(root):
    if root is None:
        return None, None
    node = root
    parent = None
    while node.right is not None:
        parent = node
        node = node.right
    return parent if node else None, node


def remove(root, key) -> Optional[Node]:
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None if root.value == key else root
    parent, node = find_key(root, key)
    if node is None:
        return root
    right = node.right
    left = node.left
    if left is not None:
        x, node_to_replace = get_rightest_node(left)
        if x is not None:
            x.right = node_to_replace.left
            node_to_replace.left = None
        node_to_replace.right = right
        node_to_replace.left = left
    else:
        node_to_replace = right
    if parent is not None:
        if parent.left is node:
            parent.left = node_to_replace
        else:
            parent.right = node_to_replace
    else:
        root = node_to_replace
    return root
    #  “ヽ(´▽｀)ノ”


def test():
    n1 = Node(value=31)
    n2 = Node(value=624)
    n3 = Node(value=220)
    n4 = Node(value=130)
    n5 = Node(value=302)
    n6 = Node(value=442)
    n7 = Node(value=858)
    n8 = Node(value=763)
    n9 = Node(value=701)
    n10 = Node(value=867)

    n1.right = n2
    n2.left = n3
    n2.right = n7
    n3.left = n4
    n3.right = n5
    n5.right = n6
    n7.left = n8
    n7.right = n10
    n8.left = n9

    root = n1
    remove(root, 701)
    remove(root, 130)
    remove(root, 302)


if __name__ == "__main__":
    test()
