MAX_Y = 1000
X_BASE = MAX_Y * 10


class Gh:
    def __init__(self, mtx: list[list[bool]]):
        self.mtx: list[list[bool]] = mtx

    def outgoing_edges(self, v) -> list[int]:
        x, y = v // X_BASE, v % X_BASE
        res: list[int] = []
        if x - 1 >= 0 and self.mtx[y][x - 1]:
            x1 = x - 1
            res.append(X_BASE * x1 + y)
        if x + 1 < len(self.mtx[y]) and self.mtx[y][x + 1]:
            x2 = x + 1
            res.append(X_BASE * x2 + y)
        if y - 1 >= 0 and self.mtx[y - 1][x]:
            y1 = y - 1
            res.append(X_BASE * x + y1)
        if y + 1 < len(self.mtx) and self.mtx[y + 1][x]:
            y2 = y + 1
            res.append(X_BASE * x + y2)
        return res


def subgraph_size(start, graph: Gh):
    res = 0
    stack = [start]
    while stack:
        vertex = stack.pop()
        x, y = vertex // X_BASE, vertex % X_BASE
        if graph.mtx[y][x]:
            res += 1
            graph.mtx[y][x] = False
            for neighbor in graph.outgoing_edges(vertex):
                stack.append(neighbor)
    return res


def solution(inp):
    res = []
    n, m = map(int, inp.readline().split())
    for i in range(n):
        res.append(list(map(lambda x: x == "#", inp.readline().strip())))
    graph = Gh(res)
    l, s = 0, 0
    for y in range(n):
        for x in range(m):
            if graph.mtx[y][x]:
                start = X_BASE * x + y
                sgs = subgraph_size(start, graph)
                l += 1
                s = max(s, sgs)
    return l, s


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        print(*solution(inp), file=out)


if __name__ == "__main__":
    main()
