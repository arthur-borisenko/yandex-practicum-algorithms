import unittest
import main.main.sprint_8_final.solution_n120_shpargalka as task
from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """examiwillpasstheexam
5
will
pass
the
exam
i

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """YES

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """abacaba
2
abac
caba

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """NO

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """abacaba
3
abac
caba
aba

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """YES

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
