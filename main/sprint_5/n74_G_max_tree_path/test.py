from utils import testUtil
import unittest


from main.sprint_5.n74_G_max_tree_path.solution  import solution

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class TestCase(unittest.TestCase):
    def test(self):
        node1 = Node(5, None, None)
        node2 = Node(1, None, None)
        node3 = Node(-3, node2, node1)
        node4 = Node(2, None, None)
        node5 = Node(2, node4, node3)
        self.assertEqual(solution(node5), 6)
