import os



class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class LinkedList:
    """Linked list data structure
    supports: iterate
    """

    def __init__(self, head=None):
        self.head: Node = Node(None, head)
        self.tail = self.head
        self._len: int = 0

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


def solution(node):
    """CPU - O(n)
    RAM - O(1)"""
    with open("output.txt", "w") as outp:
        l = LinkedList(node)
        for el in l:
            print(el.value, file=outp)


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    # Output is:
    # node0
    # node1
    # node2
    # node3


if __name__ == "__main__":
    test()
