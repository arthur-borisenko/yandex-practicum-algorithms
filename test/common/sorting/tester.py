import unittest
import unittest.mock as mock


class SortTester(unittest.TestCase):
    def _checker(self, i, o, reverse=False):
        exp = sorted(i, reverse=reverse)
        self.assertEqual(exp, list(o))

    def _patch_sorted(self, m, *args, **kwargs):
        with mock.patch(
            "builtins.sorted",
            mock.Mock(
                side_effect=AssertionError(
                    "Built-in sorting methods may not be used in solution"
                )
            ),
        ):
            return m(*args, **kwargs)
