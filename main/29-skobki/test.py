import unittest
from task import main
from utils.testUtil import file_test
import task


class Test(unittest.TestCase):
    def test_case1(self):
        res = file_test(
            """3
        """,
            task.main,
        )
        self.assertEqual(
            res,
            """((()))
(()())
(())()
()(())
()()()
""",
        )

    def test_case2(self):
        res = file_test(
            """2
        """,
            task.main,
        )
        self.assertEqual(
            res,
            """(())
()()
""",
        )

    def test_case3(self):
        res = file_test(
            """1
""",
            task.main,
        )
        self.assertEqual(
            res,
            """()
""",
        )
