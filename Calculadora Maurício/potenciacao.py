from operacao import Operacao

class Potenciacao(Operacao):
    simbolo = "elevado á"
    nome = "Ponteciação"

    def calcular(self):
        return self.a ** self.b