import sprint_2.n18_D_zabotlivaya_mama.solution as task


import unittest


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def parse_input(data):
    prev_node = Node(data[0])
    res_node = prev_node
    for node in data[1:]:
        current_node = Node(node)
        prev_node.next_item = current_node
        prev_node = current_node

    return res_node


class TestCase(unittest.TestCase):
    def test_case1(self):
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)
        idx = task.solution(node0, "node2")
        assert idx == 2

    def test_case2(self):
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)
        idx = task.solution(node0, "node0")
        assert idx == 0

    def test_case3(self):
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)
        idx = task.solution(node0, "node3")
        assert idx == 3


if __name__ == "__main__":
    unittest.main()
