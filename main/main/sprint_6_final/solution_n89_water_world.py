from queue import Queue


class ColorEnum:
    WHITE = 0
    GREY = 1


class Gh:
    def __init__(self, mtx, vertices):
        self.vertices = vertices
        self.mtx = mtx

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices)

    def outgoing_edges(self, v):
        x, y = xyid(v)
        res = []
        if x - 1 >= 0 and self.mtx[y][x - 1]:
            res.append(vid(x - 1, y))
        if x + 1 < len(self.mtx[y]) and self.mtx[y][x + 1]:
            res.append(vid(x + 1, y))
        if y - 1 >= 0 and self.mtx[y - 1][x]:
            res.append(vid(x, y - 1))
        if y + 1 < len(self.mtx) and self.mtx[y + 1][x]:
            res.append(vid(x, y + 1))
        return res


def vid(x, y):
    return 10000 * x + y


def xyid(v):
    return v // 10000, v % 10000


def subgraph_size(start, graph: Gh, visited: set):
    queue = Queue()
    queue.put(start)
    res = 0
    while not queue.empty():
        vertex = queue.get()
        if vertex not in visited:
            visited.add(vertex)
            res += 1
            for next_vertex in graph.outgoing_edges(vertex):
                if next_vertex not in visited:
                    queue.put(next_vertex)
    return res


def aaa(inp):
    res = []
    n, m = map(int, inp.readline().split())
    for i in range(n):
        res.append(list(map(lambda x: x == "#", inp.readline().strip())))
    r = []

    for y in range(n):
        for x in range(m):
            if res[y][x]:
                r.append(vid(x, y))
    graph = Gh(res, r)
    l, s = 0, 0
    visited = set()
    for start in graph.vertices:
        if start in visited:
            continue
        sgs = subgraph_size(start, graph, visited)
        l += 1
        s = max(s, sgs)
    return l, s


def main():
    print(*aaa(open("input.txt", "r")))


if __name__ == "__main__":
    main()
