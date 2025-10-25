import unittest
import main.sprint_8.final.solution_n119_packed_prefix as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3
2[a]2[ab]
3[a]2[r2[t]]
a2[aa3[b]]

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """aaa

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3
abacabaca
2[abac]a
3[aba]

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """aba

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
