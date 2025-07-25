class DeletedElement:
    def __init__(self):
        pass


class HashMap:
    DELETED_ELEMENT_INSTANCE = DeletedElement()

    def _pf(self, b, i):
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
        while self._pf(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._pf(bucket_i, i)]
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
        while self._pf(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._pf(bucket_i, i)]
            if bucket[0] == key:
                bucket = (key, value)
                self._arr[self._pf(bucket_i, i)] = bucket
                return
            elif bucket[0] is None or isinstance(bucket[0], DeletedElement):
                bucket = (key, value)
                self._arr[self._pf(bucket_i, i)] = bucket
                return
            else:
                i += 1
        raise RuntimeError()

    def __delitem__(self, key):
        i = 0
        bucket_i = self.hash_fn(key) % self._m
        while self._pf(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._pf(bucket_i, i)]
            if bucket[0] == key:
                self._arr[self._pf(bucket_i, i)] = (self.DELETED_ELEMENT_INSTANCE, None)
                return
            elif bucket[0] is None:
                raise KeyError(key)
            else:
                i += 1
        raise KeyError(key)

    def keys(self):
        keys = []
        for bucket in self._arr:
            if bucket[0] is not None and not isinstance(bucket[0], DeletedElement):
                keys.append(bucket[0])
        return keys

    def values(self):
        values = []
        for bucket in self._arr:
            if bucket[0] is not None and not isinstance(bucket[0], DeletedElement):
                values.append(bucket[1])
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
