from collections import defaultdict

MOD = 10**9 + 7


class Graph:
    def __init__(self, rb):
        self.vertices = set()
        self.m = {}
        self.p = {}
        for p, t in rb:
            self.vertices.add(p)
            self.vertices.add(t)
            self.m[p] = self.m.get(p, [])
            self.m[p].append(t)
            self.p[t] = self.p.get(t, [])
            self.p[t].append(p)

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices)

    def parents(self, v):
        return self.p[v] if v in self.p else set()

    def outgoing_edges(self, v):
        return self.m.get(v, [])


def parse_input(inp):
    m = {}
    n, k = map(int, inp.readline().split())
    for i in range(k):
        ribble = inp.readline()
        v1, v2 = map(int, ribble.split())
        m[v1] = m.get(v1, {})
        m[v2] = m.get(v2, {})
        m[v1][v2] = 1
    return m, n, k


def _top_sort(start, graph, colors):
    stack = []
    stack.append(start)
    colors[start] = "white"
    while stack:
        vertex = stack.pop()
        if colors.get(vertex, "white") == "grey":
            yield vertex
            colors[vertex] = "black"
        if colors.get(vertex, "white") == "white":
            stack.append(vertex)
            colors[vertex] = "grey"
            for next_vertex in graph.outgoing_edges(vertex):
                if colors.get(next_vertex, "white") == "white":
                    stack.append(next_vertex)


def top_sort(start, graph):
    return list(reversed(list(_top_sort(start, graph, {}))))


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n, m = map(int, inp.readline().split())
        rb = []
        for _ in range(m):
            p, t = map(int, inp.readline().split())
            rb.append((p, t))
        a, b = map(int, inp.readline().split())
        graph = Graph(rb)
        counts = defaultdict(lambda: 0)
        counts[a] = 1
        for v in top_sort(a, graph):
            for p in graph.parents(v):
                counts[v] += counts[p]
            counts[v] %= MOD
        print(counts[b], file=out)


# print(*reversed(order))
if __name__ == "__main__":
    main()
