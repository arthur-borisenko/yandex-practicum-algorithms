import random
import time
import unittest

import main.common.structures.hashmap as hashmap


class TestCase(unittest.TestCase):
    def test_random_data(self):
        exp = {}
        real = hashmap.HashMap()
        ks = set()
        t_start = time.time()
        for i in range(100000):
            k = random.randint(0, 10000)
            v = random.randint(0, 10000)
            ks.add(k)
            exp[k] = v
            real[k] = v

        for i in range(100):
            k = random.choice(list(ks))
            del exp[k]
            del real[k]
            ks.remove(k)
        t_end = time.time()
        for k in ks:
            self.assertEqual(
                real[k],
                exp[k],
                f"for key {k} expected value {exp[k]}, but got {real[k]}",
            )
        self.assertSetEqual(set(real.keys()), set(exp.keys()))
        self.assertSetEqual(set(real.values()), set(exp.values()))
        print("OK")


if __name__ == "__main__":
    unittest.main()
