import unittest
from main.free_learning.ciphers import solution_shift_cipher as solution


class TestPermutationsCipher(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(
            "".join(
                solution.encrypt(
                    "умзаключаетсянетольковзнанииноивуменииприлагатьзнаниенаделе", 7
                )
            ),
            "ъуожстеюжлщшёфлщхтгсхиофжфппфхпиъулфппцчптжйжщгофжфплфжклтл",
        )

    def test_decrypt(self):
        self.assertEqual(
            "".join(
                solution.decrypt(
                    "ъуожстеюжлщшёфлщхтгсхиофжфппфхпиъулфппцчптжйжщгофжфплфжклтл", 7
                )
            ),
            "умзаключаетсянетольковзнанииноивуменииприлагатьзнаниенаделе",
        )
