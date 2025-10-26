import sprint_2.n17_C_nelubimoe_delo.solution as task


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
        new_head = task.solution(node0, 1)
        assert new_head is node0
        assert new_head.next_item is node2
        assert new_head.next_item.next_item is node3
        assert new_head.next_item.next_item.next_item is None

    def test_case2(self):
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)
        new_head = task.solution(node0, 3)
        assert new_head is node0
        assert new_head.next_item is node1
        assert new_head.next_item.next_item is node2
        assert new_head.next_item.next_item.next_item is None


if __name__ == "__main__":
    unittest.main()
