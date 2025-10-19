from array import array


class Stack:

    def __init__(self, size):
        self._len = 0
        self.size = size
        self._data = array("q", (0,) * size)

    def push(self, item):
        """CPU - O(1)
        RAM - O(1)"""
        if self._len == self.size:
            raise OverflowError("Stack overflow")
        self._data[self._len] = item
        self._len += 1

    def pop(self):
        """CPU - O(1)
        RAM - O(1)"""
        if self._len == 0:
            raise IndexError("Stack underflow")
        res = self.peek()
        self._len -= 1
        return res

    def peek(self):
        """CPU - O(1)
        RAM - O(1)"""
        if self._len == 0:
            raise IndexError("Attempted to get element of empty stack")
        return self._data[self._len - 1]

    def __bool__(self):
        """CPU - O(1)
        RAM - O(1)"""
        return len(self) > 0

    def __len__(self):
        """CPU - O(1)
        RAM - O(1)"""
        return self._len


class StackMaxEffective:
    def __init__(self, size):
        self.size = size
        self._data = Stack(size)
        self._maximums = Stack(size)

    def push(self, x):
        """CPU - O(1)
        RAM - O(1)"""
        if self.__len__() == self.size:
            raise OverflowError("Stack overflow")
        self._data.push(x)
        if self._maximums and self._maximums.peek() > x:
            current_max = self._maximums.peek()
        else:
            current_max = x
        self._maximums.push(current_max)

    def __len__(self):
        """CPU - O(1)
        RAM - O(1)"""
        return len(self._data)

    def pop(self):
        """CPU - O(1)
        RAM - O(1)"""
        self._maximums.pop()
        return self._data.pop()

    def peek(self):
        """CPU - O(1)
        RAM - O(1)"""
        return self._data.peek()

    def __bool__(self):
        """CPU - O(1)
        RAM - O(1)"""
        return bool(self._data)

    def get_max(self):
        """CPU - O(1)
        RAM - O(1)"""
        if self._maximums:
            return self._maximums.peek()
        return None


def run_input_cmd(line, stack):
    cmd, args = line.split()[0], line.split()[1:]
    match cmd:
        case "push":
            stack.push(int(args[0]))
        case "get_max":
            return stack.get_max()
        case "pop":
            return stack.pop()
        case "top":
            return stack.peek()
        case _:
            raise ValueError(f"Invalid command: {cmd}")


def main():
    """CPU - O(n)
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        stack = StackMaxEffective(n)
        for i in range(n):
            cmd = inp.readline().strip()
            try:
                res = run_input_cmd(cmd, stack)
            except:
                res = "error"
            if cmd == "get_max" or cmd == "top" or res == "error":
                print(res, file=outp)


if __name__ == "__main__":
    main()
