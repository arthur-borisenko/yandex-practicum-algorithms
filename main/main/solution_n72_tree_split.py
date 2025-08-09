import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0, size=0):
            self.right = right
            self.left = left
            self.value = value
            self.size = size

        def __repr__(self):
            return "Node({}, {})".format(self.value, self.size)


def action(node, k):
    if node.size < k:
        return "not_enough"
    elif node.size == k:
        return "take_node_with_all_subtrees"
    elif node.left is not None and node.left.size >= k:
        return "move_left"
    else:
        return "take_node_with_left_subtree_and_move_right"


def size(node):
    return node.size if node is not None else 0


def update_size(node):
    node.size = size(node.left) + size(node.right) + 1


def qbdsib(root, k):
    node = root
    # cases:
    # take node and left subtree = size(node.left) + 1 == k
    # take node, left subtree and part of its right subtree = size(node.left) + 1 < k
    # take node and all its subtrees = root.size == k
    # move left = root.left.size>=k
    # not enough = root.size < k
    # left subtree always taken fully, except move left
    if size(node) < k:  # not enough
        return node, None
    elif size(node) == k:  # take node and all its subtrees
        return node, None
    elif size(node.left) + 1 == k:  # take node and left subtree
        right = node.right
        node.right = None
        update_size(node)
        return node, right
    elif (
        size(node.left) + 1 < k
    ):  # take node, left subtree and part of its right subtree
        k_to_take_from_right = k - size(node.left) - 1
        left_root, right_root = qbdsib(node.right, k_to_take_from_right)
        node.right = left_root
        update_size(node)
        return node, right_root
    elif size(node.left) >= k:  # move left
        left_root, right_root = qbdsib(node.left, k)
        node.left = right_root
        update_size(node)
        return left_root, node
    else:
        raise Exception("impossible case")


def split(root, k):
    x1, x2 = qbdsib(root, k)

    return (x1, x2)


def teest():
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
    teest()
