import sys


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
    return m, n, k


def _top_sort(start, ribble_map, colors):
    stack = []
    d = []
    stack.append(Vertex(start, ribble_map))
    colors[start] = ColorEnum.WHITE
    while stack:
        vertex = stack.pop()
        if colors.get(vertex.id, ColorEnum.WHITE) == ColorEnum.GREY:
            yield vertex.id
            colors[vertex.id] = ColorEnum.BLACK
        if colors.get(vertex.id, ColorEnum.WHITE) == ColorEnum.WHITE:
            stack.append(vertex)
            colors[vertex.id] = ColorEnum.GREY
            for next_vertex, weight in vertex.connections:
                if colors.get(next_vertex.id, ColorEnum.WHITE) == ColorEnum.WHITE:
                    stack.append(next_vertex)


def top_sort(ribble_map, n):
    colors = {}
    for start in range(1, n + 1):
        if colors.get(start, ColorEnum.WHITE) == ColorEnum.WHITE:
            yield from _top_sort(start, ribble_map, colors)


def main():
    m, n, k = parse_input(open("input.txt", "r"))
    print(*reversed(list(top_sort(m, n))), file=open("output.txt", "w"))


if __name__ == "__main__":
    main()
