class HashMap:
    KEY_IDX = 0
    VAL_IDX = 1

    def __init__(self, m=10**5 + 3, hash_fn=hash):
        self._arr: list[list] = [[] for _ in range(m)]
        self.m = m
        self.hash_fn = hash_fn

    def __getitem__(self, key):
        bucket = self._arr[self.hash_fn(key) % self.m]
        for el in bucket:
            if el[self.KEY_IDX] == key:
                return el[self.VAL_IDX]
        raise KeyError(key)

    def __setitem__(self, key, value):
        bucket = self._arr[self.hash_fn(key) % self.m]
        for el in bucket:
            if el[self.KEY_IDX] == key:
                el[self.VAL_IDX] = value
                return
        bucket.append([key, value])

    def __delitem__(self, key):
        bucket = self._arr[self.hash_fn(key) % self.m]
        for i, el in enumerate(bucket):
            if el[self.KEY_IDX] == key:
                del bucket[i]
                return
        raise KeyError(key)

    def get(self, key, default=None):
        bucket = self._arr[self.hash_fn(key) % self.m]
        for el in bucket:
            if el[self.KEY_IDX] == key:
                return el[self.VAL_IDX]
        return default

    def pop(self, key):
        value = self[key]
        del self[key]
        return value


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        data = HashMap()
        for _ in range(n):
            query = inp.readline().split()
            match query[0]:
                case "get":
                    i = int(query[1])
                    print(data.get(i), file=out)
                case "put":
                    i = int(query[1])
                    value = int(query[2])
                    data[i] = value
                case "delete":
                    try:
                        i = int(query[1])
                        print(data.pop(i), file=out)
                    except KeyError:
                        print(None, file=out)


if __name__ == "__main__":
    main()
