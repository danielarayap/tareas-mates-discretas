class Hanoi:
    def run(self, n):
        self.Q(n, "A", "B", "C")  # la funcion run implementa el juego de Hanoi con n discos

    def Q(self, n, source, target, temp):  # funcion Q del comportamiento de Hanoi
        if n == 0:
            return  # caso base
        self.R(n - 1, source, temp, target)  # para definir Q en este programa se utilizó la expresión encontrada
        print(source + "->" + target)  # encontrada en la parte a) 2R(n-1) + 1, donde 1 corresponde a la instrucción
        self.R(n - 1, temp, target, source)  # print(source + "->" + target)

    def R(self, n, source, target, temp):
        if n == 0:  # caso base
            return
        self.R(n - 1, source, target, temp)  # de la misma forma que en Q, R se definió a partir de la parte a)
        print(source + "->" + temp)  # Rn=2R(n-1)+ 1+Q(n-1)+1=Qn+Q(n-1)+1
        self.Q(n - 1, target, source, temp)
        print(temp + "->" + target)
        self.R(n - 1, source, target, temp)

    def main(self):
        self.run(2)


h = Hanoi()
if __name__ == '__main__':
    h.main()
