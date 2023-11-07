import sys
from typing import Self
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from nuevo_usuario_copy import nuevo_usuario
from clase_perfil_copy import perfil
from propietario_copy import propietario
from Excepciones import mora




class MainWindowPruebaPaginaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("gui/MainWindowproyectoAPO.ui", self)
        self.setFixedSize(self.size())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindowPruebaPaginaPrincipal()
    win.show()
    sys.exit(app.exec_())

        