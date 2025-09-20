def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as out:
        a = inp.readline()
        i = 0
        fuck = ""
        while i < len(a):
            ii = i
            while a[ii] != " ":
                if ii == len(a) - 1:
                    break
                ii += 1
            fuck += " "
            iii = ii if a[ii] != " " else ii - 1
            while iii >= i:
                fuck += a[iii]
                iii -= 1
            i = ii + 1
        print(fuck[::-1], file=out)
