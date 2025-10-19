from utils import testUtil
import main.sprint_8.n113_J_camel_case.solution as task


import unittest
from utils import testUtil




class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3
MamaMilaRamu
MamaMia
MonAmi
2
MM
MA


""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """MamaMia
MamaMilaRamu
MonAmi

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """2
AlphaBetaGgamma
AbcdBcdGggg
2
ABGG
ABG
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """AbcdBcdGggg
AlphaBetaGgamma
""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """5
WudHnagkbhfwrbci
WCUkvoxboxufsdap
jdrxomezzrpuhbgi
ZcGHdrPplfoldemu
cylbtqwuxhiveznc
3
WGHV
NKVDT
ZGHU
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """



""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
