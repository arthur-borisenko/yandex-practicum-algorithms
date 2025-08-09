from itertools import combinations_with_replacement

CHARACTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def polynominal_hash(s, base, mod):
    """CPU - O(n)
    RAM - O(1)

    we can use result % mod on all iterations, and it will equal result%mod on last iteration because:
    result = mod * a + r,
    so r = result % mod = result - mod * a.
    On next iteration we calculate result using:
    result = (base * mod * a + base * r + code) % mod
    and because first part has multiplier a, it will give zero modulo,
    so (base * mod * a + base * r + code) % mod = (base * mod * a - base*mod*a+base*r+code)%mod
    so, because we return result % mod, we can use (base * mod * a - base * mod * a + base * r + code) % mod,
    which equals (base * (result % mod) + code) % mod in all calculations
    """
    result = 0
    for char in s:
        code = ord(char)
        result = (base * result + code) % mod
    return result % mod


def break_collision():
    hash_to_string = {}
    # CPU - O(len(characters)^999)
    for length in range(1000):
        # CPU - O(len(characters)^length)
        for comb in combinations_with_replacement(CHARACTERS, length):
            string = "".join(comb)
            h = polynominal_hash(string, 1000, 123987123)
            if h in hash_to_string:
                return hash_to_string[h], string
            hash_to_string[h] = string
    return None, ""


def main():
    with open("output.txt", "w") as f:
        print(break_collision())


if __name__ == "__main__":
    main()
