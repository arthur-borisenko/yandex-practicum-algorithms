import math
import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root, ma=math.inf, mi=-math.inf) -> bool:
    if not mi < root.value < ma:
        return False
    if root.left is None and root.right is None:
        return True
    elif root.left is not None and root.right is None:
        return (
            solution(root.left, ma=min(root.value, ma), mi=mi)
            and root.value > root.left.value
        )
    elif root.right is not None and root.left is None:
        return (
            solution(root.right, mi=max(root.value, mi), ma=ma)
            and root.value <= root.right.value
        )
    else:
        return (
            solution(root.left, ma=min(root.value, ma), mi=mi)
            and solution(root.right, mi=max(root.value, mi), ma=ma)
            and root.left.value < root.value <= root.right.value
        )


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == "__main__":
    test()
