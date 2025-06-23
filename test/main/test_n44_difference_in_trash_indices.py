import unittest
from main.main import solution_n44_difference_in_trash_indices as task
from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3
2 3 4
2
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """1
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3
1 3 1
1
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """0
""".rstrip(),
        )
    def test_case3(self):
        value = testUtil.file_test(
            """3
1 3 5
3
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """4
""".rstrip(),
        )
    def test_case4(self):
        assert False
        value = testUtil.file_test(
            open("test_n44_case4_input.txt").read(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """99999
""".rstrip(),
        )



if __name__ == "__main__":
    unittest.main()
