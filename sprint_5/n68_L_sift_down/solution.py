def sift_down(heap, idx) -> int:
    target_i = idx
    while True:
        heap_max_index = len(heap) - 1
        left = target_i * 2
        right = target_i * 2 + 1
        if left > heap_max_index:
            return target_i

        if right <= heap_max_index and heap[right] > heap[left]:
            max_child_i = right
        else:
            max_child_i = left
        if heap[target_i] >= heap[max_child_i]:
            return target_i
        heap[max_child_i], heap[target_i] = heap[target_i], heap[max_child_i]
        target_i = max_child_i
    #  “ヽ(´▽｀)ノ”


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == "__main__":
    test()
