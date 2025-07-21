from collections import defaultdict

inp = open("input.txt", "r")
d = defaultdict(dict)
q = []
n = int(inp.readline())
for i in range(n):
    dct = inp.readline().split()
    for el in dct:
        data = d[el]
        data[i] = data.get(i, 0) + 1

m = int(inp.readline())
for i in range(m):
    dct = inp.readline().split()
    q.append(set())
    for el in dct:
        q[-1].add(el)
out = open("output.txt", "w")
for qq in q:
    rels = {}
    for word in qq:
        for ddd in d[word].keys():
            rels[ddd] = rels.get(ddd, 0) + d[word][ddd]
    res = []
    for ddd in rels.keys():
        res.append((rels[ddd], ddd))
        res.sort(reverse=True, key=lambda x: (x[0], -x[1]))
        if len(res) > 5:
            res.pop()
    print(*map(lambda x: x[1] + 1, res), file=out)
