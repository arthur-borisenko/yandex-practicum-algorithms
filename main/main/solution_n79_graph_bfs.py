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
    s = int(inp.readline())
    inp.close()
    return m, n, k, s


def dfs(start, ribble_map):
    stack = []
    colors = {}
    d = []
    stack.append(VertexAbstraction(start, ribble_map))
    colors[start] = "white"
    while stack:
        vertex = stack.pop()
        if colors.get(vertex.id, "white") == "white":
            yield vertex.id
            d.append(vertex.id)
        colors[vertex.id] = "grey"
        for next_vertex, weight in vertex.connections:
            if colors.get(next_vertex.id, "white") == "white":
                stack.append(next_vertex)
        colors[vertex.id] = "black"


def main():
    out = open("output.txt", "w")
    m, n, k, s = parse_input(open("input.txt", "r"))
    print(*dfs(s, m), file=out)


if __name__ == "__main__":
    main()
