import main.main.sprint_3_final.solution_n45_search_in_broken_array as sol
import random
import unittest


class TestCase(unittest.TestCase):
        def test_from_template(self):
            arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
            assert sol.broken_search(arr, 5) == 6

        def test_random(self):
            n=10
            l=random.sample(range(n*10), n)
            l=sorted(l)
            fuck=random.randint(0,len(l)-1)
            l1=l[fuck:]
            l2=l[:fuck]
            l1.extend(l2)
            target_i=random.randint(0, len(l) - 1)
            target=l1[target_i]
            assert sol.broken_search(l1, target)==target_i
if __name__ == "__main__":
    unittest.main()