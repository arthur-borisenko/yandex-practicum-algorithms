import unittest


import sprint_5.n62_E_search_tree.solution as solution


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class TestCase(unittest.TestCase):
    def test(self):
        node1 = Node(1, None, None)
        node2 = Node(4, None, None)
        node3 = Node(3, node1, node2)
        node4 = Node(8, None, None)
        node5 = Node(5, node3, node4)

        assert solution.solution(node5)
        node2.value = 5
        assert not solution.solution(node5)
