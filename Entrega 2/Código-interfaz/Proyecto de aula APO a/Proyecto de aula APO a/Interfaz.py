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
        uic.loadUi("gui/PruebaPaginaPrincipal.ui", self)
        self.setFixedSize(self.size())
        self.appfinanciera= perfil(nombre="a", profesion="b", edad= 10000)        
        self.__configurar()
        self.__cargar_datos()
        self.abrir_dialogo_solicitar_prestamo= DialogoSolicitarPrestamo()

    def __configurar(self):
        #Configurar el QListView
        self.lv_prestamos_vigentes.setModel(QStandardItemModel())

        #Enlazar eventos de los botones
        self.pb_cliente.clicked.connect(self.abrir_dialogo_solicitar_prestamo)



    def __cargar_datos(self):
        prestamos = list(self.appfinanciera.values())
        for prestamo in prestamos:
            item = QStandardItem(str(prestamo)) # (David Riv) profesion - 19
            item.prestamo = prestamo
            item.setEditable(False)
            self.lv_prestamos_vigentes.model().appendRow(item)

    def abrir_dialogo_solicitar_prestamo(self):
        resp = self.abrir_dialogo_solicitar_prestamo.exec()
        if resp == QDialog.accepted:
            nombre = self.abrir_dialogo_solicitar_prestamo.le_nombre.text()
            edad = int(self.abrir_dialogo_solicitar_prestamo.le_edad.text())
            cantidad = float(self.abrir_dialogo_solicitar_prestamo.le_cantidad.text())



#app.py
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindowPruebaPaginaPrincipal()
    win.show()
    sys.exit(app.exec_())



class DialogoSolicitarPrestamo(QDialog):
    
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/DialogoSolicitarPrestamo.ui", self)

        #Asignar tamaño original
        self.setFixedSize(self.size())


    