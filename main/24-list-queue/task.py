class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class LinkedList:
    """Linked list data structure
    supports: add, insert, iterate, slice, get item, delete item,
     string interpretation, equality
    methods which names starts with _ are internal and
     may not be used outside this class
    """

    def __init__(self):
        self.head: Node = Node(None)
        self.tail = self.head
        self._len: int = 0

    def _get_node(self, i: int):
        res = self.head
        for i in range(i + 1):
            if res.next_item is None:
                raise IndexError
            res = res.next_item
        return res

    def _create_node(self, after_node, data):
        next_node = after_node.next_item
        new_node = Node(None, next_node)
        after_node.next_item = new_node
        self._len += 1
        node = new_node
        node.value = data
        self.tail = node
        return node

    def append(self, data):
        """
        add element to end of LinkedList
        difficulty O(1)
        :param data: data of new node
        :return: new node
        """
        after_node = self.tail
        node = self._create_node(after_node, data)
        return node

    def _delete_node(self, prev_node: Node):
        if prev_node.next_item == self.tail:
            self.tail = prev_node
        prev_node.next_item = prev_node.next_item.next_item
        self._len -= 1

    def __delitem__(self, index):
        """
        deletes
        can be used with standard python syntax
        difficulty O(n)
        n - index
        :param index: index
        :return: None
        """
        prev_node = self._get_node(index - 1)
        self._delete_node(prev_node)

    def __len__(self):
        return self._len

    def __getitem__(self, index):
        """
        get item by index
        can be used with standard python syntax
        difficulty O(n)
        n - index
        :param index: index or slice without step
        :return: node or sliced list
        """
        node = self._get_node(index)
        return node


class LinkedListQueue:
    def __init__(self):
        self._data = LinkedList()

    def push(self, item):
        self._data.append(item)

    def pop(self):
        res = self.peek()
        del self._data[0]
        return res

    def peek(self):
        return self._data[0].value

    def __len__(self):
        return self._data.__len__()


def parse_input_cmd(line, queue):
    cmd, args = line.split()[0], line.split()[1:]
    match cmd:
        case "put":
            queue.push(int(args[0]))
        case "size":
            return len(queue)
        case "get":
            return queue.pop()
        case _:
            raise ValueError(f"Invalid command: {cmd}")


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        queue = LinkedListQueue()
        for i in range(n):
            cmd = inp.readline().strip()
            try:
                res = parse_input_cmd(cmd, queue)
            except IndexError:
                print("error", file=outp)
            else:
                if res is not None:
                    print(res, file=outp)
        pass  # 66 -41 96 0 42 44 -43 -37


if __name__ == "__main__":
    main()
