from utils import testUtil
import main.sprint_6.n87_M_bipartite_checking.solution as task


import unittest

from utils import testUtil




class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3 2
1 2
2 3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """YES
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3 3
1 2
2 3
1 3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """NO
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            f"""6 6
1 3
2 4
2 5
3 4
4 6
5 6
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
