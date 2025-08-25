inp1=[]
n, m = map(int, input().split())
for i in range(n):
    inp1.append(list(map(int, input())))
d=[[0 for i in range(m)] for j in range(n)]

for ii in range(-n+1, 0):
    i=-ii
    for j in range(m):
        d[i][j]=0
        if i > 0:
            d[i][j]=max(d[i][j], d[i-1][j])
        if j > 0:
            d[i][j]=max(d[i][j], d[i][j-1])
        d[i][j]+=inp1[i][j]
print(d[-1][-1])