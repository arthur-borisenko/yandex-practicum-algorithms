class DoubleConnectedNode:
    def __init__(self, value, next_item=None, prev_item=None):
        self.value = value
        self.next_item = next_item
        self.prev_item = prev_item


class DoubleLinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self._len = 0

        if values is not None:
            for value in values:
                self.append(value)

    def _get_node(self, index):
        if index < 0 or index >= self._len:
            raise IndexError("Index out of range")
        node = self.head
        for _ in range(index):
            node = node.next_item
        return node

    def append(self, value):
        new_node = DoubleConnectedNode(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next_item = new_node
            new_node.prev_item = self.tail
            self.tail = new_node
        self._len += 1
        return new_node

    def create_node(self, after_node: DoubleConnectedNode, value):
        new_node = DoubleConnectedNode(value)
        new_node.next_item = after_node.next_item
        new_node.prev_item = after_node

        after_node.next_item = new_node

        if new_node.next_item:
            new_node.next_item.prev_item = new_node
        else:
            self.tail = new_node

        self._len += 1
        return new_node

    def delete_node(self, node: DoubleConnectedNode):
        if node is None:
            return

        if node.prev_item:
            node.prev_item.next_item = node.next_item
        else:  # node == head
            self.head = node.next_item

        if node.next_item:
            node.next_item.prev_item = node.prev_item
        else:  # node == tail
            self.tail = node.prev_item

        self._len -= 1

    def __delitem__(self, index):
        node = self._get_node(index)
        self.delete_node(node)

    def __getitem__(self, index):
        return self._get_node(index)

    def __len__(self):
        return self._len

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next_item

    def __str__(self):
        return " <-> ".join(str(x.value) for x in self)

    def __repr__(self):
        return f"DoubleLinkedList({list(map(lambda x: x.value, self))})"


class HashMap:
    def __init__(self, m=10**5 + 3, hash_fn=lambda x: int(x)):
        self._arr: list[DoubleLinkedList] = []
        self.m = m
        self.hash_fn = hash_fn
        for i in range(m):
            self._arr.append(DoubleLinkedList())

    def __getitem__(self, key):
        bucket = self._arr[self.hash_fn(key) % self.m]
        for node in bucket:
            if node.value[0] == key:
                return node.value[1]
        raise KeyError(key)

    def __setitem__(self, key, value, hash_fn=lambda x: int(x)):
        bucket = self._arr[self.hash_fn(key) % self.m]
        for node in bucket:
            if node.value[0] == key:
                node.value[1] = value
                return
        bucket.append([key, value])

    def __delitem__(self, key):
        bucket = self._arr[self.hash_fn(key) % self.m]
        for node in bucket:
            if node.value[0] == key:
                bucket.delete_node(node)
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
