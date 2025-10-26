from utils import testUtil
import main.sprint_1.n09_I_stepen_4.solution as task


import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """16
""",
            task.main,
        )
        self.assertEqual(
            value,
            """True
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """15
            """,
            task.main,
        )
        self.assertEqual(
            value,
            """False
""",
        )


if __name__ == "__main__":
    unittest.main()
