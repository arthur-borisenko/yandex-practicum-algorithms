from io import StringIO

fuck=StringIO("""examiwillpasstheexam
5
will
pass
the
exam
i
""")
def prefix_function(s):
    # Функция возвращает массив длины |s|
    n = len(s)
    prefix_func = [None] * n
    prefix_func[0] = 0
    for i in range(1, n):
        suffix_start_i = prefix_func[i - 1]
        while suffix_start_i > 0 and s[suffix_start_i] != s[i]:
            suffix_start_i = prefix_func[suffix_start_i - 1]
        if s[suffix_start_i] == s[i]:
            suffix_start_i += 1
        prefix_func[i] = suffix_start_i
    return prefix_func
def find_all(s, p):
    sep=chr(31)
    pf=prefix_function(p+sep+s)
    rs=[]
    for ii, el in enumerate(pf):
        i=ii-len(p)
        if i<0:
            continue
        if el == len(p):
            rs.append((i-len(p)+1, i+1))
    return rs
a=fuck.readline().strip()
n=int(fuck.readline())
ss=[]
for iii in range(n):
    ss.append(fuck.readline().strip())
    print(find_all(a, ss[-1]))