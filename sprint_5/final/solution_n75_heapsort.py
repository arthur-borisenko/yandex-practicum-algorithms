class MaxHeap:
    def __init__(self, cmp_func):
        self.heap = []
        self.cmp = cmp_func

    def sift_up(self, idx) -> int:
        heap = self.heap
        target_index = idx
        parent_index = target_index // 2
        while (
            target_index > 0 and self.cmp(heap[target_index], heap[parent_index]) == 1
        ):
            heap[target_index], heap[parent_index] = (
                heap[parent_index],
                heap[target_index],
            )
            target_index = parent_index
            parent_index = target_index // 2
            pass
        return target_index

    #  “ヽ(´▽｀)ノ”

    def sift_down(self, idx) -> int:
        heap = self.heap
        target_i = idx
        while True:
            heap_max_index = len(heap) - 1
            left = target_i * 2
            right = target_i * 2 + 1
            if left > heap_max_index:
                return target_i

            if right <= heap_max_index and self.cmp(heap[right], heap[left]) == 1:
                max_child_i = right
            else:
                max_child_i = left
            if self.cmp(heap[target_i], heap[max_child_i]) != -1:
                return target_i
            heap[max_child_i], heap[target_i] = heap[target_i], heap[max_child_i]
            target_i = max_child_i
        #  “ヽ(´▽｀)ノ”

    def add(self, value):
        self.heap.append(value)
        return self.sift_up(len(self.heap) - 1)

    def remove(self, index):
        self.heap[index], self.heap[-1] = self.heap[-1], self.heap[index]
        self.heap.pop()
        self.sift_down(index)

    def get(self, index):
        return self.heap[index]

    def size(self):
        return len(self.heap)

    def max(self):
        return self.heap[0]

    def __len__(self):
        return self.size()


def cmpf(a: tuple[int, int, str], b: tuple[int, int, str]):
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1

    if a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1

    if a[2] < b[2]:
        return 1
    elif a[2] > b[2]:
        return -1

    return 0


def heapsort(arr):
    heap = MaxHeap(cmp_func=cmpf)
    for el in arr:
        heap.add(el)
    while len(heap) > 0:
        yield heap.max()
        heap.remove(0)


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = inp.readline()
        n = int(n)
        array = []
        for i in range(n):
            line = inp.readline()
            data = line.split()
            array.append((int(data[1]), int(data[2]), data[0]))
        sorted_data = heapsort(array)
        print(*map(lambda x: x[2], sorted_data), sep="\n", file=out)


if __name__ == "__main__":
    main()
