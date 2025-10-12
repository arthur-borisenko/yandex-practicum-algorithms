class AVLTree:
    class Node:
        def __init__(self, value, height=1, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right
            self.height = height
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node is not None else 0
    def small_left_rotation(self, a):
        b = a.right
        C = b.left

        a.right = C
        b.left = a
        a.height = max(self.get_height(a.left),
                       self.get_height(C)) + 1
        b.height = max(self.get_height(b.right), a.height) + 1

        return b

    def small_right_rotation(self, a):
        b = a.left
        C = b.right

        a.left = C
        b.right = a
        a.height = max(self.get_height(a.right),
                       self.get_height(C)) + 1
        b.height = max(self.get_height(b.left), a.height) + 1

        return b

    def big_left_rotation(self, v):
        v.right = self.small_right_rotation(v.right)
        return self.small_left_rotation(v)

    def big_right_rotation(self, v):
        v.left = self.small_left_rotation(v.left)
        return self.small_right_rotation(v)

    def rotate(self, vertex):
        if vertex is None:
            return vertex

        left_h = self.get_height(vertex.left)
        right_h = self.get_height(vertex.right)
        balance = left_h - right_h

        if abs(balance) < 2:
            return vertex

        if balance == -2:
            b = vertex.right
            R = b.right
            C = b.left

            if self.get_height(C) <= self.get_height(R):
                return self.small_left_rotation(vertex)
            else:
                return self.big_left_rotation(vertex)
        if balance == 2:
            b = vertex.left
            L = b.left
            C = b.right

            if self.get_height(C) <= self.get_height(L):
                return self.small_right_rotation(vertex)
            else:
                return self.big_right_rotation(vertex)

        return vertex
    def _insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
            return self.root
        current=self.root
        while True:
            if value < current.value:
                if current.left:
                    current=current.left
                else:
                    current.left=self.Node(value)
                    return self.root
            elif value > current.value:
                if current.right:
                    current=current.right
                else:
                    current.right=self.Node(value)
                    return self.root
            else:
                raise ValueError("value is already in tree")
    def insert(self, value):
        self.root = self.rotate(self._insert(value))
