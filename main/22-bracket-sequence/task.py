from array import array

BRACKETS = {"(": ")", "[": "]", "{": "}"}


class Stack:

    def __init__(self, size):
        self._len = 0
        self.size = size
        self._data = array(
            "u", "-" * size
        )  # using - as empty value because array item must be unicode character

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


class SafeStack(Stack):
    def safe_peek(self):
        if self._len == 0:
            return None
        else:
            return self.peek()


def check_closing_bracket(opening, closing):
    return BRACKETS.get(opening, None) == closing


def check_bracket_sequence(seq: str):
    """CPU - O(n)
    RAM - O(n)"""
    open_brackets = SafeStack(len(seq))
    for bracket in seq:
        if check_closing_bracket(open_brackets.safe_peek(), bracket):
            open_brackets.pop()
        else:
            open_brackets.push(bracket)
    return not open_brackets


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        print(check_bracket_sequence(inp.readline().strip()), file=outp)


if __name__ == "__main__":
    main()
