import unittest


import sprint_5.n66_J_insert_element.solution as solution


class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


class TestCase(unittest.TestCase):

    def test(self):
        node1 = Node(None, None, 7)
        node2 = Node(node1, None, 8)
        node3 = Node(None, node2, 7)
        new_head = solution.insert(node3, 6)
        assert new_head is node3
        assert new_head.left.value == 6
