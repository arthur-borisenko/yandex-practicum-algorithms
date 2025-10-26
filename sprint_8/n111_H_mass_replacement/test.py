import unittest


import sprint_8.n111_H_mass_replacement.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """pingpong
ng
mpi

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """pimpipompi

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """aaa
a
ab

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """ababab

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
