import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *




class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Esto determina las dimensiones de la ventana:
        self.resize(720, 600)

        # Aquí cargamos lo que denominamos "señales"
        # Conectamos señales (izq) a slots (derecha)



        # Esto determina el título de la ventana
        self.setWindowTitle("Este es el título de la ventana")

        # Aquí ponemos los Widgets que queramos
        label1 = QLabel("ToolBar") 
        label1.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label1) # Esto lo necesitamos para el slot de button_lexer


        #Creación del Toolbar
        toolbar = QToolBar("Mi primer toolbar")
        toolbar.setIconSize(QSize(64, 64))
        self.addToolBar(toolbar)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # Acciones del toolbar
        button_lexer = QAction(QIcon("LexerIcon.png"), "Analizador léxico", self)
        button_lexer.setStatusTip("Lex") # Esto es el estado que se va a mostrar en la barra de estados que haremos luego
        button_lexer.triggered.connect(lambda x: self.onMyToolbarButtonLexico(x, label = label1))
        toolbar.addAction(button_lexer) # Esto añade el botón del lexer

        toolbar.addSeparator() #Separa los íconos

        button_syntax = QAction(QIcon("Syntax.png"), "Analizador sintáctico", self)
        button_syntax.setStatusTip("Syntax") # Esto es el estado que se va a mostrar en la barra de estados que haremos luego
        button_syntax.triggered.connect(lambda x: self.onMyToolbarButtonSyntax(x, label = label1))
        toolbar.addAction(button_syntax) # Esto añade el botón del lexer




        #Text Area Input
        self.textArea = QPlainTextEdit(self)
        self.textArea.move(0,95)
        self.textArea.resize(360,480)

        # Text Area Output
        self.textArea = QPlainTextEdit(self)
        self.textArea.insertPlainText("Aquí sale tu resultado!\n")
        self.textArea.move(360,95)
        self.textArea.resize(360,480)
        self.textArea.setReadOnly(True)

        # Añadir más widgets
        # toolbar.addWidget(QLabel("FIN?"))


        # Checkable true al inicio
        button_lexer.setCheckable(True)
        button_syntax.setCheckable(True)



        # Creamos la barra de estado
        self.setStatusBar(QStatusBar(self))



    # Aquí definimos los comportanmientos (slots) que utilizamos en la sección se signals

    # El slot del lexer
    def onMyToolbarButtonLexico(self, s, label):
        print("Se activa el slot del lexer ",s )
        label.setText("Tokenizar finalizado")

    def onMyToolbarButtonSyntax(self, s, label):
        print("Se activa el slot del syntax ",s )
        label.setText("Sintaxis finalizada")

    def onWindowTitleChange(self, s):
        print(s)


    def contextMenuEvent(self, event):
        print("Has dado click derecho", event)


# Aquí ha terminado la clase que definimos

# Aquí pasamos a instanciar la apliación (nota el nivel de sangría)
app = QApplication(sys.argv)



# Aquí instanciamos window y hacemos que se muestre. Corremos la app
window = MainWindow()
window.show()
app.exec_()


print("Ha terminado la app")