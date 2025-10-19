from utils import testUtil
import unittest


import main.sprint_8.n116_F_frequent_word.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5
caba
aba
caba
abac
aba

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """aba

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3
b
bc
bcd

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """b

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """10
ciwlaxtnhhrnenw
ciwnvsuni
ciwaxeujmsmvpojqjkxk
ciwnvsuni
ciwnvsuni
ciwuxlkecnofovq
ciwuxlkecnofovq
ciwodramivid
ciwlaxtnhhrnenw
ciwnvsuni
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """ciwnvsuni

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
