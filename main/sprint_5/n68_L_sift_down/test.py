from utils import testUtil
import unittest


import main.sprint_5.n68_L_sift_down.solution as task


class TestCase(unittest.TestCase):

    def test(self):
        sample = [-1, 12, 1, 8, 3, 4, 7]
        assert task.sift_down(sample, 2) == 5
