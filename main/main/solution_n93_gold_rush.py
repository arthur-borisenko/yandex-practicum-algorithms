def pi(inp):
    m=int(inp.readline())
    n=int(inp.readline())
    r=[]
    for i in range(n):
        r.append(list(map(int, inp.readline().split())))
    return m,n,r
def main():
    with open("input.txt","r") as inp, open("output.txt","w") as out:
        m,n,r=pi(inp)
        rr=sorted(r, reverse=True)
        rrr=0
        for ci, mi in rr:
            if m<=0:
                break
            rrr+=ci*min(m, mi)
            m-=min(m, mi)
        print(rrr, file=out)
if __name__ == '__main__':
    main()