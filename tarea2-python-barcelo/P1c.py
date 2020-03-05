from numpy import *


class P1c:
    a = zeros(100)
    b = zeros(100)
    c = zeros(100)

    @staticmethod
    def f(i):
        P1c.a[0] = 1
        if (P1c.a[i % 100]) != 0:
            return P1c.a[i % 100]
        else:
            P1c.a[i % 100] = (5 * P1c.f(i - 1) + 2 * P1c.g(i - 1)) % 100
            return P1c.a[i % 100]

    @staticmethod
    def g(i):
        P1c.b[0] = 2
        if (P1c.b[i % 100]) != 0:
            return P1c.b[i % 100]
        else:
            P1c.b[i % 100] = (3 * P1c.f(i - 1) + P1c.g(i - 1)) % 100
            return P1c.b[i % 100]

    @staticmethod
    def h(i):
        return P1c.f(i) + P1c.g(i)

    @staticmethod
    def sumatoria(k):
        m = 1000000007
        P1c.c[0] = P1c.h(0)
        for i in range(1, 100):
            P1c.c[i] = P1c.c[i - 1] + P1c.h(i)
        return (P1c.c[int(k % 100)] + int(k//100) * P1c.c[99]) % m

    @staticmethod
    def main():
        k = int(input("k= "))
        print("resultadoSumatoria = ", P1c.sumatoria(k))


p = P1c()
if __name__ == '__main__':
    p.main()
