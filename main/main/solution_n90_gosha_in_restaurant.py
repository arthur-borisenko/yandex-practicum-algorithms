import sys
from collections import defaultdict

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
n=int(inp.readline())
l=[]
for i in range(n):
    l.append(int(inp.readline()))
#inp = [696, 744, 517, 510, 566, 772, 988, 691, 800, 802]
dt = a(l, 0, 0)
print(dt[0], len(dt[2]))
print(*sorted(dt[2]), sep="\n")