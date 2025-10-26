from queue import Queue


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
        r = []
        ribbles_for_node = self.data.get(self.id, {})
        for second in sorted(ribbles_for_node.keys()):
            r.append(Vertex(second, self.data))
        return r

    def hasChild(self, child):
        return child in self.connections


def bfs(start, ribble_map, colors):
    queue = Queue()
    queue.put(Vertex(start, ribble_map))
    colors[start] = ColorEnum.WHITE
    while not queue.empty():
        vertex = queue.get()
        if colors.get(vertex.id, ColorEnum.WHITE) == ColorEnum.WHITE:
            colors[vertex.id] = ColorEnum.GREY
            yield vertex.id
            for next_vertex in vertex.connections:
                if colors.get(next_vertex.id, ColorEnum.WHITE) == ColorEnum.WHITE:
                    queue.put(next_vertex)
            colors[vertex.id] = ColorEnum.BLACK
