from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTableWidget, QVBoxLayout, QHBoxLayout, QTableWidgetItem
from PyQt6.QtGui import QPixmap,QIcon
from PyQt6.QtCore import Qt

from sys import argv 

class Cadastro(QWidget):
   def __init__(self):
        self.linha = 0
        self.valor_total = 0.0
        super().__init__()
        self.setWindowTitle("Cadastro do Usuário")
        self.setGeometry(150,50,1600,900)

        self.setWindowIcon(QIcon("pata2.png"))


# ===================================COR DE FUNDO===============================================================


        self.layout_horizontal = QHBoxLayout()
        
        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel{background-color:#FFAD2C}")

        self.label_col_esquerda = QLabel()
        self.label_col_esquerda.setStyleSheet("QLabel{background-color:#D4A43E}")
        self.label_col_direita.setFixedWidth(800)


# =======================================================================================


        self.layout_vert_col_esq = QVBoxLayout()

        self.label_logo = QLabel()
        self.label_logo.setPixmap(QPixmap("cachorro3.png"))
        self.label_logo.setScaledContents(True)

        self.layout_vert_col_esq.addWidget(self.label_logo)
        self.label_col_esquerda.setLayout(self.layout_vert_col_esq)


# =============================================INICÍO COLUNA DIREITA==============================================================
        

        self.layout_vert_col_dir = QVBoxLayout()

        self.label_titulo = QLabel("CADASTRO DE USUÁRIO")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_titulo.setStyleSheet("""QLabel {color: white; font-size: 40pt; font-weight: bold;}""")
        self.layout_vert_col_dir.addWidget(self.label_titulo)

        
        self.label_nome_conta = QLabel("Nome da conta")
        self.label_nome_conta.setStyleSheet("font-size: 24pt; font-weight: bold; color:#ffffff;")
        self.edit_nome_conta = QLineEdit()
        self.edit_nome_conta.setStyleSheet("QLineEdit{font-size:25pt}")
        self.edit_nome_conta.setFixedHeight(88)


        self.label_email_conta = QLabel("Email da conta")
        self.label_email_conta.setStyleSheet("font-size: 24pt; font-weight: bold; color:#ffffff;")
        self.edit_email_conta = QLineEdit()
        self.edit_email_conta.setStyleSheet("QLineEdit{font-size:25pt}")
        self.edit_email_conta.setFixedHeight(88)


        self.label_senha_conta = QLabel("Senha da conta")
        self.label_senha_conta.setStyleSheet("font-size: 24pt; font-weight: bold; color:#ffffff;")
        self.edit_senha_conta = QLineEdit()
        self.edit_senha_conta.setStyleSheet("QLineEdit{font-size:25pt}")
        self.edit_senha_conta.setFixedHeight(88)


# ==============================================================================================================


        self.layout_vert_col_dir.addWidget(self.label_nome_conta)
        self.layout_vert_col_dir.addWidget(self.edit_nome_conta)

        self.layout_vert_col_dir.addWidget(self.label_email_conta)
        self.layout_vert_col_dir.addWidget(self.edit_email_conta)
        
        self.layout_vert_col_dir.addWidget(self.label_senha_conta)
        self.layout_vert_col_dir.addWidget(self.edit_senha_conta)

        
        self.label_col_direita.setLayout(self.layout_vert_col_dir)


# ===============================================FIM COLUNA DIREITA========================================================


        self.layout_horizontal.addWidget(self.label_col_esquerda)
        self.layout_horizontal.addWidget(self.label_col_direita)


        self.setLayout(self.layout_horizontal)


        self.edit_nome_conta.setText("")
        self.edit_email_conta.setText("")
        self.edit_senha_conta.setText("")
       


app = QApplication(argv)
janela = Cadastro()
janela.show()
app.exec()