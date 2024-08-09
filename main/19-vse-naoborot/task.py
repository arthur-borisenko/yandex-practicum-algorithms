# From template
import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"


class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class TwoLinkedList:
    """2 - Linked list data structure
    supports: reverse
    methods which names starts with _ are internal and
     may not be used outside this class
    """

    def __init__(self, head=None):
        """
        CPU - O(n)
        n - len of initial data
        :param head: initial data head
        """
        self.head = DoubleConnectedNode(None, head)
        self.tail = self.head
        self._len: int = 0
        self.head.next = head
        while self.tail.next:
            self.tail = self.tail.next

    def __iter__(self):
        base = self

        class _Iterator:
            def __init__(self):
                self._base = base
                self.current = self._base.head

            def __next__(self):
                if self.current.next:
                    self.current = self.current.next
                    return self.current
                else:
                    raise StopIteration

        return _Iterator()

    def reverse(self):
        """
        CPU - O(n)
        RAM - O(n)
        """
        nodes = []
        for node in self:
            nodes.append(node)
        for node in nodes:
            (node.prev, node.next) = (node.next, node.prev)
        (self.head, self.tail) = (self.tail, self.head)


# solution
def solution(head):
    """
    CPU - O(n)
    RAM - O(n)
    :param head:
    :return:
    """
    l = TwoLinkedList(head)
    l.reverse()
    return l.head


# From template
def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node2.prev is node3
    assert node1.next is node0
    assert node1.prev is node2
    assert node0.prev is node1


if __name__ == "__main__":
    test()
