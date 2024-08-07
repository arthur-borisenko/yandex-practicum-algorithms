# From template
import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class DoubleConnectedNode:
        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev

# solution
def solution(head):
    Node_class = head.__class__

    class TwoLinkedList:
        """Linked list data structure
        supports: add, insert, iterate, slice, get item, delete item,
         string interpretation, equality
        methods which names starts with _ are internal and
         may not be used outside this class
        """

        def __init__(self):
            self.head: Node_class = Node_class(None)
            self.tail = self.head
            self._len: int = 0

        def _get_node(self, i: int):
            if i < self._len / 2:
                res = self.head
                for i in range(i + 1):
                    if res.next is None:
                        raise IndexError
                    res = res.next
            else:
                res = self.tail
                i = self._len - i
                for i in range(i + 1):
                    if res.prev is None:
                        raise IndexError
                    res = res.prev
            return res

        def _create_node(self, after_node, data):
            next_node = after_node.next
            new_node = Node_class(None, next_node, after_node)
            after_node.next = new_node
            next_node.prev = new_node
            self._len += 1
            node = new_node
            node.value = data
            self.tail = node
            return node

        def insert(self, data, after: int):
            """
            insert element to LinkedList
            difficulty O(n)
            :param data: data of new node
            :param after: index of new node
            :return: new node
            """
            after_node = self._get_node(after)
            node = self._create_node(after_node, data)
            return node

        def add(self, data):
            """
            add element to end of LinkedList
            difficulty O(1)
            :param data: data of new node
            :return: new node
            """
            after_node = self.tail
            node = self._create_node(data, after_node)
            return node

        def _delete_node(self, prev_node: Node_class):
            if prev_node.next == self.tail:
                self.tail = prev_node

            prev_node.next = prev_node.next.next
            if prev_node.next.next:
                prev_node.next.next.prev = prev_node

        def _slice(self, start, stop, step):
            start = start if start else 0
            stop = stop if stop else len(self)
            step = step if step else 1
            node = self._get_node(start)
            new_l = self.__class__()
            for i in range(stop - start):
                if not node:
                    raise IndexError
                if i % step == 0:
                    new_l.add(node.value)
                node = node.next
            return new_l

        def __delitem__(self, key):
            """
            deletes
            can be used with standard python syntax
            difficulty O(n)
            :param key: index
            :return: None
            """
            prev_node = self._get_node(key - 1)
            self._delete_node(prev_node)

        def __eq__(self, other):
            """equality check
            difficulty O(n)"""
            if len(self) != len(other):
                return False
            else:
                current = self.head.next
                for el in other:
                    if el.value != current.value:
                        return False
                    current = current.next_item
            return True

        def __repr__(self):
            return str(self)

        def __ne__(self, other):
            """inversed equality check
            difficulty O(n)"""
            return not self == other

        def __len__(self):
            return self._len

        def __str__(self):
            """convert to string of format
            LinkedList(value1, value2, ..., valueN, )
            difficulty O(n)"""
            res = "LinkedList("
            for el in self:
                res += (
                    str(el.value if not isinstance(el.value, str) else f"'{el.value}'")
                    + ", "
                )
            res += ")"
            return res

        def __getitem__(self, key):
            """
            gets items and performs slices
            can be used with standard python syntax
            difficulty O(n)
            :param key: index or slice without step
            :return: node or sliced list
            """
            if isinstance(key, int):
                node = self._get_node(key)
                return node
            elif isinstance(key, slice):
                return self._slice(key.start, key.stop, key.step)

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

        def __reversed__(self):
            base = self

            class _Iterator:
                def __init__(self):
                    self._base = base
                    self.current = self._base.tail

                def __next__(self):
                    if self.current.prev:
                        self.current = self.current.prev
                        return self.current
                    else:
                        raise StopIteration

            return _Iterator()

        def reverse(self):
            nodes = []
            for node in self:
                nodes.append(node)
            for node in nodes:
                (node.prev, node.next) = (node.next, node.prev)
            (self.head, self.tail) = (self.tail, self.head)

    l = TwoLinkedList()
    l.head.next = head
    tail = head
    while tail.next:
        tail = tail.next
    l.tail = tail
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
