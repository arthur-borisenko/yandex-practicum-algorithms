class DeletedElement:
    def __init__(self):
        pass


class HashMap:
    def _probing_func(self, b, i):
        return (b + i) % self._m

    def __init__(self, m=2 * 10**5, hash_fn=lambda x: abs(int(x))):
        self._arr: list = []
        self._m = m
        self.hash_fn = hash_fn
        for i in range(m):
            self._arr.append((None, None))

    def __getitem__(self, key):
        i = 0
        bucket_i = self.hash_fn(key) % self._m
        while self._probing_func(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._probing_func(bucket_i, i)]
            if bucket[0] == key:
                return bucket[1]
            elif bucket[0] is None:
                raise KeyError(key)
            else:
                i += 1
        raise KeyError(key)

    def __setitem__(self, key, value):
        i = 0
        bucket_i = self.hash_fn(key) % self._m
        while self._probing_func(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._probing_func(bucket_i, i)]
            if bucket[0] == key:
                bucket = (key, value)
                self._arr[self._probing_func(bucket_i, i)] = bucket
                return
            elif bucket[0] is None or isinstance(bucket[0], DeletedElement):
                bucket = (key, value)
                self._arr[self._probing_func(bucket_i, i)] = bucket
                return
            else:
                i += 1
        raise RuntimeError()

    def __delitem__(self, key):
        i = 0
        bucket_i = self.hash_fn(key) % self._m
        while self._probing_func(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._probing_func(bucket_i, i)]
            if bucket[0] == key:
                self._arr[self._probing_func(bucket_i, i)] = (DeletedElement(), None)
                return
            elif bucket[0] is None:
                raise KeyError(key)
            else:
                i += 1
        raise KeyError(key)

    def get(self, key, default=None):
        i = 0
        bucket_i = self.hash_fn(key) % self._m
        while self._probing_func(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._probing_func(bucket_i, i)]
            if bucket[0] == key:
                return bucket[1]
            elif bucket[0] is None:
                return default
            else:
                i += 1
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
