from utils import testUtil
import main.sprint_3.n31_C_sequence.solution as task


import unittest

from utils import testUtil




class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """abc
ahbgdcu
""",
            task.main,
        )
        self.assertEqual(
            value,
            """True
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """qtqkcxytpoptpinnnzsywdkcxcevafs
hzwgejxespojukkupeiwxlnuojaoqrqrfgkccwtxukshxnldgxoeldgewtbqjdqmmelmlmtkfzhvxysbjkdqfhqwtmylrqtjocwnyxilzlzfzxshgdliuwszkksgqrzalmmznnwpijvgwyegtinhrueviqufjizbpzxpfqqvjytvxbvaqunumkclcdzhnawkxilubfzisberzvspunknmvvgkjilmgffefklsjgjugrccfpmxwemnzvsynhfjgskfgcdqmkawuhjbvvicevhlqrqlwghumqgvbdvujqmzygbvycqmoaqmodwjrwcootijhxehabnacmzcyjpyldqgrkplshelszsqluyafqqwvbkfbchpfvyregezibwsrfulueikahthpbnurkgedshtnedeqmpmcikxxwvttebkwblqvagtgsgxiegcmhimeeyeapecjszpwdruwtrxqobfnkieeaxsyxjxbvvjbgutrmhbdhoofquqxutmswffpuuuyurkrgmovdbdavkwfoedvqaimkgkvvqkzjvzmznmbcpxfoxteezivyhnxryculurbflolhvbiwsmgfzhkunrpbzqfqvdojjksbepfighundadzvhcdhuwegqbqyhcociehxlqgecnxpcufzveosrmfnlevgjlxazwmbwyaxcffxhihdekzyxnplxoazfdvsjtbopkwebmuocdagmgtqttgximtjlaigootdddpeqefwuizrcuzzzzzmmwinbdwtukpydrrgvzogexutcyofkdyclsktdiqdcvxpmfqbslshwkpoiyjtiokmgytnbbbvfqoqtiutzexccmdhxuzmfdtfmmtboizpfzatllnpjctwlkjqybhafavopqgtbiyxvzlvfhirdultyiamrobylmiisddmnqvqcbxtknznavv
""",
            task.main,
        )
        self.assertEqual(
            value,
            """True
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            f"""{"".join(map(str,range(149999)))}
{"".join(map(str,range(150000)))}
""",
            task.main,
        )
        self.assertEqual(
            value,
            """True
""",
        )


if __name__ == "__main__":
    unittest.main()
