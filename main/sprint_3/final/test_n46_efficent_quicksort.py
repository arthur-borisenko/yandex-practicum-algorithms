import random
import unittest
from functools import cmp_to_key

import main.sprint_3.final.solution_n46_efficent_quicksort as solution
from utils import testUtil


class Test(unittest.TestCase):
    @staticmethod
    def cmp(a, b):
        n1, p1, f1, n2, p2, f2 = a[0], a[1], a[2], b[0], b[1], b[2]
        if p1 < p2:
            return 1
        if p1 > p2:
            return -1
        if f1 < f2:
            return -1
        if f1 > f2:
            return 1
        if n1 < n2:
            return -1
        if n1 > n2:
            return 1
        return 0

    def test_case1(self):
        value = testUtil.file_test(
            """5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80
""",
            solution.main,
        )
        self.assertEqual(
            value.strip(),
            """gena
timofey
alla
gosha
rita
""".strip().rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """5
alla 0 0
gena 0 0
gosha 0 0
rita 0 0
timofey 0 0
    """.strip().rstrip(),
            solution.main,
        )
        self.assertEqual(
            value.strip(),
            """alla
gena
gosha
rita
timofey
    """.strip(),
        )

    def test_random(self):
        n = 100
        k = 100
        for _ in range(n):
            ids = random.sample(list(map(str, range(100))), k)
            case = []
            for _id in ids:
                case.append((_id, random.randint(1, 100), random.randint(1, 100)))
            expected = sorted(case, key=cmp_to_key(self.cmp))
            l = "\n".join(map(lambda x: f"{x[0]} {x[1]} {x[2]}", case))
            value = testUtil.file_test(
                f"""{k}
            {l}""".strip().rstrip(),
                solution.main,
            )
            self.assertEqual(value.strip().split(), list(map(lambda x: x[0], expected)))
