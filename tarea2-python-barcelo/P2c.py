from numpy import *


class Nodo:
    vecinos = []
    visitado = False


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def setgrafo(matriz, n, m):
    hashmaps = {}
    for i in range(n):
        for j in range(m):
            nodo = Nodo()
            if i < n - 1:
                if matriz[i][j] == matriz[i + 1][j]:
                    nodo.vecinos.append(str(i + 1) + "," + str(j))
            if i > 0:
                if matriz[i][j] == matriz[i - 1][j]:
                    nodo.vecinos.append(str(i - 1) + "," + str(j))
            if j < m - 1:
                if matriz[i][j] == matriz[i][j + 1]:
                    nodo.vecinos.append(str(i) + "," + str(j + 1))
            if j > 0:
                if matriz[i][j] == matriz[i][j - 1]:
                    nodo.vecinos.append(str(i) + "," + str(j - 1))
            hashmaps[matriz[i][j]][str(i) + "," + str(j)] = nodo
    return hashmaps


def buscarCiclo(hashmaps):
    for hashmap in hashmaps:
        p = [hashmap[list(hashmap)[0]]]
        p.push(hashmap(0))
        while not p.isEmpty():
            n = p.pop()
            if n.visitado:
                return True
            else:
                for nodo in n.vecinos:
                    p.append(nodo)
    return False


class P2c:
    @staticmethod
    def main():
        n = int(input("numero de filas"))
        m = int(input("numero de columnas"))
        matriz = [None] * n
        for i in range(n):
            matriz[i] = [None] * m
        for i in range(n):
            s = input("Ingrese fila")
            for j in range(m):
                matriz[i][j] = s[j]
        hashmaps = setgrafo(matriz, n, m)
        decision = buscarCiclo(hashmaps)
        print(decision)


asd = P2c()
if __name__ == '__main__':
    asd.main()
