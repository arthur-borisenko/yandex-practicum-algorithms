import array
from typing import Iterable

MAX_NUMBER=10000000
class Node:
    def __init__(self, value,prev_item, next_item=None):
        self.value = value
        self.next_item = next_item
        self.prev_item=prev_item
class LinkedList:
    """Linked list data structure
    supports: add, insert, iterate, slice, get item, delete item,
     string interpretation, equality
    methods which names starts with _ are internal and
     may not be used outside this class
    """

    def __init__(self, init_data=[]):
        self.head: Node = Node(None, None)
        self.tail = self.head
        self._len: int = 0
        for item in init_data:
            self.add(item)


    def _get_node(self, i: int):
        res = self.head
        for i in range(i + 1):
            if res.next_item is None:
                raise IndexError
            res = res.next_item
        return res

    def _create_node(self, after_node, data):
        next_node = after_node.next_item
        new_node = Node(data, after_node, next_node)
        after_node.next_item = new_node
        if next_node is not None:
            next_node.prev_item = new_node
        self._len += 1
        if after_node == self.tail:
            self.tail = new_node
        return new_node

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
        node = self._create_node(after_node, data)
        return node

    def _delete_node(self, prev_node: Node):
        if prev_node.next_item == self.tail:
            self.tail = prev_node
        prev_node.next_item = prev_node.next_item.next_item
        prev_node.next_item.next_item.prev_item=prev_node

    def _slice(self, start, stop, step):
        start = start if start else 0
        stop = stop if stop else len(self)
        step = step if step else 1
        node = self._get_node(start)
        new_l = LinkedList()
        for i in range(stop - start):
            if not node:
                raise IndexError
            if i % step == 0:
                new_l.add(node.value)
            node = node.next_item
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
            current = self.head.next_item
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
        raise TypeError

    def __iter__(self) -> Iterable[Node]:
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


def main():
    """CPU - ???
    RAM - ???"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n=int(inp.readline())
        vals=sorted(map(int, inp.readline().split()))
        k=int(inp.readline())
        minimals=LinkedList([MAX_NUMBER+1]*k)
        diffs=[]
        for idx, val in enumerate(vals):
            for idx2, val2 in enumerate(vals):
                if idx<=idx2:
                    continue
                diff=abs(val2-val)
                diffs.append([val,val2,diff,idx,idx2])
                if diff<minimals[k-1].value:
                    for el in minimals:
                        if el.value>diff:
                            minimals._create_node(el.prev_item,diff)
                            minimals.tail=minimals.tail.prev_item
                            minimals.tail.next_item = None
                            minimals._len-=1
                            break
        print(minimals[k-1].value, file=outp)

if __name__ == '__main__':
    main()


