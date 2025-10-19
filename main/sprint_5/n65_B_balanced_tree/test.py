from utils import testUtil
import unittest


import main.sprint_5.n65_B_balanced_tree.solution  as solution


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class TestCase(unittest.TestCase):
    def test1(self):
        node1 = Node(1)
        node2 = Node(-5)
        node3 = Node(3, node1, node2)
        node4 = Node(10)
        node5 = Node(2, node3, node4)
        assert solution.solution(node5)

    def test2(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node2.right = node3
        node2.left = node1
        node3.right = node5
        node5.left = node4
        assert not solution.solution(node2)
