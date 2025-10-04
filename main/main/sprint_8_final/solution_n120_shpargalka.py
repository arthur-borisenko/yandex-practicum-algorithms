from collections import defaultdict
import sys


class PrefixTree:
    def __init__(self):
        self.terminals = set()
        self.ribbles = defaultdict(dict)
        self.root_id = 0
        self.ribbles[self.root_id] = {}
        self._free_id = self.root_id + 1

    def _add_node(self, parent, symbol):
        self.ribbles[parent] = self.ribbles.get(parent, {})
        self.ribbles[parent][symbol] = self._free_id
        self._free_id += 1
        return self.ribbles[parent][symbol]

    def get_node_by_symbol(self, parent, symbol):
        return (
            self.ribbles[parent][symbol]
            if parent in self.ribbles and symbol in self.ribbles[parent]
            else None
        )

    def is_root(self, node):
        return node == self.root_id

    def is_terminal(self, node):
        return node in self.terminals

    def add_string(self, string):
        current_node = self.root_id
        for i, symbol in enumerate(string):
            symbol = string[i]  # На каждом шаге работаем с одним символом.

            if self.get_node_by_symbol(current_node, symbol) is None:
                self._add_node(current_node, symbol)
            # Сдвинуться на следующий символ.
            current_node = self.get_node_by_symbol(current_node, symbol)
        self.terminals.add(current_node)
        return current_node

    def all_words_from(self, node):
        res = []
        f = []
        st = [(node, [])]
        while st:
            node, dt = st.pop()
            f.append(node)
            if node in self.terminals:
                res.append("".join(dt))
            for symbol, next_id in self.ribbles[node].items():
                st.append((next_id, dt + [symbol]))
        return res


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        a = inp.readline().strip()
        n = int(inp.readline())
        pt = PrefixTree()
        for iii in range(n):
            pt.add_string(inp.readline().strip())
        can_split = [False for i in range(len(a))]
        can_split.append(True)
        for i in range(len(a) - 1, -1, -1):
            ii = i
            current = pt.root_id
            while ii <= len(a):
                if can_split[ii] and (pt.is_terminal(current) or pt.is_root(current)):
                    can_split[i] = True
                    break
                if ii < len(a):
                    next_node = pt.get_node_by_symbol(current, a[ii])
                    if next_node is None:
                        break
                    else:
                        current = next_node
                ii = ii + 1

        print("YES" if can_split[0] else "NO")
