import sprint_5.n61_A_lightbulbs.solution as task


import unittest


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class TestCase(unittest.TestCase):
    def test(self):
        node1 = Node(1)
        node2 = Node(-5)
        node3 = Node(3, node1, node2)
        node4 = Node(2, node3, None)
        assert task.solution(node4) == 3
