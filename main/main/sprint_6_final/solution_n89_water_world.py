import time


class ColorEnum:
    WHITE: int = 0
    GREY: int = 1
class Gh:
    def __init__(self, mtx: list[list[bool]]):
        self.mtx:list[list[bool]] = mtx
    def outgoing_edges(self, v) -> list[int]:
        result = v // 10000, v % 10000
        x, y = result
        res: list[int]=[]
        if x - 1 >= 0 and self.mtx[y][x - 1]:
            x1 = x - 1
            res.append(10000 * x1 + y)
        if x + 1 < len(self.mtx[y]) and self.mtx[y][x + 1]:
            x2 = x + 1
            res.append(10000 * x2 + y)
        if y - 1 >= 0 and self.mtx[y - 1][x]:
            y1 = y - 1
            res.append(10000 * x + y1)
        if y + 1 < len(self.mtx) and self.mtx[y + 1][x]:
            y2 = y + 1
            res.append(10000 * x + y2)
        return res


def subgraph_size(start, graph: Gh, visited: set):
    res=0
    stack=[]
    stack.append(start)
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            res += 1
            visited.add(vertex)
            for neighbor in graph.outgoing_edges(vertex):
                if neighbor not in visited:
                    stack.append(neighbor)
    return res

def aaa(inp):
    res = []
    n, m = map(int, inp.readline().split())
    for i in range(n):
        res.append(
            list(map(lambda x: x == "#", inp.readline().strip())))
    graph = Gh(res)
    l, s = 0, 0
    visited = set()
    for y in range(n):
        for x in range(m):
            if res[y][x]:
                start= 10000 * x + y
                if start not in visited:
                    sgs=subgraph_size(start, graph, visited)
                    l+=1
                    s=max(s, sgs)
    return l, s

print(*aaa(open("input.txt", "r")))

