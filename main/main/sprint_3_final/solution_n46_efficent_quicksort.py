def find_pivot(array, left, right):
    return sorted((array[left+(right-left)//2], array[left], array[right]))[1]
def reorder(array, pivot, left, right, cmp_func):
    left1=left
    right1=right
    while right>left:
        if left >= right:
            break
        while cmp_func(array[left], pivot)==-1:
            left+=1
        while cmp_func(array[right], pivot)==1:
            right-=1
        array[left], array[right] = array[right], array[left]
    center_start=None
    center_end=None
    while left1<=right1:
        if array[left1] == pivot:
            if center_start is None:
                center_start=left1
        if array[left1] == pivot:
            center_end=left1
        left1+=1
    return center_start, center_end
def quicksort(array, left, right, cmp_func):
    if left >= right:
        return
    pivot=find_pivot(array, left, right)
    center_start, center_end=reorder(array, pivot, left, right, cmp_func)
    quicksort(array, left, center_start-1, cmp_func)
    quicksort(array, center_end+1, right, cmp_func)
def _cmp(n1, p1, f1, n2, p2, f2):
    if p1 < p2:
        return 1
    if p1>p2:
        return -1
    if f1 < f2:
        return -1
    if f1 > f2:
        return 1
    if n1 < n2:
        return -1
    if n1 > n2:
        return 1
    return 0
def cmp(a, b):
    return _cmp(a[0], a[1], a[2], b[0], b[1], b[2])
def main():
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        n = inp.readline()
        n = int(n)
        array = []
        for i in range(n):
            line = inp.readline()
            array.append((line.split()[0], int(line.split()[1]), int(line.split()[2])))
        quicksort(array, 0, n-1, cmp)
        print(*map(lambda x: x[0], array), sep="\n", file=outp)
if __name__=="__main__":
    main()