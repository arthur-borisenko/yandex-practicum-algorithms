from main.main.sprint_5_final import solution_n76_remove_node as task
import unittest


Node = task.Node


class TestCase(unittest.TestCase):
    def test(self):
        node1 = Node(None, None, 2)
        node2 = Node(node1, None, 3)
        node3 = Node(None, node2, 1)
        node4 = Node(None, None, 6)
        node5 = Node(node4, None, 8)
        node6 = Node(node5, None, 10)
        node7 = Node(node3, node6, 5)
        new_head = task.remove(node7, 10)
        self.assertEqual(new_head.value, 5)
        self.assertIs(new_head.right, node5)
        self.assertEqual(new_head.right.value, 8)


if __name__ == "__main__":
    unittest.main()
