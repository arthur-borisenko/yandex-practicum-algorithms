def main():
    inp = open("input.txt", "r")
    out = open("output.txt", "w")
    n, k = map(int, inp.readline().split())
    mtx = []
    for i in range(n):
        mtx.append([])
        for j in range(n):
            mtx[i].append(0)
    for ribble in inp.readlines():
        v1, v2 = map(int, ribble.split())
        mtx[v1 - 1][v2 - 1] = 1
        # uncomment this if graph is not directional
        # mtx[v2 - 1][v1 - 1]=1
    print(*map(lambda x: " ".join(map(str, x)), mtx), sep="\n")
    inp.close()
    out.close()


if __name__ == "__main__":
    main()
