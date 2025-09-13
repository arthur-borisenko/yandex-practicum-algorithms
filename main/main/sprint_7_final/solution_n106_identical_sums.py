from collections import defaultdict

n=int(input())
l=list(map(int,input().split()))
s=sum(l)
a=defaultdict(int)
for el in l:
    a[el]+=1
if s%2==0:
    m=s//2
    dd=[{-1:0} for i in range(m)]
    dd[0][-1]=True
    for i in range(m):
        for el in l:
            if i-el>=0 and dd[i-el][-1]!=0 and a[el]>dd[i-el][el]:
                dd[i][-1]=1
                dd[i][el]=dd[i].get(el,0)+1
                break
    print(dd[-1])
else:
    print(False)