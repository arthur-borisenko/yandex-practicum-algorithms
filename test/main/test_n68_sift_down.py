import unittest
import main.main.solution_n68_sift_down as task


class TestCase(unittest.TestCase):

    def test(self):
        sample = [-1, 12, 1, 8, 3, 4, 7]
        assert task.sift_down(sample, 2) == 5
