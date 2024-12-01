import sys 
from PyQt5 import QtCore 
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QPropertyAnimation 
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget,QDesktopWidget
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QAbstractItemView
from Controlador.ArregloProveedor import *
aProveedor=ArregloProveedor()
class VentanaRegistroProveedores(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaRegistroProveedores,self).__init__(parent)
        loadUi("UI/REGISTRO-PROVEEDORES.ui",self)
        self.editar=False
        self.btnCancelar.setVisible(False)
        self.btnCerrar.clicked.connect(self.cerrarVentana)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.tblProvedores.cellDoubleClicked.connect(self.cargarDatos)
        self.btnInsertar.clicked.connect(self.insertar)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.tblProvedores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listar()
    
    def limpiarTabla(self):
        self.tblProvedores.clearContents()
        self.tblProvedores.setRowCount(0) 

    def validacion(self):
        if len(self.txtRuc.text().strip()) != 11 or self.txtRuc.text().isdigit()==False:
            self.txtRuc.setFocus()
            return "Ingrese correctamente el RUC"
        elif self.txtNombre.text().strip() == "":
            self.txtNombre.setFocus()
            return "!!Ingrese un Nombre!!"
        elif self.txtRazSocial.text().strip() == "":
            self.txtRazSocial.setFocus()
            return "!!Ingrese la Razon Social!!"
        elif self.txtDireccion.text().strip() == "":
            self.txtDireccion.setFocus()
            return "!!Ingrese una Direccion!!"
        elif len(self.txtTelefono.text().strip()) != 9 or self.txtTelefono.text().isdigit()==False:
            self.txtTelefono.setFocus()
            return "Ingrese correctamente el numero Celular"
        else:
            return 0
        
    def reiniciar(self):
        self.btnCancelar.setVisible(False)
        self.btnInsertar.setText("Insertar")
        self.txtRuc.setEnabled(True)
        self.editar=False
        self.txtRuc.clear()
        self.txtNombre.clear()
        self.txtRazSocial.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()
    
    def listar(self):
        self.tblProvedores.setRowCount(len(aProveedor.listar()))
        self.tblProvedores.setColumnCount(5)
        self.tblProvedores.verticalHeader().setVisible(False)
        lista=aProveedor.listar()
        for fila, Proveedor in enumerate(lista):
            for columna, valor in enumerate(Proveedor):
                item = QTableWidgetItem(str(valor))
                self.tblProvedores.setItem(fila, columna, item)

    def insertar(self):
        if (self.editar):
            if self.validacion()== 0 :
                objProveedor= Proveedor(self.txtRuc.text().strip(),
                                    self.txtNombre.text().strip(),
                                    self.txtRazSocial.text().strip(),
                                    self.txtDireccion.text().strip(),
                                    self.txtTelefono.text().strip())
                
                try:
                    aProveedor.modificar(objProveedor)
                    self.reiniciar()
                    self.limpiarTabla()
                    self.listar()
                except Exception as x:
                    QtWidgets.QMessageBox.critical(self, "Registrar Proveedor","Ocurrio un error al registrar los datos, verifique nuevamente.", QtWidgets.QMessageBox.Ok)
                    print(x)
            else:
                QtWidgets.QMessageBox.critical(self, "Registrar Proveedor",self.validacion(), QtWidgets.QMessageBox.Ok)
        else: 
            if self.validacion()== 0 :
                objProveedor= Proveedor(self.txtRuc.text().strip(),
                                    self.txtNombre.text().strip(),
                                    self.txtRazSocial.text().strip(),
                                    self.txtDireccion.text().strip(),
                                    self.txtTelefono.text().strip())
                Ruc = self.txtRuc.text()
                if aProveedor.verificarExistencia(Ruc)==False:
                    try:
                        aProveedor.insertar(objProveedor)
                        self.reiniciar()
                        self.limpiarTabla()
                        self.listar()
                    except Exception as x:
                        QtWidgets.QMessageBox.critical(self, "Registrar Proveedor","Ocurrio un error al registrar los datos, verifique nuevamente.", QtWidgets.QMessageBox.Ok)
                        print(x)
                else:
                    QtWidgets.QMessageBox.information(self, "Registrar Proveedor", "Ya existe un Proveedor ingresado con la misma Identificacion.", QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.critical(self, "Registrar Proveedor",self.validacion(), QtWidgets.QMessageBox.Ok)

    def cargarDatos(self):
        fila=self.tblProvedores.selectedItems()
        indiceFila=fila[0].row()
        Ruc = self.tblProvedores.item(indiceFila, 0).text()
        Nombre = self.tblProvedores.item(indiceFila, 1).text()
        RazSocial = self.tblProvedores.item(indiceFila, 2).text()
        Direccion = self.tblProvedores.item(indiceFila, 3).text()
        Telefono = self.tblProvedores.item(indiceFila, 4).text()

        self.btnInsertar.setText("Guardar")
        self.txtRuc.setText(Ruc)
        self.txtRuc.setEnabled(False)
        self.txtNombre.setText(Nombre)
        self.txtRazSocial.setText(RazSocial)
        self.txtDireccion.setText(Direccion)
        self.txtTelefono.setText(Telefono)
        self.btnCancelar.setVisible(True)
        self.editar=True
    
    def cancelar(self):
        self.reiniciar()
        self.limpiarTabla()
        self.listar()
    
    def cerrarVentana(self):
        self.close()