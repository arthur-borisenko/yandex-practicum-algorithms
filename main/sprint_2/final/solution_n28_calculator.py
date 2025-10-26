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

    def __len__(self):
        return self._len


def calculate(task):
    operands = Stack(len(task))
    for el in task:
        match el:
            case "+":
                op2, op1 = operands.pop(), operands.pop()
                operands.push(op1 + op2)
            case "-":
                op2, op1 = operands.pop(), operands.pop()
                operands.push(op1 - op2)
            case "*":
                op2, op1 = operands.pop(), operands.pop()
                operands.push(op1 * op2)
            case "/":
                op2, op1 = operands.pop(), operands.pop()
                operands.push(op1 // op2)
            case _:
                operands.push(int(el))
    return operands.peek()


def main():
    """CPU - O(n)
    RAM - O(n)
    n - number of operands"""
    with (
        open("input.txt", "r") as inp,
        open("output.txt", "w") as outp,
    ):
        print(calculate(inp.readline().split()), file=outp)


if __name__ == "__main__":
    main()
