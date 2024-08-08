import task
import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5
0 1 4 9 0
""",
            task.main,
        )
        self.assertEqual(
            value,
            """0 1 2 1 0
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """6
0 7 9 4 8 20
""",
            task.main,
        )
        self.assertEqual(
            value,
            """0 1 2 3 4 5
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            """9
98 0 10 77 0 59 28 0 94
""",
            task.main,
        )
        self.assertEqual(
            value,
            """1 0 1 1 0 1 1 0 1
""",
        )

    def test_time(self):
        import time

        input_data = f"""{10**6}
{" ".join(map(str,range(10**6)))}"""
        output = " ".join(map(str, range(10**6)))
        start_time = time.process_time()
        value = testUtil.file_test(
            input_data,
            task.main,
        )
        sol_time = time.process_time() - start_time
        self.assertEqual(
            value,
            output + "\n",
        )
        self.assertLess(sol_time, 3)


if __name__ == "__main__":
    unittest.main()
