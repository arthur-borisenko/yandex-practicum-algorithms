def solution(s: str, t: str) -> bool:
    """CPU - O(n)
    RAM - O(n)"""
    if len(s) != len(t):
        return False
    s_to_t = {}
    t_to_s = {}
    for i, s_i_char in enumerate(s):
        t_i_char = t[i]
        if s_to_t.get(s_i_char) is None:
            s_to_t[s_i_char] = t_i_char
        if t_to_s.get(t_i_char) is None:
            t_to_s[t_i_char] = s_i_char
        if s_to_t[s_i_char] != t_i_char or t_to_s[t_i_char] != s_i_char:
            return False
    return True


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        s, t = inp.read().splitlines()[:2]
        print("YES" if solution(s, t) else "NO", file=out)


if __name__ == "__main__":
    main()
