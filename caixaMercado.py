import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap

class CaixaMercado(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,25,1590,840)
        self.setWindowTitle("Caixa Mercado")

        verticalEsquerda = QVBoxLayout()
        verticalDireita = QVBoxLayout()




app = QApplication(sys.argv)
janela = CaixaMercado()
janela.show()
app.exec_()