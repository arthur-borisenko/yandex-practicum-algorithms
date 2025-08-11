def sift_up(heap, idx) -> int:
    """CPU - O(h)
    RAM - O(1)
    """
    target_i = idx
    parent_i = target_i // 2
    while target_i > 1 and heap[target_i] > heap[parent_i]:
        heap[target_i], heap[parent_i] = heap[parent_i], heap[target_i]
        target_i = parent_i
        parent_i = target_i // 2
        pass
    return target_i
    #  “ヽ(´▽｀)ノ”


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == "__main__":
    test()
