import unittest


import sprint_5.n67_M_sift_up.solution as task


class TestCase(unittest.TestCase):
    def test(self):
        sample = [-1, 12, 6, 8, 3, 15, 7]
        assert task.sift_up(sample, 5) == 1
