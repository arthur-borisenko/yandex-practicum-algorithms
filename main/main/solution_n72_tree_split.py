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


def qbdsib(root, k):
    node = root
    if root.size <= k:
        return root, None
    parent = None
    while node.left is not None and node.left.size > k:
        parent = node
        node = node.left
    if node.left.size == k:
        root1 = node.left
        node.left = None
        return root1, root
    else:
        root1, root2 = qbdsib(node.right, k - node.left.size - 1)
        node.right = root1
        parent.left = root2
        return node, root


def split(root, k):
    x1, x2 = qbdsib(root, k)

    return x


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
