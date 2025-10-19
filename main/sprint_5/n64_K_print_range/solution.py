import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def solution(node, l, r):
    result = []
    if node.left is not None and l <= node.value:
        result.extend(solution(node.left, l, r))
    if l <= node.value <= r:
        result.append(node.value)
    if node.right is not None and node.value <= r:
        result.extend(solution(node.right, l, r))
    return result


def print_range(node, l, r):
    with open("output.txt", "w") as f:
        print(*solution(node, l, r), file=f)
    #  “ヽ(´▽｀)ノ”
    pass


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8


if __name__ == "__main__":
    test()
