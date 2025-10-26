from utils import testUtil
import main.sprint_3.n33_E_1_pokupka_domov_sort.solution as task


import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3 300
999 999 999""",
            task.main,
        )
        self.assertEqual(
            value,
            """0
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3 1000
350 999 200
""",
            task.main,
        )
        self.assertEqual(
            value,
            """2
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            f"""100000 100000
{("1 "*100000).strip()}
""",
            task.main,
        )
        self.assertEqual(
            value,
            """100000
""",
        )


if __name__ == "__main__":
    unittest.main()
