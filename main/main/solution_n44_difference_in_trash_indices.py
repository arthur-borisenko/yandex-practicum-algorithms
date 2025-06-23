import array
from typing import Iterable

MAX_NUMBER=1000000

def binary_nearest_search(seq, target, key=lambda x: x):
    start = 0
    end = len(seq) - 1
    while start <= end:
        mid = (start + end) // 2
        if key(seq[mid]) <= target:
            start = mid + 1
        elif mid != 0 and key(seq[mid - 1]) > target:
            end = mid - 1
        else:
            return mid
    return -2


def main():
    """CPU - ???
    RAM - ???"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n=int(inp.readline())
        vals=sorted(map(int, inp.readline().split()))
        k=int(inp.readline())
        minimals=array.array("L", [MAX_NUMBER+1]*k)
        diffs=[]
        for idx, val in enumerate(vals):
            for idx2, val2 in enumerate(vals):
                if idx<=idx2:
                    continue
                diff=abs(val2-val)
                diffs.append([val,val2,diff,idx,idx2])
                if diff<minimals[k-1]:
                    i=binary_nearest_search(minimals, diff)
                    minimals.insert(i,diff)
                    minimals.pop()
        print(minimals[k-1], file=outp)

if __name__ == '__main__':
    main()


