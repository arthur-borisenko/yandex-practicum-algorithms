import main.sprint_3_final.solution_n45_search_in_broken_array as sol
import random
import unittest


class TestCase(unittest.TestCase):
    def test_from_template(self):
        arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
        assert sol.broken_search(arr, 5) == 6

    def test_random(self):
        n = 10
        init_array = random.sample(range(n * 10), n)
        init_array = sorted(init_array)
        broken_index = random.randint(0, len(init_array) - 1)
        broken_array = init_array[broken_index:]
        broken_array.extend(init_array[:broken_index])
        target_i = random.randint(0, len(init_array) - 1)
        target = broken_array[target_i]
        assert sol.broken_search(broken_array, target) == target_i


if __name__ == "__main__":
    unittest.main()
