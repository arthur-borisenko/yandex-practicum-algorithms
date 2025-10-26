from utils import testUtil
import main.sprint_6.n82_D_graph_bfs.solution as task


import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """4 4
1 2
2 3
3 4
1 4
3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """3 2 4 1
""",
        )


if __name__ == "__main__":
    unittest.main()
