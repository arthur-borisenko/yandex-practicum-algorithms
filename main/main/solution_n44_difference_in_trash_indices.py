import numba

MAX_VALUE=1000000

def main():
    """CPU - ???
    RAM - ???"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n=int(inp.readline())
        vals=list(map(int, inp.readline().split()))
        k=int(inp.readline())
        diffs_counts = count_diffs(vals)
        cnt=0
        for diff, diff_cnt in enumerate(diffs_counts):
            if cnt+diff_cnt >= k:
                print(diff, file=outp)
                break
            cnt+=diff_cnt

@numba.njit
def count_diffs(vals):
    diffs_counts = (MAX_VALUE + 1) * [0]
    for idx, val in enumerate(vals):
        for val2 in vals[idx + 1:]:
            diff_cnt = abs(val2 - val)
            diffs_counts[diff_cnt] += 1
    return diffs_counts


if __name__ == '__main__':
    main()


