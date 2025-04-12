import unittest
from main.free_learning.ciphers import solution_permutations_cipher as solution


class TestPermutationsCipher(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(
            "".join(
                solution.encrypt(
                    [2, 5, 9, 3, 1, 8, 4, 7, 10, 6],
                    "УМ ЗАКЛЮЧАЕТСЯ НЕ ТОЛЬКО В ЗНАНИИ, НО И В УМЕНИИ ПРИЛАГАТЬ ЗНАНИЕ НА ДЕЛЕ",
                )
            ),
            "КЕАЕААУТОИИНАННМГНЮОИИЬЕМСВВЛИЕКОРАЧЛИИЗЛЛТННТДЗЯЗУАЕАЬНПНЕ",
        )

    def test_decrypt(self):
        self.assertEqual(
            "".join(
                solution.decrypt(
                    [2, 5, 9, 3, 1, 8, 4, 7, 10, 6],
                    "КЕАЕААУТОИИНАННМГНЮОИИЬЕМСВВЛИЕКОРАЧЛИИЗЛЛТННТДЗЯЗУАЕАЬНПНЕ",
                )
            ),
            "УМЗАКЛЮЧАЕТСЯНЕТОЛЬКОВЗНАНИИНОИВУМЕНИИПРИЛАГАТЬЗНАНИЕНАДЕЛЕ",
        )
