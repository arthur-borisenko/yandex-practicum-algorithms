import math
import sys
from collections import defaultdict
from io import StringIO
from queue import Queue


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
        return cls(m, m.keys())

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


def bfs(start, graph: Graph, colors):
    queue = Queue()
    queue.put(start)
    colors[start] = "white"
    while not queue.empty():
        vertex = queue.get()
        if colors.get(vertex, "white") == "white":
            yield vertex
            colors[vertex] = "grey"
            for next_vertex in graph.outgoing_edges(vertex):
                if colors.get(next_vertex, "white") == "white":
                    queue.put(next_vertex)


def solution(graph: Graph):
    colors = defaultdict(lambda: "white")
    search_colors = {}
    for start in graph.vertices:
        if start in search_colors:
            continue
        colors[start] = "red"
        for vertex in bfs(start, graph, search_colors):
            for neighbor in graph.outgoing_edges(vertex):
                if colors[vertex] == "white":
                    if colors[neighbor] == "red":
                        colors[vertex] = "blue"
                    elif colors[neighbor] == "blue":
                        colors[vertex] = "red"
                if colors[vertex] == "red":
                    if colors[neighbor] == "red":
                        return False
                    colors[neighbor] = "blue"
                if colors[vertex] == "blue":
                    if colors[neighbor] == "blue":
                        return False
                    colors[neighbor] = "red"
    return True


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        g = Graph.parse_input(inp)
        print("YES" if solution(g) else "NO", file=out)


if __name__ == "__main__":
    main()
