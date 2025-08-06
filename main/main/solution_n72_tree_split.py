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


def _acts(root, k):
    node = root
    if action(node, k) == "not_enough":
        return Node
    actions = []
    while node is not None:
        if action(node, k) == "move_left":
            node = node.left
        elif action(node, k) == "take_node_with_left_subtree_and_move_right":
            actions.append(("take_node_with_left_ST", node))
            k -= node.left.size + 1
            node = node.right
        elif action(node, k) == "take_node_with_all_subtrees":
            actions.append(("take_node_with_all_ST", node))
            k -= node.size
            node = None
        elif action(node, k) == "not_enough":
            raise Exception("500 Internal Brains Error")
        else:
            raise Exception("400 Bad Thoughts Error")
    return actions


def split(root, k):
    print(_acts(root, k))
    pass


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
