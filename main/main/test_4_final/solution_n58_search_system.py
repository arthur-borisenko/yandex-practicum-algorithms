from collections import defaultdict


def create_documents_index(inp):
    index = defaultdict(dict)
    n = int(inp.readline())
    for i in range(n):
        document = inp.readline().split()
        for el in document:
            data = index[el]
            data[i] = data.get(i, 0) + 1
    return index


def parse_queries(inp):
    queries = []
    m = int(inp.readline())
    for i in range(m):
        query = inp.readline().split()
        queries.append(set())
        for el in query:
            queries[-1].add(el)
    return queries


def search(index, query):
    rels = {}
    for word in query:
        for document in index[word].keys():
            rels[document] = rels.get(document, 0) + index[word][document]
    res = []
    for document in rels.keys():
        res.append((rels[document], document))
    res.sort(reverse=True, key=lambda x: (x[0], -x[1]))
    return res


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        index = create_documents_index(inp)
        queries = parse_queries(inp)
        for query in queries:
            res = search(index, query)
            print(*map(lambda x: x[1] + 1, res[:5]), file=out)


if __name__ == "__main__":
    main()
