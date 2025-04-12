from main.main import solution_n23_bordered_queue as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """8
2
peek
push 5
push 2
peek
size
size
push 1
size
""",
            task.main,
        )
        self.assertEqual(
            value,
            """None
5
2
2
error
2
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """10
1
push 1
size
push 3
size
push 1
pop
push 1
pop
push 3
push 3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """1
error
1
error
1
1
error
""",
        )


if __name__ == "__main__":
    unittest.main()
