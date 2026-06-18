from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

class Janela2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha Janela")
        # Largura, altura e posição da janela
        self.setGeometry(10,20,800,400)
        self.texto = QLabel("Clique no botão abaixo")
        self.botao = QPushButton("Clique aqui")
        # Para organizar os controles(label, pushbutton), usaremos o comando
        # QVBoxLayout, para distribuit os controles de forma vertical da tela
        layout_vertical = QVBoxLayout()    # Determina as posições de cada objeto
        layout_vertical.addWidget(self.texto) 
        layout_vertical.addWidget(self.botao)
        # Adicionar o layout verical a tela
        self.setLayout(layout_vertical) 


app = QApplication(sys.argv)
tela = Janela2()
tela.show()
app.exec()
        