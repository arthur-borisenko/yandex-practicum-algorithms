import unittest


from sprint_5.n70_C_anagram_tree.solution import solution


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class TestCase(unittest.TestCase):

    def test(self):
        node1 = Node(3, None, None)
        node2 = Node(4, None, None)
        node3 = Node(4, None, None)
        node4 = Node(3, None, None)
        node5 = Node(2, node1, node2)
        node6 = Node(2, node3, node4)
        node7 = Node(1, node5, node6)
        assert solution(node7)

    def test2(self):
        node4 = Node(1, None, None)
        node3 = Node(1, None, None)
        node2 = Node(1, node4, None)
        node1 = Node(1, node2, node3)
        assert not solution(node1)

    def test3(self):
        node5 = Node(3, None, None)
        node4 = Node(3, None, None)
        node3 = Node(2, None, node5)
        node2 = Node(2, node4, None)
        node1 = Node(0, node2, node3)
        assert solution(node1)
