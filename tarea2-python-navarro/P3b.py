from numpy import *


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def coef_binomial(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def prob_ganar(p, k, n):
    Pr = 0
    q = 1 - p
    while n <= k:
        Pr += ((coef_binomial(k, n)) * (p ** n) * (q ** (k - n)))  # Pr(X>=n)=1-(Pr(X=0)+Pr(X=1)+...+Pr(X=n-1) o
        #                                                                    =Pr(X=n)+Pr(X=n+1)+...Pr(X=k)
        n += 1
    return Pr


print(prob_ganar(0.15, 100, 4))  # ejemplo
