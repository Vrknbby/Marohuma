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
from Controlador.ArregloDocumento import *


aDocumento= ArregloDocumento()
DataBase=ConexionDB()
class VentanaRegistroDocumentos(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaRegistroDocumentos,self).__init__(parent)
        loadUi("UI/REGISTRO-DOCUMENTOS.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.cargarServicios()
        self.rutaSalida=""
        self.rutaArch=""
        self.listar("--Todos--")
        self.cargarServiciosListar()
        self.dateFecha.setDate(QDate.currentDate())
        self.btnMinimizar.clicked.connect(self.showMinimized)
        self.btnCerrar.clicked.connect(self.cerrarVentana)
        self.cboListar.currentIndexChanged.connect(self.detectarCboListar)
        self.btnSubir.clicked.connect(self.subirArchivo)
        self.btnGuardar.clicked.connect(self.guardar)
        self.dateFecha.setVisible(False)
        self.lblFecha.setVisible(False)
        self.tblDocumentos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cboTipo.currentIndexChanged.connect(self.detectarTipo)

    def detectarTipo(self):
        if self.cboTipo.currentText()=="Informes":
            self.dateFecha.setVisible(True)
            self.lblFecha.setVisible(True)
        else:
            self.dateFecha.setVisible(False)
            self.lblFecha.setVisible(False)

    def validacion(self):
        if self.rutaArch=="":
            return "Olvido subir Documento"
        elif self.cboServicio.currentText() == "--Seleccionar--" :
            return "No selecciono un Servicio"
        elif self.cboTipo.currentText() == "--Seleccionar--" :
            return "No selecciono un tipo de documento"
        elif self.txtID.text().strip() == "":
            return "No ingreso ID"
        elif self.pteDescripcion.toPlainText().strip() == "":
            return "No ingreso Descripcion"
        else:
            return 0 

    def reiniciar(self):
        self.cboListar.setCurrentIndex(0)
        self.listar("--Todos--")
        self.rutaSalida=""
        self.rutaArch=""
        self.pteDescripcion.clear()
        self.txtID.clear()
        self.cboServicio.setCurrentIndex(0)
        self.cboTipo.setCurrentIndex(0)
        self.dateFecha.setDate(QDate.currentDate())
        self.dateFecha.setVisible(False)
        self.lblFecha.setVisible(False)

    def subirArchivo(self):
        #esto devuelve una tupla por eso lo separo
        self.rutaArch,_ = QFileDialog.getOpenFileName(self,"Seleccione el Documento","","Archivos Tipo Word (*.docx);;Archivos PDF (*.pdf)")

    def cargarServicios(self):
        conexion= conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT IdServicio FROM Servicio where Estado = 'En Proceso'")
        servicios = comando.fetchall()
        conexion.close()
        for servicio in servicios:
            self.cboServicio.addItem(str(servicio[0]))

    def cargarServiciosListar(self):
        conexion= conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT IdServicio FROM Servicio")
        servicios = comando.fetchall()
        conexion.close()
        for servicio in servicios:
            self.cboListar.addItem(str(servicio[0]))

    def guardar(self):
        if self.cboTipo.currentText()=="Informes":
            if self.validacion()!=0:
                QtWidgets.QMessageBox.critical(self, "Subir Archivo", self.validacion(), QtWidgets.QMessageBox.Ok)
            else:
                documento = Documento(self.txtID.text(),
                                    self.cboServicio.currentText(),
                                    self.cboTipo.currentText(),
                                    self.pteDescripcion.toPlainText(),
                                    self.dateFecha.date().toString("yyyy-MM-dd"))
                id= documento.getID()
                if aDocumento.verificarExistencia(id)==False:
                    aDocumento.insertar(documento)
                    self.definirSalida(self.rutaArch, documento)
                    if self.rutaArch:
                        try:
                            shutil.copy(self.rutaArch,self.rutaSalida)
                            self.reiniciar()
                        except IOError as e:
                            print(e)
                else:
                    QtWidgets.QMessageBox.critical(self, "Subir Archivo", "Ya existe un documento con el mismo Identificador.", QtWidgets.QMessageBox.Ok)
        else:
            if self.validacion()!=0:
                QtWidgets.QMessageBox.critical(self, "Subir Archivo", self.validacion(), QtWidgets.QMessageBox.Ok)
            else:
                documentoSinFech = Documento(self.txtID.text(),
                                    self.cboServicio.currentText(),
                                    self.cboTipo.currentText(),
                                    self.pteDescripcion.toPlainText())
                id= documentoSinFech.getID()
                if aDocumento.verificarExistencia(id)==False:
                    aDocumento.insertarSinFecha(documentoSinFech)
                    self.definirSalida(self.rutaArch, documentoSinFech)
                    if self.rutaArch:
                        try:
                            shutil.copy(self.rutaArch,self.rutaSalida)
                            self.reiniciar()
                        except IOError as e:
                            print(e)
                else:
                    QtWidgets.QMessageBox.critical(self, "Subir Archivo", "Ya existe un documento con el mismo Identificador.", QtWidgets.QMessageBox.Ok)

    def detectarCboListar(self):
        serv=self.cboListar.currentText()
        self.listar(serv)

    def listar(self, servicio):
        if self.cboListar.currentText()=="--Todos--":
            self.tblDocumentos.setRowCount(len(aDocumento.listar()))
            self.tblDocumentos.setColumnCount(5)
            self.tblDocumentos.verticalHeader().setVisible(False)
            lista=aDocumento.listar()
            for fila, Documento in enumerate(lista):
                for columna, valor in enumerate(Documento):
                    if str(valor) == "None":
                        valor= ""
                    item = QTableWidgetItem(str(valor))
                    self.tblDocumentos.setItem(fila, columna, item)
        else:
            self.tblDocumentos.setRowCount(len(aDocumento.listarPor(servicio)))
            self.tblDocumentos.setColumnCount(5)
            self.tblDocumentos.verticalHeader().setVisible(False)
            lista=aDocumento.listarPor(servicio)
            for fila, Documento in enumerate(lista):
                    for columna, valor in enumerate(Documento):
                        if str(valor) == "None":
                            valor= ""
                        item = QTableWidgetItem(str(valor))
                        self.tblDocumentos.setItem(fila, columna, item)
    
    def definirSalida(self, rutaDoc, objDoc):
        columna = str(rutaDoc).split("/")
        nombre= columna[-1]
        if not (os.path.exists("PROYECTOS/"+objDoc.getIdServicio()+"/Documentos/"+objDoc.getTipo()+"/")):
            if not (os.path.exists("PROYECTOS/"+objDoc.getIdServicio()+"/Documentos/")):
                os.mkdir("PROYECTOS/"+objDoc.getIdServicio()+"/Documentos/")
                os.mkdir("PROYECTOS/"+objDoc.getIdServicio()+"/Documentos/"+objDoc.getTipo()+"/")
            else:
                os.mkdir("PROYECTOS/"+objDoc.getIdServicio()+"/Documentos/"+objDoc.getTipo()+"/")
        self.rutaSalida="PROYECTOS/"+objDoc.getIdServicio()+"/Documentos/"+objDoc.getTipo()+"/"+nombre

    def cerrarVentana(self):
        self.close()