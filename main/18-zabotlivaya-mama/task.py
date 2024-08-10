

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


pass


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self._len: int = 0

    def find_first(self, value):
        """
        CPU - O(n)
        RAM - O(1)
        :param value:
        :return:
        """
        for i, el in enumerate(self):
            if el.value == value:
                return i
        return -1

    def __iter__(self):
        base: LinkedList = self

        class _Iterator:
            def __init__(self):
                self._base = base
                self.current = self._base.head

            def __next__(self):
                if self.current.next_item:
                    self.current = self.current.next_item
                    return self.current
                else:
                    raise StopIteration

        return _Iterator()


def solution(node, value):
    """
    CPU - O(n)
    RAM - O(1)
    :param node:
    :param value:
    :return:
    """
    l = LinkedList()
    l.head.next_item = node
    return l.find_first(value)


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2


if __name__ == "__main__":
    test()
