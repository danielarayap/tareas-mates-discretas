from matplotlib import pyplot


def prob_no_repet(n):
    p1 = 1.0
    res = 1.0
    for i in range(2, n + 1):
        res = p1 * ((366 - i) / 365)
        p1 = res
    return res


def prob_repet(n):
    return 1 - prob_no_repet(n)


# Valores del eje X que toma el gráfico.
x = range(0, 101)
# Graficar ambas funciones.
pyplot.plot(x, [prob_repet(i) for i in x])
# Éstas son las funciones constantes
pyplot.plot(x, [0.25 for i in x])
pyplot.plot(x, [0.5 for i in x])
pyplot.plot(x, [0.75 for i in x])
pyplot.plot(x, [0.9 for i in x])
# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(0, 100)
pyplot.ylim(0, 1.2)
# nombrar ejes
pyplot.xlabel('n° de personas (n)')
pyplot.ylabel('probabilidad (P(n))')
# grilla
pyplot.grid(color='0.5', linestyle='--', axis='both')
pyplot.savefig("grafico.png")  # Guardar gráfico como imágen PNG.
# Mostrarlo.
pyplot.show()
