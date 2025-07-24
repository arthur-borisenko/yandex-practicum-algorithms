class HashMap:
    def __init__(self, m=10**5 + 3, hash_fn=lambda x: int(x)):
        self._arr: list[list] = []
        self.m = m
        self.hash_fn = hash_fn
        for i in range(m):
            self._arr.append([])

    def __getitem__(self, key):
        bucket = self._arr[self.hash_fn(key) % self.m]
        for el in bucket:
            if el[0] == key:
                return el[1]
        raise KeyError(key)

    def __setitem__(self, key, value, hash_fn=lambda x: int(x)):
        bucket = self._arr[self.hash_fn(key) % self.m]
        for el in bucket:
            if el[0] == key:
                el[1] = value
                return
        bucket.append([key, value])

    def __delitem__(self, key):
        bucket = self._arr[self.hash_fn(key) % self.m]
        for i, el in enumerate(bucket):
            if el[0] == key:
                del bucket[i]
                return
        raise KeyError(key)

    def keys(self):
        keys = []
        for bucket in self._arr:
            for node in bucket:
                keys.append(node.value[0])
        return keys

    def values(self):
        values = []
        for bucket in self._arr:
            for node in bucket:
                values.append(node.value[1])
        return values

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
                    try:
                        i = query[1]
                        print(data[i], file=out)
                    except KeyError:
                        print(None, file=out)
                case "put":
                    i = query[1]
                    value = query[2]
                    data[i] = value
                case "delete":
                    try:
                        i = query[1]
                        print(data.pop(i), file=out)
                    except KeyError:
                        print(None, file=out)


if __name__ == "__main__":
    main()
