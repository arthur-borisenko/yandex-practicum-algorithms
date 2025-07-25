from typing import Any


class HashMap:
    DELETED = object()
    KEY_IDX = 0
    VAL_IDX = 1

    def __init__(self, m: int = 2 * 10**5, hash_fn=hash):
        self._arr: list[list] = [[None, None] for _ in range(m)]
        self.m = m
        self.hash_fn = hash_fn

    def _probe_func(self, b: int, i: int) -> int:
        return (b + i) % self.m

    def __getitem__(self, key) -> Any:
        i = 0
        bucket_i = self.hash_fn(key) % self.m
        while self._probe_func(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._probe_func(bucket_i, i)]
            if bucket[self.KEY_IDX] == key:
                return bucket[self.VAL_IDX]
            elif bucket[self.KEY_IDX] is None:
                raise KeyError(key)
            else:
                i += 1
        raise KeyError(key)

    def __setitem__(self, key, value) -> Any:
        i = 0
        bucket_i = self.hash_fn(key) % self.m
        while self._probe_func(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._probe_func(bucket_i, i)]
            if (
                bucket[self.KEY_IDX] == key
                or bucket[self.KEY_IDX] is None
                or bucket[self.KEY_IDX] is self.DELETED
            ):
                bucket = [key, value]
                self._arr[self._probe_func(bucket_i, i)] = bucket
                return
            else:
                i += 1
        raise RuntimeError()

    def __delitem__(self, key) -> None:
        i = 0
        bucket_i = self.hash_fn(key) % self.m
        while self._probe_func(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._probe_func(bucket_i, i)]
            if bucket[self.KEY_IDX] == key:
                self._arr[self._probe_func(bucket_i, i)] = [self.DELETED, None]
                return
            elif bucket[self.KEY_IDX] is None:
                raise KeyError(key)
            else:
                i += 1
        raise KeyError(key)

    def get(self, key, default=None) -> Any:
        i = 0
        bucket_i = self.hash_fn(key) % self.m
        while self._probe_func(bucket_i, i) != bucket_i - 1:
            bucket = self._arr[self._probe_func(bucket_i, i)]
            if bucket[self.KEY_IDX] == key:
                return bucket[self.VAL_IDX]
            elif bucket[self.KEY_IDX] is None:
                return default
            else:
                i += 1
        return default

    def pop(self, key) -> Any:
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
