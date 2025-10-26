import random
import time
from matplotlib import pyplot
import common.structure.hashmap.hashmap as hm


def o1(n, k):
    a = 0
    for i in range(k):
        a += 1
    return


def on(n, k):
    for i in range(k):
        a = list(range(n)) * i
    return


def on2(n, k):
    a = 0
    for i in range(k):
        for i in range(n):
            for j in range(n):
                a += i + j


def hmm(n, k):

    a = 0
    m = hm.HashMap()
    for i in range(n):
        m[i] = i * 2
    randint = random.randint(0, 10000000)
    t_s = time.time()
    for i in range(k):
        a += m[n - 1]
        m[n - 1] = randint
    t_e = time.time()
    return t_e - t_s


# и помнишь график с хешмапой, там был некорректность - там была зависимость от числа запрросов. я исправил на количество элементов
def plot(*ms):
    for m, color in ms:
        x = 300000
        points = {}
        k = 300000
        n = 10
        while n < x:
            n = int(n * 2)
            t_s = time.time()
            res_t = m(n, k)
            t_e = time.time()
            points[n] = t_e - t_s if res_t is None else res_t
        pyplot.plot(list(points.keys()), list(points.values()), color=color)
    pyplot.show()


plot((o1, "grey"), (hmm, "red"))
