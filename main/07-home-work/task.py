class Binary:
    """Base binary number.
    Currently supported:
    create - O(log(n))
    str - O(1)
    int-O(1)
    bool - O(1)
    equal - O(1)
    add - O(n)"""

    def _halfsumm(self, a, b):
        if a and b:
            return True, False
        if ((not a) and b) or ((not b) and a):
            return False, True
        else:
            return False, False

    def _summ(self, a, b, cin):
        ab2nd, ab1st = self._halfsumm(a, b)
        abc2nd, abc1st = self._halfsumm(ab1st, cin)
        return abc2nd or ab2nd, abc1st

    def parseint(self, value):
        """convert base 10 integer to binary string"""
        sign = True
        if value < 0:
            sign = False
            value = -value
        current_power = 0
        res = ""
        while 2**current_power <= value:
            if value % 2 ** (current_power + 1) != 0:
                value -= 2**current_power
                res += "1"
            else:
                res += "0"
            current_power += 1
        if not sign:
            res += "-"
        if not res:
            res = "0"
        return "".join(list(reversed(res)))

    def __add__(self, other):
        if isinstance(other, str):
            other = Binary(other)
        elif isinstance(other, Binary):
            pass
        else:
            raise TypeError("other must be Binary or str")
        long = max([self._value, other._value], key=lambda x: len(x))
        short = min([self._value, other._value], key=lambda x: len(x))
        _next = False
        res = ""
        for i, el_1 in enumerate(reversed(long)):
            el_2 = "0"
            if i < len(short):
                el_2 = short[-i - 1]
            summ = self._summ(el_1 == 1, el_2 == 1, _next)
            _next, val = summ
            res += "1" if val else "0"
        return res

    def __radd__(self, other):
        return self.__add__(other)

    def __init__(self, value):
        self._value = "0"
        if isinstance(value, Binary):
            self._value = value._value
        if isinstance(value, str):
            self._value = self.parseint(int(value))
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
        return self._value

    def __int__(self):
        return int(self._value, 2)

    def __bool__(self):
        return self._value != "0"

    def __repr__(self):
        return f"Binary(0b{self._value})"


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
