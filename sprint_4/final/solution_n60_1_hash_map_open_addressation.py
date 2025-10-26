from typing import Any


class HashMap:
    DELETED = object()
    KEY_IDX = 0
    VAL_IDX = 1

    def __init__(self, m: int = 2 * 10**5, hash_fn=hash):
        self.m = m
        self.hash_fn = hash_fn
        self._arr: list[list] = [[None, None] for _ in range(m)]

    def _probe_func(self, b: int, i: int) -> int:
        return (b + i) % self.m

    def __getitem__(self, key) -> Any:
        probe_step = 0
        i = self.hash_fn(key) % self.m
        while self._probe_func(i, probe_step) != i - 1:
            el = self._arr[self._probe_func(i, probe_step)]
            if el[self.KEY_IDX] == key:
                return el[self.VAL_IDX]
            elif el[self.KEY_IDX] is None:
                raise KeyError(key)
            else:
                probe_step += 1
        raise KeyError(key)

    def __setitem__(self, key, value) -> Any:
        probe_step = 0
        i = self.hash_fn(key) % self.m
        while self._probe_func(i, probe_step) != i - 1:
            el = self._arr[self._probe_func(i, probe_step)]
            if (
                el[self.KEY_IDX] == key
                or el[self.KEY_IDX] is None
                or el[self.KEY_IDX] is self.DELETED
            ):
                el = [key, value]
                self._arr[self._probe_func(i, probe_step)] = el
                return
            else:
                probe_step += 1
        raise RuntimeError()

    def __delitem__(self, key) -> None:
        probe_step = 0
        i = self.hash_fn(key) % self.m
        while self._probe_func(i, probe_step) != i - 1:
            bucket = self._arr[self._probe_func(i, probe_step)]
            if bucket[self.KEY_IDX] == key:
                self._arr[self._probe_func(i, probe_step)] = [self.DELETED, None]
                return
            elif bucket[self.KEY_IDX] is None:
                raise KeyError(key)
            else:
                probe_step += 1
        raise KeyError(key)

    def get(self, key, default=None) -> Any:
        probe_step = 0
        i = self.hash_fn(key) % self.m
        while self._probe_func(i, probe_step) != i - 1:
            el = self._arr[self._probe_func(i, probe_step)]
            if el[self.KEY_IDX] == key:
                return el[self.VAL_IDX]
            elif el[self.KEY_IDX] is None:
                return default
            else:
                probe_step += 1
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
