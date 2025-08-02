import unittest
import main.main.solution_n67_sift_up as task


class TestCase(unittest.TestCase):
    def test(self):
        sample = [-1, 12, 6, 8, 3, 15, 7]
        assert task.sift_up(sample, 5) == 1
