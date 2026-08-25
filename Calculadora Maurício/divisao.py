from operacao import Operacao

class Divisao(Operacao):
    simbolo = ":"
    nome = "Dividir"

    def calcular(self):
        return self.a / self.b