import sys
import time
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


def find_replacement_node(root):
    if root is None:
        return None, None
    node = root
    parent = None
    while node.right is not None:
        parent = node
        node = node.right
    return parent, node


def replace_parent_node_link(parent, node, new_node):
    if parent.left is node:
        parent.left = new_node
    else:
        parent.right = new_node
def merge_subtrees(left, right):
    replacement_node_parent, replacement_node = find_replacement_node(left)
    if replacement_node_parent is None:
        left=None
    else:
        replacement_node_parent.right = replacement_node.left
    replacement_node.left = left
    replacement_node.right = right
    return replacement_node


def remove(root, key) -> Optional[Node]:
    if root is None:
        return None
    parent, node = find_key(root, key)
    if node is None:
        return root
    if root.left is None and root.right is None:
        return None
    right = node.right
    left = node.left
    if left is None and right is None:
        replace_parent_node_link(parent, node, None)
        return root
    elif left is not None and right is not None:
        replacement_node = merge_subtrees(left, right)
        if parent is not None:
            replace_parent_node_link(parent, node, replacement_node)
        else:
            root = replacement_node
    else:
        replacement_node = right if right is not None else left
        if parent is not None:
            replace_parent_node_link(parent, node, replacement_node)
        else:
            root = replacement_node
    return root
    #  “ヽ(´▽｀)ノ”
def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8



if __name__ == "__main__":
    test()
