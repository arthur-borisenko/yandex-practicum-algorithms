from queue import Queue


class VertexAbstraction:
    def __init__(self, id, ribble_map):
        self.data = ribble_map
        self.id = id

    @property
    def connections(self):
        r = []
        ribbles_for_node = self.data.get(self.id, {})
        for second in sorted(ribbles_for_node.keys()):
            r.append(VertexAbstraction(second, self.data))
        return r

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
    return m, n, k, s


def bfs(start, ribble_map, colors):
    queue = Queue()
    queue.put(VertexAbstraction(start, ribble_map))
    colors[start] = "white"
    while not queue.empty():
        vertex = queue.get()
        if colors.get(vertex.id, "white") == "white":
            colors[vertex.id] = "grey"
            yield vertex.id
            for next_vertex in vertex.connections:
                if colors.get(next_vertex.id, "white") == "white":
                    queue.put(next_vertex)


def main():
    m, n, k, s = parse_input(open("input.txt", "r"))
    print(*bfs(s, m, {}))


if __name__ == "__main__":
    main()
