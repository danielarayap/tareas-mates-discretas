import random


def elegir_numero(lista):  # funcion que elige un valor de la lista al azar
    indice = 0
    valores = str.split(lista, ",")  # divide todos los valores que esten separados por una coma
    for i, number in enumerate(valores[1:]):  # este ciclo recorre todos los numeros en el arreglo
        if random.randint(0, i) == i:  # y para cada i lo compara con un random entre 0 e i, si son iguales
            indice = i  # indice toma el valor de ese i temporalmente mientras no aparezca otro valor que coincida
    return valores[indice]  # azarosamente con el random entre 0 y éste


print(elegir_numero("1,2,3,4,5,6,7,8,9,10,11"))
