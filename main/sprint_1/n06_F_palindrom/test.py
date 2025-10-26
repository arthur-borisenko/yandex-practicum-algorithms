import unittest
import main.sprint_1.n06_F_palindrom.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """A man, a plan, a canal: Panama

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """True
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """zo

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """False
""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
