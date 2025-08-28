import sys
from io import StringIO

inp=StringIO("""6
1
2
6
1
42
52
""")
inp=sys.stdin
n=int(inp.readline())
l=[]
for i in range(n):
    l.append((int(inp.readline()), i))
import heapq
T=500
l2=[[]]
h1=[]=[]
for el, i in l:
    heapq.heappush(h1, (el, i))
    l2.append(l2[-1].copy())
    if el>T:
        heapq.heappush(l2[-1], (el, i))
l3=sorted(l, reverse=True)
used=set()
a=[]
b=[]
c=[]
for el, i in l3:
    vg=l2[i]
    if len(vg)==0 or el in used:
        a.append((el, i))
    else:
        vg1=heapq.heappop(vg)
        g=True
        while vg1 in used:
            if len(vg)==0:
                g=False
                break
            vg1=heapq.heappop(vg)
        if g:
            b.append((el, i, vg1))
            c.append(i+1)
            used.add(vg1)
            used.add((el, i))
        else:
            a.append((el, i))
print(sum(map(lambda x: x[0], a)), len(c))
print(*sorted(c))