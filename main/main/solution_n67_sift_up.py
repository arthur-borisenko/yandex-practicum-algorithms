def sift_up(heap, idx) -> int:
    target_index = idx
    parent_index = target_index // 2
    while target_index > 1 and heap[target_index] > heap[parent_index]:
        heap[target_index], heap[parent_index] = heap[parent_index], heap[target_index]
        target_index = parent_index
        parent_index = target_index // 2
        pass
    return target_index
    #  “ヽ(´▽｀)ノ”


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == "__main__":
    test()
