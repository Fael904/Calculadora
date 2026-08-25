from operacao import Operacao

class Multiplicacao(Operacao):
    simbolo = "x"
    nome = "Multiplicar"

    def calcular(self):
        return self.a * self.b