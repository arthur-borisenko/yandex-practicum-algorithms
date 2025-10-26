import math


class Graph:
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


def parse_input(inp):
    m = {}
    n, k = map(int, inp.readline().split())
    for i in range(k):
        ribble = inp.readline()
        v1, v2, w = map(int, ribble.split())
        m[v1] = m.get(v1, {})
        m[v2] = m.get(v2, {})
        m[v1][v2] = min(m[v1].get(v2, math.inf), w)
        m[v2][v1] = min(m[v2].get(v1, math.inf), w)
    r = range(1, n + 1)
    inp.close()
    return Graph(m, r)


def get_min_dist_not_visited_vertex(graph: Graph, dist, visited):
    current_minimum = math.inf
    current_minimum_vertex = None

    for v in graph.vertices:
        if not visited[v] and dist[v] < current_minimum:
            current_minimum = dist[v]
            current_minimum_vertex = v

    return current_minimum_vertex


def dijkstra(graph: Graph, s):
    dist = {}
    prev = {}
    vst = {}
    for v in graph.vertices:
        dist[v] = math.inf
        prev[v] = -1
        vst[v] = False

    dist[s] = 0

    while True:
        u = get_min_dist_not_visited_vertex(graph, dist, vst)
        if u is None or dist[u] == math.inf:
            break

        vst[u] = True
        neighbours = graph.outgoing_edges(u)

        for v in neighbours:
            if dist[v] > dist[u] + graph.weight(u, v):
                dist[v] = dist[u] + graph.weight(u, v)
                prev[v] = u
    return dist


def main():
    g = parse_input(open("input.txt", "r"))
    outp = open("output.txt", "w")
    dist = {}
    for v in g.vertices:
        dst = dijkstra(g, v)
        dist[v] = dst
    for v in range(1, len(g) + 1):
        for u in range(1, len(g) + 1):
            d = dist.get(v, {}).get(u, -1)
            print(d if d != math.inf else -1, end=" ", file=outp)
        print(file=outp)
    outp.close()


if __name__ == "__main__":
    main()
