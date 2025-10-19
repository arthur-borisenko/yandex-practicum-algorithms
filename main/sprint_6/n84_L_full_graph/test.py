from utils import testUtil
import main.sprint_6.n84_L_full_graph.solution as task


import unittest

from utils import testUtil




class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """4 6
1 2
2 2
2 3
2 4
3 4
4 3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """NO
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3 5
1 2
2 1
3 1
2 3
3 3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """YES
""",
        )


if __name__ == "__main__":
    unittest.main()
