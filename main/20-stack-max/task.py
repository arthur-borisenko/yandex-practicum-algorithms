from array import array


class Stack:
    """Basic stack - supports push, pop, peek, iterate from top."""

    def __init__(self, size):
        self._len = 0
        self.size = size
        self._data = array("q", (0,) * size)

    def push(self, item):
        if self._len == self.size:
            raise OverflowError("Stack overflow")
        self._data[self._len] = item
        self._len += 1

    def pop(self):
        if self._len == 0:
            raise IndexError("Stack underflow")
        res = self.peek()
        self._len -= 1
        return res

    def peek(self):
        if self._len == 0:
            raise IndexError("Attempted to get element of empty stack")
        return self._data[self._len - 1]

    def __bool__(self):
        return len(self) > 0

    def __iter__(self):
        class _Iterator:
            def __init__(self, stack):
                self._stack = stack
                self._index = stack._len - 1

            def __next__(self):
                if self._index < 0:
                    raise StopIteration
                res = self._stack._data[self._index]
                self._index -= 1
                return res

        return _Iterator(self)

    def __len__(self):
        return self._len


class StackMax(Stack):
    def get_max(self):
        res = None
        for el in self:
            if res is None or el > res:
                res = el
        return res


def parse_input_cmd(line, stack):
    cmd, args = line.split()[0], line.split()[1:]
    match cmd:
        case "push":
            stack.push(int(args[0]))
        case "get_max":
            return stack.get_max()
        case "pop":
            return stack.pop()
        case "peek":
            return stack.peek()
        case _:
            raise ValueError(f"Invalid command: {cmd}")


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        stack = StackMax(n)
        for i in range(n):
            cmd = inp.readline().strip()
            try:
                res = parse_input_cmd(cmd, stack)
            except Exception as e:
                res = "error"
            if cmd == "get_max" or cmd == "peek" or res == "error":
                print(res, file=outp)
