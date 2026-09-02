import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLayout,
    QLineEdit,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from soma import Soma
from subtracao import Subtracao
from divisao import Divisao
from multiplicacao import Multiplicacao
from potenciacao import Potenciacao

class Calculadora(QWidget):
    def __init__(self):
        self.setWindowTitle("Calculadora")
        selfESTILO = """
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