import time
from matplotlib import pyplot
import main.common.structures.hashmap as hm


def o1(n):
    return


def on(n):
    a = list(range(n)) * 100
    return


def on2(n):
    a = 0
    for i in range(n):
        for j in range(n):
            a += i + j


def hmm(n):

    a = 0
    m = hm.HashMap()
    for i in range(n):
        m[i] = i * 2
    for i in range(n):
        a += m[i]


def plot(*ms):
    for m, color in ms:
        x = 1000000
        points = {}
        n = 10
        while n < x:
            n = int(n * 1.25)
            t_s = time.time()
            m(n)
            t_e = time.time()
            points[n] = t_e - t_s
        pyplot.plot(list(points.keys()), list(points.values()), color=color)
    pyplot.show()


plot((o1, "grey"), (on, "black"), (hmm, "red"))
