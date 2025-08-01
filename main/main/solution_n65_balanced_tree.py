import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def _solution(node):
    h = 1
    ok = True
    if node.left is not None and node.right is None:
        lh, left_ok = _solution(node.left)
        h=lh+1
        ok = ok and left_ok and lh <= 1
    if node.left is None and node.right is not None:
        rh, right_ok = _solution(node.right)
        h=rh+1
        ok = ok and right_ok and rh <= 1
    if node.left is not None and node.right is not None:
        lh, left_ok = _solution(node.left)
        rh, right_ok = _solution(node.right)
        h=max(lh, rh)+1
        ok = ok and left_ok and right_ok and abs(lh - rh) <= 1
    return h, ok


def solution(root) -> bool:
    cnt, ok = _solution(root)
    return ok
    #  “ヽ(´▽｀)ノ”


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == "__main__":
    test()
