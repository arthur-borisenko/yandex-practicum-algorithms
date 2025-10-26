class ColorEnum:
    WHITE = 1
    GREY = 2
    BLACK = 3


class Vertex:
    def __init__(self, id, ribble_map):
        self.data = ribble_map
        self.id = id

    @property
    def connections(self):
        ribbles_for_node = self.data.get(self.id, {})
        for second in sorted(ribbles_for_node.keys(), reverse=True):
            yield Vertex(second, self.data), ribbles_for_node[second]

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
    s = 1
    return m, n, k, s


def dfs(start, ribble_map):
    colors = {}
    stack = []
    e, l = {}, {}
    t = 0
    stack.append(Vertex(start, ribble_map))
    colors[start] = ColorEnum.WHITE
    while stack:
        vertex = stack.pop()
        if colors.get(vertex.id, ColorEnum.WHITE) == ColorEnum.GREY:
            colors[vertex.id] = ColorEnum.BLACK
            l[vertex.id] = t
            t += 1
        if colors.get(vertex.id, ColorEnum.WHITE) == ColorEnum.WHITE:
            stack.append(vertex)
            colors[vertex.id] = ColorEnum.GREY
            for next_vertex, weight in vertex.connections:
                if colors.get(next_vertex.id, ColorEnum.WHITE) == ColorEnum.WHITE:
                    stack.append(next_vertex)
            e[vertex.id] = t
            t += 1
    return e, l


def main():
    m, n, k, s = parse_input(open("input.txt", "r"))
    out = open("output.txt", "w")
    entry, leave = dfs(1, m)
    for e, l in zip(
        map(lambda x: x[1], sorted(entry.items(), key=lambda x: x[0])),
        map(lambda x: x[1], sorted(leave.items(), key=lambda x: x[0])),
    ):
        print(e, l, file=out)
    out.close()


if __name__ == "__main__":
    main()
