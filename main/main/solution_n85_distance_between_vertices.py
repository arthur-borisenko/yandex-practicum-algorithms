import math
from queue import Queue

class ColorEnum:
    WHITE = 0
    GREY = 1
class Graph:
    @classmethod
    def parse_input(cls, inp):
        m = {}
        n, k = map(int, inp.readline().split())
        for i in range(k):
            ribble = inp.readline()
            v1, v2 = map(int, ribble.split())
            m[v1] = m.get(v1, {})
            m[v2] = m.get(v2, {})
            w = 1
            m[v1][v2] = min(m[v1].get(v2, math.inf), w)
            m[v2][v1] = min(m[v2].get(v1, math.inf), w)
        r = range(1, n + 1)
        return cls(m, r)

    def __init__(self, m, r):
        self.vertices = list(r)
        self.m = m

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices)

    def weight(self, a, b):
        return self.m.get(a, {}).get(b, -1)

    def outgoing_edges(self, v):
        return self.m.get(v, {}).keys()


def get_distance(start, target, graph: Graph, colors):
    queue = Queue()
    queue.put((start, 0))
    colors[start] = ColorEnum.WHITE
    while not queue.empty():
        vertex, dist = queue.get()
        if colors.get(vertex, ColorEnum.WHITE) == ColorEnum.WHITE:
            colors[vertex] = ColorEnum.GREY
            if vertex == target:
                return dist
            for next_vertex in graph.outgoing_edges(vertex):
                if colors.get(next_vertex, ColorEnum.WHITE) == ColorEnum.WHITE:
                    queue.put((next_vertex, dist + 1))
    return -1


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        graph = Graph.parse_input(inp)
        start, end = map(int, inp.readline().split())
        print(get_distance(start, end, graph, {}), file=out)


if __name__ == "__main__":
    main()
