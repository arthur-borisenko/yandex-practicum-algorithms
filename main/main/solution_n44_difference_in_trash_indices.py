MAX_VALUE=1000000

def main():
    """CPU - O(n log(k) + n log(n))
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n=int(inp.readline())
        vals=sorted(map(int, inp.readline().split()))
        k=int(inp.readline())
        print(search(vals,k), file=outp)

def search(v,k):
    pass
    #TODO: solve
if __name__ == '__main__':
    main()


