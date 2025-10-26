import sprint_2.n20_F_stack_max.solution as task


import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """8
get_max
push 7
pop
push -2
push -1
pop
get_max
get_max
""",
            task.main,
        )
        self.assertEqual(
            value,
            """None
-2
-2
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
