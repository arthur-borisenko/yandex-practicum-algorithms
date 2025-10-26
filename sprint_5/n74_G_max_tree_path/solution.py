import os


LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def get_parents_mapping(root):
    stack = Stack()
    parents_map = {}
    node = root
    stack.push(node)
    parents_map[node] = None
    while not stack.isEmpty():
        node = stack.pop()
        for node1 in [node.left, node.right]:
            if node1 is None:
                continue
            parents_map[node1] = node
            if node1 is None:
                continue
            stack.push(node1)
    return parents_map


def _s(root, pm, prev=None):
    nodes_to_visit = []
    end = True
    if root.left is not None and root.left is not prev:
        nodes_to_visit.append(root.left)
        end = False
    if root.right is not None and root.right is not prev:
        nodes_to_visit.append(root.right)
        end = False
    if pm[root] is not None and pm[root] is not prev:
        nodes_to_visit.append(pm[root])
        end = False
    if end:
        return root.value
    variants = []
    for node in nodes_to_visit:
        variants.append(_s(node, pm, root))
    return max(max(variants) + root.value, root.value)


def solution(root) -> int:
    pm = get_parents_mapping(root)
    variants = []
    for node in pm.keys():
        variants.append(_s(node, pm))
    return max(variants)
    #  “ヽ(´▽｀)ノ”


def test():
    node1 = Node(5, None, None)
    node2 = Node(1, None, None)
    node3 = Node(-3, node2, node1)
    node4 = Node(2, None, None)
    node5 = Node(2, node4, node3)
    assert solution(node5) == 6


if __name__ == "__main__":
    test()
