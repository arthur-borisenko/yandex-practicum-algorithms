class HashMap:
    DELETED = object()

    def __init__(self, m=2 * 10**5, hash_fn=hash):
        self._arr: list[list] = [[None, None] for _ in range(m)]
        self._m = m
        self.hash_fn = hash_fn

    def _probing_fumc(self, b, i):
        return (b + i) % self._m

    def __getitem__(self, key):
        i = 0
        bucket_i = self.hash_fn(key) % self._m
        while self._probing_fumc(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._probing_fumc(bucket_i, i)]
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
        while self._probing_fumc(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._probing_fumc(bucket_i, i)]
            if bucket[0] == key or bucket[0] is None or bucket[0] is self.DELETED:
                bucket = [key, value]
                self._arr[self._probing_fumc(bucket_i, i)] = bucket
                return
            else:
                i += 1
        raise RuntimeError()

    def __delitem__(self, key):
        i = 0
        bucket_i = self.hash_fn(key) % self._m
        while self._probing_fumc(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._probing_fumc(bucket_i, i)]
            if bucket[0] == key:
                self._arr[self._probing_fumc(bucket_i, i)] = [self.DELETED, None]
                return
            elif bucket[0] is None:
                raise KeyError(key)
            else:
                i += 1
        raise KeyError(key)

    def get(self, key, default=None):
        i = 0
        bucket_i = self.hash_fn(key) % self._m
        while self._probing_fumc(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._probing_fumc(bucket_i, i)]
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
