import heapq
import math


class MaxHeapElement:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        return self.val == other.val


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return str(
            f"GraphEdge(start: {self.start}, end={self.end}, weight:{self.weight})"
        )


class NuTipoEtoGraph:
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
        for end in self.m.get(v, {}).keys():
            yield Edge(v, end, self.weight(v, end))

    @classmethod
    def parse_input(cls, inp):
        m = {}
        n, k = map(int, inp.readline().split())
        for i in range(k):
            ribble = inp.readline()
            v1, v2, w = map(int, ribble.split())
            m[v1] = m.get(v1, {})
            m[v2] = m.get(v2, {})
            m[v1][v2] = max(m[v1].get(v2, -math.inf), w)
            m[v2][v1] = max(m[v2].get(v1, -math.inf), w)
        r = range(1, n + 1)
        return cls(m, r)


def add_vertex(graph, added, not_added, edges, vertex):
    added.add(vertex)
    not_added.remove(vertex)
    for edge in graph.outgoing_edges(vertex):
        if edge.end in added:
            continue
        heapq.heappush(edges, MaxHeapElement(edge))


def solve(graph: NuTipoEtoGraph):
    result = []
    added = set()
    not_added = set(graph.vertices)
    edges = []
    vertex = graph.vertices[0]
    add_vertex(graph, added, not_added, edges, vertex)
    while edges:
        edge = heapq.heappop(edges).val
        if edge.end not in added:
            add_vertex(graph, added, not_added, edges, edge.end)
            result.append(edge)
    if not_added:
        raise ValueError("Incorrect graph.")
    return result


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        graph = NuTipoEtoGraph.parse_input(inp)
        try:
            mst = solve(graph)
            print(sum(map(lambda x: x.weight, mst)), file=out)
        except ValueError:
            print("Oops! I did it again", file=out)


if __name__ == "__main__":
    main()
