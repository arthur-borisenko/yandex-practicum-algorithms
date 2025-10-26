from utils import testUtil
import unittest


import main.sprint_7.n99_N_gosha_in_restaurant.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3
500
501
300

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """1001 1
3
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """4
502
501
503
504
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """1003 2
3 4
""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
