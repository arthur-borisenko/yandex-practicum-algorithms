from collections import defaultdict


d = []
q = []
n = int(input())
for i in range(n):
    dct = input().split()
    d.append(defaultdict(int))
    for el in dct:
        d[-1][el] += 1

m = int(input())
for i in range(m):
    dct = input().split()
    q.append(set())
    for el in dct:
        q[-1].add(el)


for qq in q:
    dcs = []
    for i, dc in enumerate(d):
        qqq = 0
        for word in qq:
            if word in dc:
                qqq += dc[word]
        if qqq > 0:
            dcs.append((qqq, i))
    print(*map(lambda x: x[1] + 1, sorted(dcs)))
