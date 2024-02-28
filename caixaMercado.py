import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap

class CaixaMercado(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,25,1590,840)
        self.setWindowTitle("Caixa Mercado")
        
        layoutCabecalho  = QHBoxLayout()
        layoutDireita    = QVBoxLayout()
        layoutEsquerda   = QVBoxLayout()
        layoutImgDados   = QHBoxLayout()
        layoutDadosProd  = QVBoxLayout()
        layoutLegenda    = QHBoxLayout()

        layoutTbValores  = QVBoxLayout()
        layoutTtlTroco   = QHBoxLayout()

        layoutTelaHor    = QHBoxLayout()
        layoutTelaVer    = QVBoxLayout()  

        labelCabecalho = QLabel("CAIXA ABERTO!")
        labelCabecalho.setStyleSheet("QLabel{color:white;background-color:#836FFF;font-size:40px}")
        labelCabecalho.setFixedHeight(100)

        labelEsquerda  = QLabel()
        labelEsquerda.setFixedWidth(800)
        labelEsquerda.styleSheet("QLabel{background-color:}")

        # 
        labelCabecalho.setLayout(layoutCabecalho)
        layoutTelaVer.addWidget(labelCabecalho)
        #Tela Inteira
        self.setLayout(layoutTelaVer)
        




app = QApplication(sys.argv)
janela = CaixaMercado()
janela.show()
app.exec_()