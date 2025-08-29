import sys
from collections import defaultdict
from io import StringIO

m=defaultdict(dict)
def a(ds, i, cu):
    if cu in m[i]:
        return m[i][cu]
    if len(ds) - i <= 0:
        m[i][cu] = (0, cu, [])
        return 0, cu, []
    if len(ds) - i <= cu:
        v  = 0, cu - (len(ds) - i), list(range(i + 1, len(ds) + 1))
        m[i][cu] = v
        return v
    cp = ds[i]
    if cp > 500:
        sm1, cu1, spt1 = a(ds, i + 1, cu + 1)
    else:
        sm1, cu1, spt1 = a(ds, i + 1, cu)
    sm1 += cp
    dt = a(ds, i + 1,
                       cu - 1) if cu > 0 else (None, None, None)
    sm2, cu2, spt2 = dt[0], dt[1], dt[2]
    if not isinstance(sm2, int):
        pass #print(sm2)
    if sm2 is not None and sm2 < sm1:
        sm3, cu3, spt3 = sm2, cu2, spt2 + [i + 1]
    else:
        sm3, cu3, spt3 = sm1, cu1, spt1
    m[i][cu] = (sm3, cu3, spt3)
    return sm3, cu3, spt3
inp=sys.stdin
inp=StringIO("""10
169
258
406
642
844
562
889
743
144
682
""")
n=int(inp.readline())
l=[]
for i in range(n):
    l.append(int(inp.readline()))
#inp = [696, 744, 517, 510, 566, 772, 988, 691, 800, 802]
d=[[(None, None, None) for _ in range(n)] for _ in range(n)]
for i in range(n-1, 1, -1):
    for j in range(len(d[i]) - 1):
        if i + 1 == len(d):
            d[i][j] = (0, j-1, [i]) if j > 0 else (l[i], j, [])
        else:
            if l[i]>500 and j<len(d[i+1])-1:
                sm1, cu1, spt1=d[i+1][j+1]
            else:
                sm1, cu1, spt1=d[i+1][j]
            sm1+=l[i]
            sm2, cu2, spt2=d[i+1][j-1]
            if sm2 is not None and sm2 < sm1:
                sm3, cu3, spt3 = sm2, cu2, spt2 + [i + 1]
            else:
                sm3, cu3, spt3 = sm1, cu1, spt1
            d[i][j] = (sm3, cu3, spt3)
dt = a(l, 0, 0)
print(dt[0], len(dt[2]))
print(*sorted(dt[2]), sep="\n")