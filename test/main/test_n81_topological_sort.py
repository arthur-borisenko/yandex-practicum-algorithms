from io import StringIO

from main.main import solution_n81_topological_sort as task
import unittest

from test.utils import testUtil


def connections(vertex, ribbles_map):
    ribbles_for_node = ribbles_map.get(vertex, {})
    for second in sorted(ribbles_for_node.keys(), reverse=True):
        yield second


class TestCase(unittest.TestCase):
    @staticmethod
    def _test(inp):
        out = testUtil.file_test(inp, task.main)
        inp_io = StringIO(inp)
        m = {}
        n, k = map(int, inp_io.readline().split())
        for i in range(k):
            ribble = inp_io.readline()
            v1, v2 = map(int, ribble.split())
            m[v1] = m.get(v1, {})
            m[v2] = m.get(v2, {})
            m[v1][v2] = 1
        data = list(map(int, out.split()))
        if len(data) != n:
            print(
                f"""Failed.
Input data was:
{inp}
Output data was:
{out}"""
            )
            return False
        visited = set()
        for v in data:
            for r in connections(v, m):
                if r in visited:
                    print(
                        f"""Failed.
Input data was:
{inp}
Output data was:
{out}"""
                    )
                    return False
            visited.add(v)
        return True

    def test_case1(self):
        assert self._test(
            """5 3
3 2
3 4
2 5
"""
        )

    def test_case2(self):
        assert self._test(
            """6 3
6 4
4 1
5 1
"""
        )

    def test_case3(self):
        assert self._test("4 0")


if __name__ == "__main__":
    unittest.main()
