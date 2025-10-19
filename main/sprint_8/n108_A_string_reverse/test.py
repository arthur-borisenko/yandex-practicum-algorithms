from utils import testUtil
import unittest


import main.sprint_8.n108_A_string_reverse.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """one two three

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """three two one

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """hello

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """hello

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """may the force be with you

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """you with be force the may

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
