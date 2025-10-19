from utils import testUtil
import main.sprint_6.n79_C_graph_dfs.solution as task


import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """4 4
3 2
4 3
1 4
1 2
3
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3 2 1 4
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """2 1
1 2
1
""",
            task.main,
        )
        self.assertEqual(value.rstrip(), "1 2")


if __name__ == "__main__":
    unittest.main()
