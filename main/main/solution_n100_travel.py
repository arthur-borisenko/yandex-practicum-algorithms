class AVLTree:
    class Node:
        def __init__(self, value, height=1, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right
            self.height = height
    def __init__(self):
        self.root = None
        self._len=0
    def __len__(self):
        return self._len

    def _get_height(self, node):
        return node.height if node is not None else 0
    def _recalc_height(self, node):
        node.height= max(self._get_height(node.left), self._get_height(node.right)) + 1
    def _small_left_rotation(self, a):
        b = a.right
        C = b.left

        a.right = C
        b.left = a
        self._recalc_height(a)
        self._recalc_height(b)

        return b

    def _small_right_rotation(self, a):
        b = a.left
        C = b.right

        a.left = C
        b.right = a
        self._recalc_height(a)
        self._recalc_height(b)
        return b

    def _big_left_rotation(self, v):
        v.right = self._small_right_rotation(v.right)
        self._recalc_height(v)
        return self._small_left_rotation(v)

    def _big_right_rotation(self, v):
        v.left = self._small_left_rotation(v.left)
        self._recalc_height(v)
        return self._small_right_rotation(v)

    def _rotate(self, vertex):
        if vertex is None:
            return vertex

        left_h = self._get_height(vertex.left)
        right_h = self._get_height(vertex.right)
        balance = left_h - right_h

        if abs(balance) < 2:
            return vertex

        if balance == -2:
            b = vertex.right
            R = b.right
            C = b.left

            if self._get_height(C) <= self._get_height(R):
                return self._small_left_rotation(vertex)
            else:
                return self._big_left_rotation(vertex)
        if balance == 2:
            b = vertex.left
            L = b.left
            C = b.right

            if self._get_height(C) <= self._get_height(L):
                return self._small_right_rotation(vertex)
            else:
                return self._big_right_rotation(vertex)

        return vertex
    def _insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
            return self.root
        current=self.root
        fuck=[]
        while True:
            fuck.append(current)
            if value < current.value:
                if current.left:
                    current=current.left
                else:
                    current.left=self.Node(value)
                    for n in reversed(fuck): self._recalc_height(n)
                    return self.root
            elif value > current.value:
                if current.right:
                    current=current.right
                else:
                    current.right=self.Node(value)
                    self._recalc_height(current)
                    for n in reversed(fuck): self._recalc_height(n)
                    return self.root
            else:
                raise ValueError("value is already in tree")
    def insert(self, value):
        """Inserts new node and performs rotation"""
        self.root = self._rotate(self._insert(value))
        self._len+=1
    def binary_nearest_search(self, target):
        """Returns node with maximum value that is less or equal to target."""
        current=self.root
        if self.root is None:
            return None
        while True:
            if current.value == target:
                return current
            elif current.value > target:
                if current.left:
                    current = current.left
                else:
                    return None
            elif current.value < target:
                if current.right and current.right.value <= target:
                    current = current.right
                else:
                    return current
def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        l = list(map(int, inp.readline().split()))
        t=AVLTree()
        p0 = [0 for _ in range(n)]
        for i in range(n):
            rr=t.binary_nearest_search((l[i]-1, 0))
            mvi=rr.value[1] if rr is not None else None
            p0[i]=(p0[mvi] if mvi is not None else 0)+1
            t.insert((l[i], i))
        r = []
        mx = 0
        ii = 0
        for i, el in enumerate(p0):
            if el > mx:
                mx = el
                ii = i
        pv = mx + 1
        while ii >= 0:
            if p0[ii] == pv - 1:
                r.append(ii)
                pv = p0[ii]
            ii -= 1
        print(mx, file=out)
        print(*reversed(r), file=out)


if __name__ == "__main__":
    main()
