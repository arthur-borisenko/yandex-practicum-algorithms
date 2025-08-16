from collections import defaultdict


class VertexAbstraction:
    def __init__(self, id, ribble_map):
        self.data = ribble_map
        self.id = id

    @property
    def connections(self):
        ribbles_for_node = self.data.get(self.id, {})
        for second in sorted(ribbles_for_node.keys(), reverse=True):
            yield VertexAbstraction(second, self.data), ribbles_for_node[second]

    def hasChild(self, child):
        return child in self.connections


def parse_input(inp):
    m = {}
    n, k = map(int, inp.readline().split())
    for i in range(k):
        ribble = inp.readline()
        v1, v2 = map(int, ribble.split())
        m[v1] = m.get(v1, {})
        m[v2] = m.get(v2, {})
        m[v1][v2] = 1
        m[v2][v1] = 1
    return m, n, k


def ks(start, ribble_map, colors, ksids):
    iteration_id = max(ksids.values()) + 1 if len(ksids) > 0 else 0
    stack = []
    visited = set()
    d = []
    stack.append(VertexAbstraction(start, ribble_map))
    colors[start] = "white"
    while stack:
        vertex = stack.pop()
        if colors.get(vertex.id, "white") == "grey":
            visited.add(vertex.id)
            iteration_id = ksids.get(vertex.id, iteration_id)
            colors[vertex.id] = "black"
        if colors.get(vertex.id, "white") == "white":
            stack.append(vertex)
            colors[vertex.id] = "grey"
            for next_vertex, weight in vertex.connections:
                if colors.get(next_vertex.id, "white") == "white":
                    stack.append(next_vertex)
    for node in visited:
        ksids[node] = iteration_id


def kss(ribble_map, n):
    colors = {}
    ksids = {}
    for start in range(1, n + 1):
        if colors.get(start, "white") == "white":
            ks(start, ribble_map, colors, ksids)
    ksids2 = defaultdict(list)
    for vx in ksids.keys():
        ksids2[ksids[vx]].append(vx)
    return ksids2.values()


def main():
    m, n, k = parse_input(open("input.txt", "r"))
    data = kss(m, n)
    print(len(data), *map(lambda x: " ".join(map(str, sorted(x))), data), sep="\n")


if __name__ == "__main__":
    main()
