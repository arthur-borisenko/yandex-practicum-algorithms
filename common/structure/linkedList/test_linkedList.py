import unittest

from common.structure.linkedList.LinkedList import LinkedList


class TestCase(unittest.TestCase):
    def test_empty(self):
        ll = LinkedList()
        self.assertEqual(len(ll), 0)
        iter_len = 0
        for el in ll:
            iter_len += 1
        self.assertEqual(iter_len, 0)

    def test_append_iterate(self):
        ll = LinkedList()
        dt = []
        for i in range(100):
            ll.append(i * 2)
            dt.append(i * 2)
            self.assertEqual(len(ll), i + 1)
            j = -1
            el = ll.tail
            for j, el in enumerate(ll):
                self.assertEqual(dt[j], el.value)
            self.assertEqual(j, i)
            self.assertEqual(ll.tail, el)

    def test_insert(self):
        ll = LinkedList()
        ll = LinkedList()
        for i in range(100):
            ll.append(i * 2)
        self.assertEqual(len(ll), 100)
        n1 = ll._create_node(ll.head.next_item.next_item.next_item, "cat")
        self.assertEqual(len(ll), 101)
        self.assertEqual(ll.head.next_item.next_item.next_item.next_item, n1)
        self.assertEqual(n1.value, "cat")
        n2 = ll._create_node(ll.tail, "dog")
        self.assertEqual(len(ll), 102)
        self.assertEqual(ll.tail, n2)
        self.assertEqual(n2.value, "dog")

    def test_remove(self):
        ll = LinkedList()
        for i in range(100):
            ll.append(i * 2)
        old_n1 = ll.head.next_item.next_item
        ll._delete_node(ll.head)
        self.assertEqual(len(ll), 99)
        self.assertEqual(ll.head.next_item, old_n1)
        del ll[98]
        self.assertEqual(len(ll), 98)
        self.assertEqual(ll.tail, ll[97])
