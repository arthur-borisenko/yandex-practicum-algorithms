import time


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
    def __init__(self, initial):
        self._data = LinkedList()
        for el in initial:
            self.push(el)

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


def main():
    """CPU - O(n)
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        c1 = time.perf_counter() * 1000
        s = inp.readline().strip()
        t = inp.readline().strip()
        s_q = LinkedListQueue(s)
        c2 = time.perf_counter() * 1000
        for el in t:
            if len(s_q) != 0 and s_q.peek() == el:
                s_q.pop()
        c3 = time.perf_counter() * 1000
        print(c2 - c1, c3 - c2, c3 - c1, file=outp)
        print(len(s_q) == 0, file=outp)


if __name__ == "__main__":
    main()
