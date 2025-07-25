class HashMap:
    KEY_IDX = 0
    VAL_IDX = 1
    BS = 20

    def __init__(self, m=10**4 + 3, hash_fn=hash):
        self._arr: list[list] = [[] for _ in range(m)]
        self.m = m
        self._len = 0
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
        self._len += 1
        if len(bucket) >= self.BS:
            self._rehash(int(self.m * 5))

    def _rehash(self, new_m: int):
        keys = self.keys()
        values = [self[key] for key in keys]
        self.__init__(new_m)
        for key, value in zip(keys, values):
            self[key] = value

    def __delitem__(self, key):
        bucket = self._arr[self.hash_fn(key) % self.m]
        for i, el in enumerate(bucket):
            if el[self.KEY_IDX] == key:
                del bucket[i]
                self._len -= 1
                return
        raise KeyError(key)

    def __len__(self):
        return self._len

    def get(self, key, default=None):
        bucket = self._arr[self.hash_fn(key) % self.m]
        for el in bucket:
            if el[self.KEY_IDX] == key:
                return el[self.VAL_IDX]
        return default

    def keys(self):
        keys = []
        for bucket in self._arr:
            for el in bucket:
                keys.append(el[self.KEY_IDX])
        return keys

    def values(self):
        values = []
        for bucket in self._arr:
            for el in bucket:
                values.append(el[self.VAL_IDX])
        return values

    def __contains__(self, key) -> bool:
        bucket = self._arr[self.hash_fn(key) % self.m]
        for el in bucket:
            if el[self.KEY_IDX] == key:
                return True
        return False

    def pop(self, key):
        value = self[key]
        del self[key]
        return value
