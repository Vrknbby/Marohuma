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
from Controlador.ConexionDB import *
from Controlador.ArregloMaterial import *

aMaterial=ArregloMaterial()
DataBase=ConexionDB()
class VentanaInventario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaInventario,self).__init__(parent)
        loadUi("UI/INVENTARIO.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.tblMaterial.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.btnCerrar.clicked.connect(self.cerrarVentana)
        self.ocultarColumnas()
        self.listar("--Todos--")
        self.cargarServicios()
        self.cboListar.currentIndexChanged.connect(self.detectarCboListar)

    def listar(self, servicio):
        if self.cboListar.currentText()=="--Todos--":
            self.tblMaterial.setRowCount(len(aMaterial.listar()))
            self.tblMaterial.setColumnCount(7)
            self.tblMaterial.verticalHeader().setVisible(False)
            lista=aMaterial.listar()
            for fila, material in enumerate(lista):
                for columna, valor in enumerate(material):
                    item = QTableWidgetItem(str(valor))
                    self.tblMaterial.setItem(fila, columna, item)

        else:
            self.tblMaterial.setRowCount(len(aMaterial.listarPorServicio(servicio)))
            self.tblMaterial.setColumnCount(7)
            self.tblMaterial.verticalHeader().setVisible(False)
            lista=aMaterial.listarPorServicio(servicio)
            for fila, material in enumerate(lista):
                    for columna, valor in enumerate(material):
                        item = QTableWidgetItem(str(valor))
                        self.tblMaterial.setItem(fila, columna, item)
    
    def detectarCboListar(self):
        serv=self.cboListar.currentText()
        self.listar(serv)

    def cargarServicios(self):
        conexion=pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT IdServicio FROM Servicio")
        servicios = comando.fetchall()
        conexion.close()
        for servicio in servicios:
            self.cboListar.addItem(str(servicio[0]))
    
    def ocultarColumnas(self):
        self.tblMaterial.setColumnHidden(0, True)
    
    def cerrarVentana(self):
        self.close()