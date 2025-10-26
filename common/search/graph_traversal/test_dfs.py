import unittest
from common.search.graph_traversal.dfs import dfs


class TestCase(unittest.TestCase):
    def test(self):
        rm = {
            1: {2: 1, 3: 1},
            2: {1: 1, 3: 1, 4: 1, 5: 1},
            3: {6: 1, 7: 1, 8: 1, 9: 1, 10: 1},
        }
        self.assertListEqual(list(dfs(1, rm)), [1, 2, 3, 6, 7, 8, 9, 10, 4, 5])
