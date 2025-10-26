import array as arr
from typing import Iterable


def array_iterator(array):
    for i in range(len(array)):
        yield array[i]


class Binary:
    """Base binary number.
    Currently supported:
    create - O(log(n))
    str - O(n)
    int-O(1)
    bool - O(1)
    equal - O(?)
    add - O(n)"""

    @staticmethod
    def _addBinaryDigits(a, b):
        """

        :param a:
        :param b:
        :return:
        """
        if a and b:
            return True, False
        if ((not a) and b) or ((not b) and a):
            return False, True
        else:
            return False, False

    def _addBinaryDigitsAnd2stCharge(self, a, b, cin):
        ab2nd, ab1st = self._addBinaryDigits(a, b)
        abc2nd, abc1st = self._addBinaryDigits(ab1st, cin)
        return abc2nd or ab2nd, abc1st

    @staticmethod
    def parseint(value):
        """convert base 10 integer to binary ARRAY"""
        sign = 1
        if value < 0:
            sign = 0
            value = -value
        current_power = 0
        while 2**current_power <= value:
            current_power += 1
        if current_power == 0:
            current_power = 1
        res = arr.array(
            "B",
            [0] * (current_power + 1),
        )
        current_power = 0
        while 2**current_power <= value:
            if value % 2 ** (current_power + 1) != 0:
                value -= 2**current_power
                res[-current_power - 1] = 1
            current_power += 1
        return res, sign

    def set_value(self, sign, value):
        self._value = arr.array("B", value)
        self._sign = sign

    def __add__(self, other):
        if isinstance(other, str):
            other = Binary(other)
        elif isinstance(other, Binary):
            pass
        else:
            raise TypeError("other must be Binary or str")
        if len(self._value) != len(other._value):
            longest_num = max([self._value, other._value], key=lambda x: len(x))
            shortest_num = min([self._value, other._value], key=lambda x: len(x))
        else:
            longest_num = self._value
            shortest_num = other._value
        _next = False
        res = arr.array("B", [0] * (len(longest_num) + 1))
        for i, digit_1 in enumerate(reversed(longest_num)):
            digit_2 = 0
            if i < len(shortest_num):
                digit_2 = shortest_num[-i - 1]
            summ = self._addBinaryDigitsAnd2stCharge(digit_1 == 1, digit_2 == 1, _next)
            _next, val = summ
            res[i] = 1 if val else 0
        if _next:
            res[-1] = 1
        sign = self._sign == other._sign
        num = Binary()
        num.set_value(1 if sign else 0, tuple(reversed(res)))
        return num

    def __radd__(self, other):
        return self.__add__(other)

    def __init__(self, value=None):
        if value is None:
            self._value = None
        elif isinstance(value, Binary):
            self._sign = value._sign
            self._value = value._value
        elif isinstance(value, str):
            self._value, self._sign = self.parseint(int(value))
        else:
            raise TypeError("value must be Binary or str")

    def __eq__(self, other):
        if isinstance(other, str):
            other_value = Binary(other)._value
        elif isinstance(other, Binary):
            other_value = other._value
        else:
            raise TypeError("other must be Binary or str")
        return self._value == other_value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        sign = self._sign
        return "-" * (not sign) + "".join(
            map(str, self._value if self._value[0] != 0 else self._value[1:])
        )

    def __int__(self):
        return int("".join(array_iterator(self._value)), 2)

    def __bool__(self):
        return self._value != "0"

    def __repr__(self):
        return f"Binary({1 - self._sign}b{''.join(map(str, self._value if self._value[0] != 0 else self._value[1:]))})"


def main():
    """
    CPU - O(n)
    RAM - O(n)
    :return: Void
    """
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        n = inp.readline()
        print(Binary(n), file=outp)


if __name__ == "__main__":
    main()
