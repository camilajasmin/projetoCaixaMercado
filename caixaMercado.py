import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap

class CaixaMercado(QWidget):
    def __init__(self):

        # Variáveis globais
        self.total = 0.0
        self.linha = 0

        super().__init__()
        self.setGeometry(0,25,1590,840)
        self.setWindowTitle("Caixa Mercado")
        
        layoutCabecalho  = QHBoxLayout()
        layoutDireita    = QVBoxLayout()
        layoutDireita.addStretch(1)
        layoutDireita.setSpacing(0)
        layoutEsquerda   = QVBoxLayout()
        layoutImgDados   = QHBoxLayout()
        layoutDadosProd  = QVBoxLayout()
        layoutDadosProd.setSpacing(0)
        layoutLegenda    = QVBoxLayout()

        layoutRecebidoTroco   = QHBoxLayout()
        layoutRecebidoTroco.setSpacing(0)
        layoutRecebido        = QVBoxLayout()
        layoutRecebido.setSpacing(0)
        layoutTroco           = QVBoxLayout()
        layoutTroco.setSpacing(0)

        layoutTelaHor    = QHBoxLayout()
        layoutTelaHor.setSpacing(0)
        layoutTelaVer    = QVBoxLayout()  

        # Labels para organização
        labelTela           = QLabel()
        labelTela.setStyleSheet("QLabel{background-color:#659CE2}")
        labelDadosProdutos  = QLabel()
        labelDadosProdutos.setFixedWidth(400)
        labelDadosProdutos.setFixedHeight(525)
        labelDadosProdutos.setStyleSheet("QLabel{margin-right:30px;background-color:#B0C4DE}")
        labelImgDados       = QLabel()
        labelImgDados.setStyleSheet("QLabel{background-color:#B0C4DE}")
        labelRecebidoTroco = QLabel()
        labelRecebidoTroco.setStyleSheet("QLabel{background-color:#B0C4DE;margin-right:49px}")
        labelRecebidoTroco.setFixedHeight(125)
        labelRecebido_      = QLabel()
        labelTroco_         = QLabel()
        labelHorLegenda     = QLabel()
        labelHorLegenda.setStyleSheet("QLabel{background-color:white}")
        labelHorLegenda.setFixedHeight(150)

        ##

        labelCabecalho = QLabel("CAIXA ABERTO!")
        labelCabecalho.setStyleSheet("QLabel{color:white;background-color:#4682B4;font-size:40px}")
        labelCabecalho.setFixedHeight(70)

        labelEsquerda  = QLabel()
        labelEsquerda.setFixedWidth(700)
        labelEsquerda.setStyleSheet("QLabel{background-color:#B0C4DE}")

        labelDireita   = QLabel()
        labelDireita.setFixedWidth(900)
        labelDireita.setStyleSheet("QLabel{background-color:#B0C4DE}")

        # informações do produto
        labelCodProduto  = QLabel("Código do Produto")
        labelCodProduto.setStyleSheet("QLabel{color:white;font-size:25px;background-color:#21426C; border-radius:5px}")
        self.codProdutoEdit   = QLineEdit("")
        self.codProdutoEdit.setStyleSheet("QLineEdit{font-size:40px;margin-right:30px;border:2px white; margin-bottom: 5px; border-radius:5px}")

        labelNomeProduto = QLabel("Nome do Produto")
        labelNomeProduto.setStyleSheet("QLabel{color:white;font-size:25px;background-color:#21426C; border-radius:5px}")
        self.nomeProdutoEdit  = QLineEdit("")
        self.nomeProdutoEdit.setStyleSheet("QLineEdit{font-size:35px;margin-right:30px;border:2px white;margin-bottom: 5px; border-radius:5px}")

        labelValorUn = QLabel("Valor Unitário")
        labelValorUn.setStyleSheet("QLabel{color:white;font-size:25px;background-color:#21426C;margin-right:30px; border-radius:5px}")
        self.valorUnEdit  = QLineEdit("")
        self.valorUnEdit.setStyleSheet("QLineEdit{font-size:35px;margin-right:30px;border:2px white;margin-bottom: 5px; border-radius:5px}")

        labelQuantidade= QLabel("Quantidade")
        labelQuantidade.setStyleSheet("QLabel{color:white;font-size:25px;background-color:#21426C;margin-right:30px; border-radius:5px}")
        self.qtdEdit  = QLineEdit("")
        self.qtdEdit.setStyleSheet("QLineEdit{font-size:35px;margin-right:30px;border:2px white;margin-bottom: 5px; border-radius:5px}")

        labelSubtotal = QLabel("Subtotal do item")
        labelSubtotal.setStyleSheet("QLabel{color:white;font-size:30px;background-color:#21426C;margin-right:30px; border-radius:5px}")
        self.subtotalEdit  = QLineEdit("0,0")
        self.subtotalEdit.setEnabled(False)
        self.subtotalEdit.setStyleSheet("QLineEdit{font-size:45px;margin-right:30px;border:2px white;margin-bottom: 5px; border-radius:5px}")

        # Área de pagamento
        labelTotal = QLabel("TOTAL")
        labelTotal.setStyleSheet("QLabel{color:white;font-size:50px;background-color:#21426C;margin-right:49px; border-radius:5px}")
        labelTotal.setFixedHeight(50)
        self.totalEdit  = QLineEdit("0,0")
        self.totalEdit.setStyleSheet("QLineEdit{font-size:55px;margin-right:49px; border-radius:5px}")
        self.totalEdit.setEnabled(False)

        labelRecebido = QLabel("Valor Recebido")
        labelRecebido.setStyleSheet("QLabel{color:white;font-size:35px;background-color:#21426C; border-radius:5px}")
        labelRecebido.setFixedHeight(40)
        self.recebidoEdit  = QLineEdit("0,0")
        self.recebidoEdit.setStyleSheet("QLineEdit{font-size:45px; border-radius:5px}")

        labelTroco = QLabel("Troco")
        labelTroco.setStyleSheet("QLabel{color:white;font-size:35px;background-color:#21426C; border-radius:5px}")
        labelTroco.setFixedHeight(40)
        self.trocoEdit  = QLineEdit("0,0")
        self.trocoEdit.setStyleSheet("QLineEdit{font-size:45px; border-radius:5px}")
        self.trocoEdit.setEnabled(False)

        # logo do Mercado
        labelLogo = QLabel()
        labelLogo.setPixmap(QPixmap("logoMercado.png"))
        labelLogo.setScaledContents(True)
        labelLogo.setFixedHeight(500)

        # Área de legenda dos comandos
        labelF1   = QLabel("F1 - Soma Subtotal")
        labelF2   = QLabel("F2 - Adiciona na Tabela")
        labelF3   = QLabel("F3 - Calcula Troco")
        labelF4   = QLabel("F4 - Limpa a tela")
       
    
        # Tabela de Preços
        labelTabeladePrecos = QLabel("Lista de Produtos")
        labelTabeladePrecos.setStyleSheet("QLabel{font-size: 35px; color:white; background-color:#21426C; border-radius:5px; margin-right:46px}")
        # Criando a tabela de dados do lado direito
        self.tbResumo = QTableWidget()
        self.tbResumo.setColumnCount(5)
        self.tbResumo.setRowCount(15)
        self.tbResumo.setFixedHeight(400)
        self.tbResumo.setFixedWidth(830)

        # criando o cabecalho para a tabela resumo
        titulos = ["Código","Nome Produto","Quantidade","Preço Unitário","Preço Total"]
        self.tbResumo.setHorizontalHeaderLabels(titulos)


        ## labels e layouts ##
       
        #  Cabeçalho
        labelCabecalho.setLayout(layoutCabecalho)
        layoutTelaVer.addWidget(labelCabecalho)
        layoutTelaVer.addWidget(labelTela)

        # Layouts do lado esquerdo da tela
        labelEsquerda.setLayout(layoutEsquerda)
        layoutEsquerda.addWidget(labelImgDados)
        layoutEsquerda.addWidget(labelHorLegenda)

        # Layouts do lado direito da tela direita
        labelDireita.setLayout(layoutDireita)
        layoutDireita.addWidget(labelTabeladePrecos)
        layoutDireita.addWidget(self.tbResumo)
        layoutDireita.addWidget(labelTotal)
        layoutDireita.addWidget(self.totalEdit)
        layoutDireita.addWidget(labelRecebidoTroco)


        # Layout da tela horizontal 
        layoutTelaHor.addWidget(labelEsquerda)
        layoutTelaHor.addWidget(labelDireita)
        labelTela.setLayout(layoutTelaHor)
        
        # Layout dos dados do produto (vertical)
        layoutDadosProd.addWidget(labelCodProduto)
        layoutDadosProd.addWidget(self.codProdutoEdit)
        layoutDadosProd.addWidget(labelNomeProduto)
        layoutDadosProd.addWidget(self.nomeProdutoEdit)
        layoutDadosProd.addWidget(labelValorUn)
        layoutDadosProd.addWidget(self.valorUnEdit)
        layoutDadosProd.addWidget(labelQuantidade)
        layoutDadosProd.addWidget(self.qtdEdit)
        layoutDadosProd.addWidget(labelSubtotal)
        layoutDadosProd.addWidget(self.subtotalEdit)

        
        labelDadosProdutos.setLayout(layoutDadosProd)
        


        ##
        labelRecebidoTroco.setLayout(layoutRecebidoTroco)

        layoutRecebidoTroco.addWidget(labelRecebido_)
        layoutRecebidoTroco.addWidget(labelTroco_)

        # Label do valor recebido 
        labelRecebido_.setLayout(layoutRecebido)

        layoutRecebido.addWidget(labelRecebido)
        layoutRecebido.addWidget(self.recebidoEdit)

        # Label do Valor do Troco
        labelTroco_.setLayout(layoutTroco)

        layoutTroco.addWidget(labelTroco)
        layoutTroco.addWidget(self.trocoEdit)


        # Label das informações do produto e da imagem (horizontal) 
        layoutImgDados.addWidget(labelLogo)
        layoutImgDados.addWidget(labelDadosProdutos)
        labelImgDados.setLayout(layoutImgDados)

        # Label da legenda
        labelHorLegenda.setLayout(layoutLegenda) 
        layoutLegenda.addWidget(labelF1)
        layoutLegenda.addWidget(labelF2)
        layoutLegenda.addWidget(labelF3)
        layoutLegenda.addWidget(labelF4)

        #Tela Inteira
        self.setLayout(layoutTelaVer)

        # Ações 
        self.keyPressEvent = self.keyPressEvent

    def keyPressEvent(self, e):

        print("event", e)

        ## Adicionando itens na tabela(F2)
        
        if (e.key() == Qt.Key_F2):   

            print(' Você teclou F2')

            self.tbResumo.setItem(self.linha,0,QTableWidgetItem(str(self.codProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,1,QTableWidgetItem(str(self.nomeProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,2,QTableWidgetItem(str(self.qtdEdit.text())))
            self.tbResumo.setItem(self.linha,3,QTableWidgetItem(str(self.valorUnEdit.text())))
            self.tbResumo.setItem(self.linha,4,QTableWidgetItem(str(self.subtotalEdit.text())))
            self.linha+=1
            
            self.total+=float(self.subtotalEdit.text())
            self.totalEdit.setText(str(self.total))

            # Limpando os LineEdit

            self.codProdutoEdit.setText("")
            self.nomeProdutoEdit.setText("")
            self.qtdEdit.setText("")
            self.valorUnEdit.setText("")
            self.subtotalEdit.setText("0,00")
        
        ## Calculando Subtotal (F1)
        elif(e.key() == Qt.Key_F1):
            qtd = self.qtdEdit.text()
            prc = self.valorUnEdit.text()
            result = float(qtd)*float(prc)
            self.subtotalEdit.setText(str(result))
        
        ## Calculando o Troco(f3)
        elif(e.key() == Qt.Key_F3):
            totalPago = self.recebidoEdit.text()
            totalPagar = self.totalEdit.text()
            result = float(totalPago) - float(totalPagar)
            self.trocoEdit.setText(str(result))

        ## Limpando a tela (f4)
        elif(e.key() == Qt.Key_F4):

            self.tbResumo.clearContents()
            self.totalEdit.setText("0,00")
            self.recebidoEdit.setText("")
            self.trocoEdit.setText("0,00")
            self.subtotalEdit.setText("0,00")
        
app = QApplication(sys.argv)
janela = CaixaMercado()
janela.show()
app.exec_()