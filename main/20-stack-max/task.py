from array import array


class Stack:

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

    def __len__(self):
        return self._len


class StackMax:
    def __init__(self, size):
        self.size = size
        self._data = Stack(size)
        self._maximums = Stack(size)

    def push(self, x):
        if self.__len__() == self.size:
            raise OverflowError("Stack overflow")
        self._data.push(x)
        if self._maximums and self._maximums.peek() > x:
            current_max = self._maximums.peek()
        else:
            current_max = x
        self._maximums.push(current_max)

    def __len__(self):
        return len(self._data)

    def pop(self):
        self._maximums.pop()
        return self._data.pop()

    def peek(self):
        return self._data.peek()

    def __bool__(self):
        return bool(self._data)

    def get_max(self):
        if self._maximums:
            return self._maximums.peek()
        return None


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
