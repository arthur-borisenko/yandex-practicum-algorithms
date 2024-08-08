from array import array


class RingArray:
    def __init__(self, type, size):
        self._data = array("q", (0,) * size)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, i):
        return self._data[self._get_real_i(i)]

    def __setitem__(self, i, value):
        self._data[self._get_real_i(i)] = value

    def _get_real_i(self, i):
        if i < 0:
            i += 1
        while i < 0:
            i += len(self)
        if i < len(self):
            real_i = i
        else:
            real_i = i % len(self)
        return real_i


class Queue:
    def __init__(self, size):
        self._len = 0
        self._tail = 0
        self.size = size
        self._data = RingArray("q", size)

    def push(self, item):
        if self._len == self.size:
            raise OverflowError("Queue overflow")
        self._data[self._len + self._tail] = item
        self._len += 1

    def pop(self):
        if self._len == 0:
            raise IndexError("Queue underflow")
        res = self.peek()
        self._tail += 1
        self._len -= 1
        return res

    def peek(self):
        if len(self) == 0:
            raise IndexError("Attempted to get element of empty queue")
        return self._data[self._tail]

    def __bool__(self):
        return len(self) > 0

    def __len__(self):
        return self._len


def parse_input_cmd(line, queue):
    cmd, args = line.split()[0], line.split()[1:]
    match cmd:
        case "push":
            queue.push(int(args[0]))
        case "size":
            return len(queue)
        case "pop":
            return queue.pop()
        case "peek":
            return queue.peek()
        case _:
            raise ValueError(f"Invalid command: {cmd}")


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        queue = Queue(int(inp.readline()))
        for i in range(n):
            cmd = inp.readline().strip()
            try:
                res = parse_input_cmd(cmd, queue)
            except OverflowError:
                print("error", file=outp)
            except IndexError:
                print(None, file=outp)
            else:
                if res is not None:
                    print(res, file=outp)
        pass  # 66 -41 96 0 42 44 -43 -37


if __name__ == "__main__":
    main()
