from numpy import random

from P1b import prob_repet

m = int(input('Ingrese n° de simulaciones (m) :'))
n = int(input('Ingrese n° de personas (n) :'))
print(prob_repet(n))
result = 0
cumples = []
for j in range(0, m):
    i = 0
    while i < n:
        cumples.append(random.randint(1, 366))
        i += 1
    cumples = list(set(cumples))
    if len(cumples) < n:
        result += 1
    del cumples[:]
print(result / m, "probabilidad de que se repita un cumpleaños")

