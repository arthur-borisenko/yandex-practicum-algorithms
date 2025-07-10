import unittest
from main.main.solution_n49_strange_comparsion import solution as b


class TestCase(unittest.TestCase):

    def test1(self):
        (
            s,
            t,
        ) = """mxyskaoghi
qodfrgmslc
    """.splitlines()[
            :2
        ]
        assert b(s, t)

    def test2(self):
        (
            s,
            t,
        ) = """agg
xdd
    """.splitlines()[
            :2
        ]
        assert b(s, t)

    def test3(self):
        (
            s,
            t,
        ) = """agg
xda
        """.splitlines()[
            :2
        ]
        assert not b(s, t)


if __name__ == "__main__":
    unittest.main()
