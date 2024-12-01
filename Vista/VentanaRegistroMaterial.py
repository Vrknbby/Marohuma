import sys 
import shutil
import os  
from PyQt5.QtCore import QDate
from PyQt5 import QtCore 
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QPropertyAnimation 
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget,QDesktopWidget
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QAbstractItemView
from Controlador.ConexionDB import *
from Controlador.ArregloMaterial import *

aMaterial=ArregloMaterial()
DataBase=ConexionDB()
class VentanaRegistroMaterial(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaRegistroMaterial,self).__init__(parent)
        loadUi("UI/REGISTRO-MATERIAL.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.cargarServicios()
        self.listar("--Todos--")
        self.ocultarColumnas()
        self.tblMaterial.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cboListar.currentIndexChanged.connect(self.detectarCboListar)
        self.btnInsertarMaterial.clicked.connect(self.insertar)
        self.btnCerrar.clicked.connect(self.cerrarVentana)

    def validacion(self):
        if self.cboServicio.currentText() == "--Seleccionar--":
            return "No selecciono el Servicio"
        elif self.txtNombreMaterial.text().strip() == "":
            return "No ingreso un nombre para el Material"
        elif self.pteDescripcion.toPlainText().strip()=="":
            return "Olvido agregar una Descripcion"
        elif self.cboUndMedida.currentText() == "--Seleccionar--":
            return "No selecciono una unidad de Medida"
        elif self.txtFrenteMaterial.text().strip()=="":
            return "No ingreso el frente"
        else:
            return 0 

    def reiniciar(self):
        self.listar("--Todos--")
        self.cboListar.setCurrentIndex(0)
        self.cboServicio.setCurrentIndex(0)
        self.txtNombreMaterial.clear()
        self.pteDescripcion.clear()
        self.cboUndMedida.setCurrentIndex(0)
        self.txtFrenteMaterial.clear()

    def limpiarTabla(self):
        self.tblMaterial.clearContents()
        self.tblMaterial.setRowCount(0)  

    def cargarServicios(self):
        conexion=pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT IdServicio FROM Servicio")
        servicios = comando.fetchall()
        conexion.close()
        for servicio in servicios:
            self.cboServicio.addItem(str(servicio[0]))  
            self.cboListar.addItem(str(servicio[0]))  
    
    def insertar(self):
        if self.validacion() == 0:
            material= Material(
                None,
                self.cboServicio.currentText(),
                self.txtNombreMaterial.text().strip(),
                self.pteDescripcion.toPlainText().strip(),
                0,
                self.cboUndMedida.currentText(),
                self.txtFrenteMaterial.text()
            )
            if not aMaterial.verificarNombre(material.getIdServicio(),material.getNombre()):
                aMaterial.insertar(material)
                self.reiniciar()
                self.limpiarTabla()
                self.listar(self.cboListar.currentText())
            else:
                QtWidgets.QMessageBox.critical(self, "Registrar Material", "Ya se encuentra registrado un Material con el mismo nombre. \nPor favor, Especifique mejor el nombre con el que desea registrar el producto.", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.critical(self, "Registrar Material", self.validacion(), QtWidgets.QMessageBox.Ok)

    def detectarCboListar(self):
        serv=self.cboListar.currentText()
        self.listar(serv)

    def listar(self, servicio):
        if self.cboListar.currentText()=="--Todos--":
            self.tblMaterial.setRowCount(len(aMaterial.listar()))
            self.tblMaterial.setColumnCount(7)
            self.tblMaterial.verticalHeader().setVisible(False)
            lista=aMaterial.listar()
            for fila, detalle in enumerate(lista):
                for columna, valor in enumerate(detalle):
                    item = QTableWidgetItem(str(valor))
                    self.tblMaterial.setItem(fila, columna, item)

        else:
            self.tblMaterial.setRowCount(len(aMaterial.listarPorServicio(servicio)))
            self.tblMaterial.setColumnCount(7)
            self.tblMaterial.verticalHeader().setVisible(False)
            lista=aMaterial.listarPorServicio(servicio)
            for fila, Documento in enumerate(lista):
                    for columna, valor in enumerate(Documento):
                        item = QTableWidgetItem(str(valor))
                        self.tblMaterial.setItem(fila, columna, item)

    def ocultarColumnas(self):
        self.tblMaterial.setColumnHidden(0, True)
        self.tblMaterial.setColumnHidden(4, True)

    def cerrarVentana(self):
        self.close()