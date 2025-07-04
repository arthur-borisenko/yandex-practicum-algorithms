import unittest
from main.main import solution_n47_circles as task
from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """8
вышивание крестиком
рисование мелками на парте
настольный керлинг
настольный керлинг
кухня африканского племени ужасмай
тяжелая атлетика
таракановедение
таракановедение
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """вышивание крестиком
рисование мелками на парте
настольный керлинг
кухня африканского племени ужасмай
тяжелая атлетика
таракановедение
""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
