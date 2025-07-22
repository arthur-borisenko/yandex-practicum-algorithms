import unittest

import main.main.sprint_4_final.solution_n58_search_system as solution
from test.utils import testUtil


class TestCase(unittest.TestCase):

    def test_case1(self):
        value = testUtil.file_test(
            """3
i love coffee
coffee with milk and sugar
free tea for everyone
3
i like black coffee without milk
everyone loves new year
mary likes black coffee without milk
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """1 2
3
2 1
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """6
buy flat in moscow
rent flat in moscow
sell flat in moscow
want flat in moscow like crazy
clean flat in moscow on weekends
renovate flat in moscow
1
flat in moscow for crazy weekends
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """4 5 1 2 3
""".rstrip(),
        )
