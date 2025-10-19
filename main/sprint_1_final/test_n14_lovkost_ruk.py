import unittest
from main.sprint_1_final import solution_n14_lovkost_ruk as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3
1231
2..2
2..2
2..2
""",
            task.main,
        )
        self.assertEqual(
            value,
            """2
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """4
1111
9999
1111
9911
""",
            task.main,
        )
        self.assertEqual(
            value,
            """1
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            """5
1111
1111
1111
1111
""",
            task.main,
        )
        self.assertEqual(
            value,
            """0
""",
        )

    def test_time(self):
        import time

        start_time = time.process_time()
        value = testUtil.file_test(
            """4
1111
9999
1111
9911
""",
            task.main,
        )
        sol_time = time.process_time() - start_time
        self.assertEqual(
            value,
            """1
""",
        )
        self.assertLess(sol_time, 1)


if __name__ == "__main__":
    unittest.main()
