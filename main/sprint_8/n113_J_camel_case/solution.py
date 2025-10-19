from collections import defaultdict


def sa(s: str):
    res = []
    for ss in s:
        if ss.isupper():
            res.append(ss)
    return "".join(res)


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
        n = int(inp.readline())
        pt = PrefixTree()
        a = defaultdict(list)
        for i in range(n):
            s = inp.readline()
            pt.add_string(sa(s))
            a[sa(s)].append(s)
        m = int(inp.readline())
        rq = []
        for i in range(m):
            rq.append(sa(inp.readline()))
        for q in rq:
            cnode = pt.root_id
            r = True
            for s in q:
                cnode1 = pt.get_node_by_symbol(cnode, s)
                if cnode1 is None:
                    break
                cnode = cnode1
            if r:
                res = []
                for word in pt.all_words_from(cnode):
                    res.extend(a[q + word])
                for el in sorted(res):
                    out.write(el)
            else:
                out.write("\n")


if __name__ == "__main__":
    main()
