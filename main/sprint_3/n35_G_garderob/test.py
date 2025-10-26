from utils import testUtil
import main.sprint_3.n35_G_garderob.solution as task


import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """7
0 2 1 2 0 0 1""",
            task.main,
        )
        self.assertEqual(
            value,
            """0 0 0 1 1 2 2
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """5
2 1 2 0 1
""",
            task.main,
        )
        self.assertEqual(
            value,
            """0 1 1 2 2
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            f"""6
2 1 1 2 0 2
""",
            task.main,
        )
        self.assertEqual(
            value,
            """0 1 1 2 2 2
""",
        )


if __name__ == "__main__":
    unittest.main()
