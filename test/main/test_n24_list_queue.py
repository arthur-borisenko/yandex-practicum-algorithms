from main.main import solution_n24_list_queue as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """10
put -34
put -23
get
size
get
size
get
get
put 80
size
""",
            task.main,
        )
        self.assertEqual(
            value,
            """-34
1
-23
0
error
error
1
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """9
get
size
put 74
get
size
put 90
size
size
size
""",
            task.main,
        )
        self.assertEqual(
            value,
            """error
0
74
0
1
1
1
""",
        )


if __name__ == "__main__":
    unittest.main()
