from main.main import solution_n16_spisok_del as task
import unittest

from test.utils import testUtil


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
        inp = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
        value, ret = testUtil.special_file_test(
            None,
            task.solution,
            parse_input(inp),
        )
        self.assertEqual(
            value.strip().split(),
            inp,
        )

    def test_case2(self):
        inp = ["Learning", "Linked", "List"]
        value, ret = testUtil.special_file_test(
            None,
            task.solution,
            parse_input(inp),
        )
        self.assertEqual(
            value.strip().split(),
            inp,
        )


if __name__ == "__main__":
    unittest.main()
