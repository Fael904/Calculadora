from operacao import Operacao

class Subtracao(Operacao):
    simbolo = "-"
    nome = "Subtrair"

    def calcular(self):
        return self.a - self.b