def main():
    m={}
    inp=open("input.txt","r")
    out=open("output.txt","w")
    n, k = map(int, inp.readline().split())
    for ribble in inp.readlines():
        v1, v2 = map(int,ribble.split())
        m[v1]=m.get(v1,{})
        m[v1][v2]=1
    for i in range(n):
        v=m.get(i + 1, {})
        print(len(v), *sorted(v.keys()), file=out)
    inp.close()
    out.close()
if __name__ == "__main__":
    main()