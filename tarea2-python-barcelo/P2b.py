from numpy import *


class P2b:
    @staticmethod
    def main():
        a = input().split()
        hx = float(a[0])
        J = float(a[1])
        k = float(a[2])
        G = zeros(int(k))
        h = zeros(int(k))
        for i in range(0, int(k)):
            a = input().split()
            G[i] = a[0]
            h[i] = a[1]
        p = (G[0]) / (hx + h[0])
        for i in range(1, int(k)):
            p = p + (G[i]) / (hx + h[i])
        p = p * (hx / J)
        print("Resultado:")
        print(p)


asd = P2b()
if __name__ == '__main__':
    asd.main()
