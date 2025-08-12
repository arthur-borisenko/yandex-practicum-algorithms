from main.main.sprint_5_final import solution_n75_heapsort as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80""",
            task.main,
        )
        self.assertEqual(
            value,
            """gena
timofey
alla
gosha
rita
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """5
alla 0 0
gena 0 0
gosha 0 0
rita 0 0
timofey 0 0
""",
            task.main,
        )
        self.assertEqual(
            value,
            """alla
gena
gosha
rita
timofey
""",
        )


if __name__ == "__main__":
    unittest.main()
