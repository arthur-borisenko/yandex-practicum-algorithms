import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.tail = self.head
        while self.tail and self.tail.next_item:
            self.tail = self.tail.next_item
        self._len: int = 0

    def _get_node(self, i: int):
        if not self.head:
            raise IndexError
        res = self.head
        for i in range(i):
            if res.next_item is None:
                raise IndexError
            res = res.next_item
        return res

    def _delete_node(self, prev_node):
        if prev_node.next_item == self.tail:
            self.tail = prev_node
        prev_node.next_item = prev_node.next_item.next_item

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


def solution(node, idx):
    """
    CPU - O(n)
    RAM - O(1)
    n - index
    :param node:
    :param idx:
    :return:
    """
    l = LinkedList(node)
    del l[idx]
    return l.head


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == "__main__":
    test()
