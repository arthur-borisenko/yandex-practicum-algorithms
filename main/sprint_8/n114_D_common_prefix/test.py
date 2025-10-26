from utils import testUtil
import unittest


import main.sprint_8.n114_D_common_prefix.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3
abacaba
abudabi
abcdefg

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """2
tutu
kukuku

""".rstrip(),
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
qwe
qwerty
qwerpy

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
