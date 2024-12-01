import sys 
import shutil
import os  
from PyQt5.QtCore import QDate
from PyQt5 import QtCore 
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QPropertyAnimation 
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget,QDesktopWidget
from PyQt5.uic import loadUi
from Controlador.ConexionDB import *
from Controlador.ArregloMovimientoMaterial import *

aMovimientoMaterial=ArregloMovimientoMaterial()
DataBase=ConexionDB()
class VentanaMovimientos(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaMovimientos,self).__init__(parent)
        loadUi("UI/MOVIMIENTO-MATERIAL.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.tblListaMaterial.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listar("--Todos--")
        self.ocultarColumnas()
        self.btnCerrar.clicked.connect(self.cerrarVentana)
        self.cboListar.currentIndexChanged.connect(self.detectarCboListar)
    
    def listar(self, servicio):
        if self.cboListar.currentText()=="--Todos--":
            self.tblListaMaterial.setRowCount(len(aMovimientoMaterial.listarVista()))
            self.tblListaMaterial.setColumnCount(9)
            self.tblListaMaterial.verticalHeader().setVisible(False)
            lista=aMovimientoMaterial.listarVista()
            for fila, movimiento in enumerate(lista):
                for columna, valor in enumerate(movimiento):
                    item = QTableWidgetItem(str(valor))
                    self.tblListaMaterial.setItem(fila, columna, item)

        else:
            self.tblListaMaterial.setRowCount(len(aMovimientoMaterial.listarPor(servicio)))
            self.tblListaMaterial.setColumnCount(9)
            self.tblListaMaterial.verticalHeader().setVisible(False)
            lista=aMovimientoMaterial.listarPor(servicio)
            for fila, movimiento in enumerate(lista):
                    for columna, valor in enumerate(movimiento):
                        item = QTableWidgetItem(str(valor))
                        self.tblListaMaterial.setItem(fila, columna, item)
    
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
        self.tblListaMaterial.setColumnHidden(0, True)

    def cerrarVentana(self):
        self.close()