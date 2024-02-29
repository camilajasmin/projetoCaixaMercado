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

        layoutRecebidoTroco   = QHBoxLayout()
        layoutRecebido        = QVBoxLayout()
        layoutTroco        = QVBoxLayout()

        layoutTelaHor    = QHBoxLayout()
        layoutTelaVer    = QVBoxLayout()  

        # Labels para organização
        labelTela           = QLabel()
        labelDadosProdutos  = QLabel()
        labelDadosProdutos.setFixedWidth(400)
        labelDadosProdutos.setFixedHeight(500)
        labelImgDados       = QLabel()
        labelImgDados.setStyleSheet("QLabel{background-color:#FFC0CB}")
        labelRecebidoTroco = QLabel()
        labelRecebido      = QLabel()
        labelTroco         = QLabel()
        ##

        labelCabecalho = QLabel("CAIXA ABERTO!")
        labelCabecalho.setStyleSheet("QLabel{color:white;background-color:#4682B4;font-size:40px}")
        labelCabecalho.setFixedHeight(100)

        labelEsquerda  = QLabel()
        labelEsquerda.setFixedWidth(700)
        labelEsquerda.setStyleSheet("QLabel{background-color:#ADD8E6;margin-left:0px}")

        labelDireita   = QLabel()
        labelDireita.setFixedWidth(900)
        labelDireita.setStyleSheet("QLabel{background-color:#B0C4DE}")

        # informações do produto
        labelCodProduto  = QLabel("Código do Produto")
        labelCodProduto.setStyleSheet("QLabel{font-size:25px;background-color:white}")
        codProdutoEdit   = QLineEdit("0,0")
        codProdutoEdit.setStyleSheet("QLineEdit{font-size:35px}")

        labelNomeProduto = QLabel("Nome do Produto")
        labelNomeProduto.setStyleSheet("QLabel{font-size:25px;background-color:white}")
        nomeProdutoEdit  = QLineEdit("0,0")
        nomeProdutoEdit.setStyleSheet("QLineEdit{font-size:35px}")

        labelValorUn = QLabel("Valor Unitário")
        labelValorUn.setStyleSheet("QLabel{font-size:25px;background-color:white}")
        valorUnEdit  = QLineEdit("0,0")
        valorUnEdit.setStyleSheet("QLineEdit{font-size:35px}")

        labelQuantidade= QLabel("Quantidade")
        labelQuantidade.setStyleSheet("QLabel{font-size:25px;background-color:white}")
        qtdEdit  = QLineEdit("0,0")
        qtdEdit.setStyleSheet("QLineEdit{font-size:35px}")

        labelSubtotal = QLabel("Subtotal do item")
        labelSubtotal.setStyleSheet("QLabel{font-size:30px;background-color:white}")
        subtotalEdit  = QLineEdit("0,0")
        subtotalEdit.setStyleSheet("QLineEdit{font-size:45px}")

        # Área de pagamento
        labelTotal = QLabel("TOTAL")
        labelTotal.setStyleSheet("QLabel{font-size:45px;background-color:white}")
        totalEdit  = QLineEdit("0,0")
        totalEdit.setStyleSheet("QLineEdit{font-size:55px}")

        labelRecebido = QLabel("Valor Recebido")
        labelRecebido.setStyleSheet("QLabel{font-size:25px;background-color:white}")
        recebidoEdit  = QLineEdit("0,0")
        recebidoEdit.setStyleSheet("QLineEdit{font-size:35px}")

        labelTroco = QLabel("Troco")
        labelTroco.setStyleSheet("QLabel{font-size:25px;background-color:white}")
        trocoEdit  = QLineEdit("0,0")
        trocoEdit.setStyleSheet("QLineEdit{font-size:35px}")

        # logo do Mercado
        labelLogo = QLabel()
        labelLogo.setPixmap(QPixmap("logoMercado.png"))
        labelLogo.setScaledContents(True)
        labelLogo.setFixedHeight(500)

        # Área de legenda dos comandos
        # Tabela de Preços
        # Criando a tabela de dados do lado direito
        tbResumo = QTableWidget()
        tbResumo.setColumnCount(5)
        tbResumo.setRowCount(10)
        # tbResumo.setStyleSheet("QTableWidget{}")
        # tbResumo.setGeometry(50, 50, 50, 50)

        # criando o cabecalho para a tabela resumo
        titulos = ["Código","Nome Produto","Quantidade","Preço Unitário","Preço Total"]
        tbResumo.setHorizontalHeaderLabels(titulos)

        # Totalizando o valor da compra
        # Valor recebido pelo cliente
        # Calculando o valor do troco

        ## labels e layouts ##
       
        #  Cabeçalho
        labelCabecalho.setLayout(layoutCabecalho)
        layoutTelaVer.addWidget(labelCabecalho)
        layoutTelaVer.addWidget(labelTela)

        # Layouts do lado esquerdo da tela
        labelEsquerda.setLayout(layoutEsquerda)
        layoutEsquerda.addWidget(labelImgDados)

        # Layouts do lado direito da tela direita
        labelDireita.setLayout(layoutDireita)
        layoutDireita.addWidget(tbResumo)
        layoutDireita.addWidget(labelTotal)
        layoutDireita.addWidget(totalEdit)
        layoutDireita.addWidget(labelRecebidoTroco)
    
        # Layout da tela horizontal 
        layoutTelaHor.addWidget(labelEsquerda)
        layoutTelaHor.addWidget(labelDireita)
        labelTela.setLayout(layoutTelaHor)
        
        # Layout dos dados do produto (vertical)
        layoutDadosProd.addWidget(labelCodProduto)
        layoutDadosProd.addWidget(codProdutoEdit)
        layoutDadosProd.addWidget(labelNomeProduto)
        layoutDadosProd.addWidget(nomeProdutoEdit)
        layoutDadosProd.addWidget(labelValorUn)
        layoutDadosProd.addWidget(valorUnEdit)
        layoutDadosProd.addWidget(labelQuantidade)
        layoutDadosProd.addWidget(qtdEdit)
        layoutDadosProd.addWidget(labelSubtotal)
        layoutDadosProd.addWidget(subtotalEdit)

        
        labelDadosProdutos.setLayout(layoutDadosProd)
        


        ##
        layoutRecebidoTroco.addWidget(labelRecebido)
        layoutRecebidoTroco.addWidget(labelTroco)

        # Label do valor recebido 
        labelRecebido.setLayout(layoutRecebido)
        layoutRecebido.addWidget(labelRecebido)
        layoutRecebido.addWidget(recebidoEdit)

        # Label do Valor do Troco
        labelTroco.setLayout(layoutTroco)
        layoutTroco.addWidget(labelTroco)
        layoutTroco.addWidget(trocoEdit)


        # Label das informações do produto e da imagem (horizontal) 
        layoutImgDados.addWidget(labelLogo)
        layoutImgDados.addWidget(labelDadosProdutos)
        labelImgDados.setLayout(layoutImgDados)

        #Tela Inteira
        self.setLayout(layoutTelaVer)
        
app = QApplication(sys.argv)
janela = CaixaMercado()
janela.show()
app.exec_()