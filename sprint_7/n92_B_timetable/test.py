import unittest


import sprint_7.n92_B_timetable.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5
9.0 10.0
9.3 10.3
10.0 11.0
10.3 11.3
11.0 12.0

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3
9.0 10.0
10.0 11.0
11.0 12.0

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3
9.0 10.0
11.0 12.25
12.15 13.3

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2
9.0 10.0
11.0 12.25

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """7
19.0 19.0
7.0 14.0
12.0 14
8.0 22.0
22.0 23.0
5.0 21.0
9.0 23.0

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3
7.0 14.0
19.0 19.0
22.0 23.0

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
