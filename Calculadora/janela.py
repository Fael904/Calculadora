import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
)

from soma import Soma
from subtracao import Subtracao
from divisao import Divisao
from multiplicacao import Multiplicacao

OPERADORES = {"+", "-", "*", "/"}


ESTILO = """
QWidget {
    background-color: #f2f2f2;
    font-family: Segoe UI, Arial;
}
QLabel#visor {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #222222;
    font-size: 28px;
    padding: 12px;
}
QLabel#conta {
    color: #777777;
    font-size: 13px;
    padding-left: 4px;
}
QPushButton {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #222222;
    font-size: 18px;
    min-width: 56px;
    min-height: 48px;
}
QPushButton:hover {
    background-color: #e8e8e8;
}
QPushButton:pressed {
    background-color: #dcdcdc;
}
"""


class Calculadora(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora")
        self.setFixedSize(350, 500)

        self.digitado = "0"
        self.primeiro = None
        self.classe = None
        self.zerar = False

        self.conta = QLabel("")
        self.conta.setObjectName("conta")
        self.conta.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.visor = QLabel(self.digitado)
        self.visor.setObjectName("visor")
        self.visor.setAlignment(Qt.AlignmentFlag.AlignRight)

        grade = QGridLayout()

        botoes = [
            ("C", 0, 0),
            ("<", 0, 1),
            ("+/-", 0, 2),
            ("/", 0, 3),

            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("*", 1, 3),

            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("-", 2, 3),

            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("+", 3, 3),

            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
        ]

        for texto, linha, coluna in botoes:
            botao = QPushButton(texto)
            largura = 2 if texto == "=" else 1
            grade.addWidget(botao, linha, coluna, 1, largura)
            botao.clicked.connect(self.criar_acao(texto))

        layout = QVBoxLayout()
        layout.addWidget(self.conta)
        layout.addWidget(self.visor)
        layout.addLayout(grade)

        self.setLayout(layout)

    def criar_acao(self, texto):
        def acao():
            self.clicar(texto)
        return acao

    def clicar(self, texto):
        if texto == "0" or texto == "1" or texto == "2" or texto == "3" or texto == "4" or texto == "5" or texto == "6" or texto == "7" or texto == "8" or texto == "9" or texto == ".":
            self.digitar(texto)
        elif texto == "+" or texto == "-" or texto == "*" or texto == "/":
            self.escolher_operacao(texto)
        elif texto == "=":
            self.calcular()
        elif texto == "C":
            self.limpar()
        elif texto == "<":
            if len(self.digitado) > 1:
                self.digitado = self.digitado[:-1]
            else:
                self.digitado = "0"
            self.visor.setText(self.digitado)
        elif texto == "+/-":
            if self.digitado != "0":
                if self.digitado.startswith("-"):
                    self.digitado = self.digitado[1:]
                else:
                    self.digitado = "-" + self.digitado
                self.visor.setText(self.digitado)

    def digitar(self, tecla):
        if self.zerar == True:
            self.digitado = "0"
            self.zerar = False

        if tecla == "." and "." in self.digitado:
            return

        if self.digitado == "0" and tecla != ".":
            self.digitado = tecla
        else:
            self.digitado = self.digitado + tecla

        self.visor.setText(self.digitado)

    def valor_do_visor(self):
        return float(self.digitado)

    def mostrar(self, numero):
        self.digitado = f"{numero:g}"
        self.visor.setText(self.digitado)

    def escolher_operacao(self, simbolo):
        if self.primeiro is not None:
            if self.zerar == False:
                self.calcular()

        self.primeiro = self.valor_do_visor()

        if simbolo == "+":
            self.classe = Soma
        elif simbolo == "-":
            self.classe = Subtracao
        elif simbolo == "*":
            self.classe = Multiplicacao
        elif simbolo == "/":
            self.classe = Divisao

        self.conta.setText(f"{self.digitado} {simbolo}")
        self.zerar = True

    def calcular(self):
        if self.primeiro is None:
            return
        if self.classe is None:
            return

        segundo = self.valor_do_visor()

        try:
            conta = self.classe(self.primeiro, segundo)
            resultado = conta.calcular()
        except ZeroDivisionError:
            self.digitado = "Não é possível dividir por Zero"
            self.visor.setText(self.digitado)
            self.conta.setText("")
            self.primeiro = None
            self.classe = None
            self.zerar = True
            return

        self.conta.setText(f"{self.conta.text()} {segundo:g} =")
        self.mostrar(resultado)
        self.primeiro = None
        self.classe = None
        self.zerar = True

    def limpar(self):
        self.digitado == "0"
        self.primeiro = None
        self.classe = None
        self.zerar = False
        self.visor.setText(self.digitado)
        self.conta.setText("")


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(ESTILO)

    janela = Calculadora()
    janela.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()