from array import array


class RingBuffer:
    def __init__(self, type, size):
        self._data = array("q", (0,) * size)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, i):
        return self._data[self._get_real_i(i)]

    def __setitem__(self, i, value):
        self._data[self._get_real_i(i)] = value

    def _get_real_i(self, i):
        while i < 0:
            i += len(self)
        if i < len(self):
            real_i = i
        else:
            real_i = i % len(self)
        return real_i


class Deq:
    def __init__(self, size):
        self._len = 0
        self._tail = 0
        self.size = size
        self._data = RingBuffer("q", size)

    def push_front(self, item):
        if self._len == self.size:
            raise OverflowError("Queue overflow")
        self._data[self._len + self._tail] = item
        self._len += 1

    def pop_front(self):
        if self._len == 0:
            raise IndexError("Queue underflow")
        res = self.peek_front()
        self._len -= 1
        return res

    def peek_front(self):
        if len(self) == 0:
            raise IndexError("Attempted to get element of empty queue")
        return self._data[self._tail + self._len - 1]

    def peek_back(self):
        if len(self) == 0:
            raise IndexError("Attempted to get element of empty queue")
        return self._data[self._tail]

    def pop_back(self):
        if len(self) == 0:
            raise IndexError("Queue underflow")
        res = self.peek_back()
        self._tail += 1
        self._len -= 1
        return res

    def __bool__(self):
        return len(self) > 0

    def push_back(self, item):
        if self._len == self.size:
            raise OverflowError("Queue overflow")
        self._data[self._tail - 1] = item
        self._len += 1
        self._tail -= 1

    def __len__(self):
        return self._len


def parse_input_cmd(line, queue):
    cmd, args = line.split()[0], line.split()[1:]
    match cmd:
        case "pop_back":
            return queue.pop_back()
        case "pop_front":
            return queue.pop_front()
        case "push_back":
            queue.push_back(int(args[0]))
        case "push_front":
            queue.push_front(int(args[0]))
        case _:
            raise ValueError(f"Invalid command: {cmd}")


def main():
    """
    CPU - O(n)
    RAM - O(n)
    """
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        queue = Deq(int(inp.readline()))
        for i in range(n):
            cmd = inp.readline().strip()
            try:
                res = parse_input_cmd(cmd, queue)
            except Exception:
                print("error", file=outp)
            else:
                if res is not None:
                    print(res, file=outp)


if __name__ == "__main__":
    main()
