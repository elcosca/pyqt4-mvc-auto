# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys
sys.path.append('../Controladores')
from main_controller import *


class MainWindows(QtGui.QWidget):

    def __init__(self):
        super(MainWindows, self).__init__()
        self.controlador = MainControlador(self)
        self.init_ui()

    def init_ui(self):
        self.label = QtGui.QLabel('Cantidad de personas')
        h_layout = QtGui.QHBoxLayout()
        h_layout.addWidget(self.label)
        button_subir = QtGui.QPushButton('Subir persona')
        button_subirmuchas = QtGui.QPushButton('Subir muchas personas')
        button_bajar = QtGui.QPushButton('Bajar persona')
        button_bajarmuchas = QtGui.QPushButton('Bajar muchas personas')
        button_subir_varias = QtGui.QPushButton('Subir estas Personas')
        button_bajar_varias = QtGui.QPushButton('Bajar estas Personas')
        h_layout.addWidget(button_subir)
        h_layout.addWidget(button_subirmuchas)
        h_layout.addWidget(button_bajar)
        h_layout.addWidget(button_bajarmuchas)
        h_layout.addWidget(button_subir_varias)
        h_layout.addWidget(button_bajar_varias)


        self.ingreso_numero = QtGui.QLineEdit(self)



        button_subir.clicked.connect(self.controlador.handler_subir_persona)
        button_subirmuchas.clicked.connect(self.controlador.handler_subir_muchas_personas)
        button_bajar.clicked.connect(self.controlador.handler_bajar_persona)
        button_bajarmuchas.clicked.connect(self.controlador.handler_bajar_muchas_personas)
        button_subir_varias.clicked.connect(self.controlador.handler_subir_varias_personas)
        button_bajar_varias.clicked.connect(self.controlador.handler_bajar_varias_personas)

        self.setLayout(h_layout)
        self.setWindowTitle('Proyecto del auto')
        self.setGeometry(200, 200, 200, 200)
        self.show()

app = QtGui.QApplication(sys.argv)
windows = MainWindows()
sys.exit(app.exec_())
