from utils import testUtil
import unittest


import main.sprint_5.n64_K_print_range.solution as task


class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


class TestCase(unittest.TestCase):
    def test_case1(self):
        node1 = Node(None, None, 2)
        node2 = Node(None, node1, 1)
        node3 = Node(None, None, 8)
        node4 = Node(None, node3, 8)
        node5 = Node(node4, None, 9)
        node6 = Node(node5, None, 10)
        node7 = Node(node2, node6, 5)
        value = testUtil.file_test(
            """""",
            lambda: task.print_range(node7, 2, 8),
        )
        self.assertEqual(
            value,
            """2 5 8 8
""",
        )


if __name__ == "__main__":
    unittest.main()
