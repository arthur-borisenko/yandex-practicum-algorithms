def solution(s: str, t: str):
    if len(s) != len(t):
        return False
    s_to_t_mapping = {}
    t_to_s_mapping = {}
    for i, val in enumerate(s):
        val2 = t[i]
        if s_to_t_mapping.get(val, None) is None:
            s_to_t_mapping[val] = val2
        if t_to_s_mapping.get(val2, None) is None:
            t_to_s_mapping[val2] = val
        if s_to_t_mapping[val] != val2 or t_to_s_mapping[val2] != val:
            return False
    return True


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        s, t = inp.read().splitlines()[:2]
        print("YES" if solution(s, t) else "NO", file=out)


if __name__ == "__main__":
    main()
