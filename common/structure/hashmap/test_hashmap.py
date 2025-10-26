import math
import random
import time
import unittest

import common.structure.hashmap.hashmap as hashmap


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        exp = {}
        for i in range(200000):
            k = random.randint(0, 10000)
            v = random.randint(0, 10000)
            exp[k] = v
        kvs_to_add = list(exp.items())
        ks_to_del = random.sample(list(exp.keys()), 1000)
        for k in ks_to_del:
            del exp[k]
        expected_keys = list(exp.keys())
        cls.random_test_data = (kvs_to_add, ks_to_del, expected_keys, exp)
        exp = {}
        for i in range(2000000):
            exp[i] = i * 100
        kvs_to_add = list(exp.items())
        for i in range(200000):
            kvs_to_add.append((i, i * 10))
            exp[i] = i * 10
        ks_to_del = list(range(100000))
        for key in ks_to_del:
            del exp[key]
        expected_keys = list(exp.keys())
        cls.range_test_data = (kvs_to_add, ks_to_del, expected_keys, exp)

    def _test(self, test_instance, data, time_msg):
        real = test_instance
        kvs_to_add, ks_to_del, expected_keys, exp = data

        t_start = time.time()

        for key, value in kvs_to_add:
            real[key] = value
        for key in ks_to_del:
            del real[key]
        for k in expected_keys:
            self.assertEqual(
                real[k],
                exp[k],
                f"for key {k} expected value {exp[k]}, but got {real[k]}",
            )

        self.assertEqual(
            len(real),
            len(exp),
            f"expected length of {len(exp)} items, but got {len(real)} items",
        )
        self.assertSetEqual(set(real.keys()), set(exp.keys()))
        self.assertSetEqual(set(real.values()), set(exp.values()))
        t_end = time.time()
        print()
        print(f"Elapsed time for {time_msg}: {t_end - t_start}")
        print()

    def test_random(self):
        test_instance = hashmap.HashMap()
        self._test(test_instance, self.random_test_data, "random")

    def test_random_without_rehash(self):
        test_instance = hashmap.HashMap()
        test_instance.BS = math.inf
        self._test(test_instance, self.random_test_data, "random without rehash")

    def test_range(self):
        test_instance = hashmap.HashMap()
        self._test(test_instance, self.range_test_data, "range")

    def test_range_without_rehash(self):
        test_instance = hashmap.HashMap()
        test_instance.BS = math.inf
        self._test(test_instance, self.range_test_data, "range without rehash")


if __name__ == "__main__":
    unittest.main()
