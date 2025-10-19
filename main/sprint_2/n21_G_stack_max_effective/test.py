from utils import testUtil
import main.sprint_2.n21_G_stack_max_effective.solution as task


import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """13
pop
pop
top
push 4
push -5
top
push 7
pop
pop
get_max
top
pop
get_max
""",
            task.main,
        )
        self.assertEqual(
            value,
            """error
error
error
-5
4
4
None
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """7
get_max
pop
pop
pop
push 10
get_max
push -9
""",
            task.main,
        )
        self.assertEqual(
            value,
            """None
error
error
error
10
""",
        )


if __name__ == "__main__":
    unittest.main()
