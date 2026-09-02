from operacao import Operacao

class Divisao(Operacao):
    simbolo = ":"
    nome = "Dividir"

    def calcular(self):
        if self.b == 0:
            raise ValueError("Não é possível dividir por zero na matemática!!!!")
        return self.a / self.b