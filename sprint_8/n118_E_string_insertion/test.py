import unittest


import sprint_8.n118_E_string_insertion.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """abacaba
3
queue 2
deque 0
stack 7

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """dequeabqueueacabastack
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """kukareku
2
p 1
q 2

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """kpuqkareku
""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
