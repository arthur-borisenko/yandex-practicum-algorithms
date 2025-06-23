import array
from typing import Iterable

MAX_VALUE=1000000

def main():
    """CPU - ???
    RAM - ???"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n=int(inp.readline())
        vals=list(map(int, inp.readline().split()))
        k=int(inp.readline())
        diffs_counts=array.array("Q", (MAX_VALUE + 1)*[0])
        for idx, val in enumerate(vals):
            for idx2, val2 in enumerate(vals):
                if idx<=idx2:
                    continue
                diff_cnt=abs(val2 - val)
                diffs_counts[diff_cnt]+=1
        cnt=0
        for diff, diff_cnt in enumerate(diffs_counts):
            if cnt+diff_cnt >= k:
                print(diff, file=outp)
                break
            cnt+=diff_cnt

if __name__ == '__main__':
    main()


