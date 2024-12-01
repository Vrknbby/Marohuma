import sys 
import os 
import re
import shutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QCompleter
from PyQt5 import QtCore 
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QPropertyAnimation 
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget,QDesktopWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate
from datetime import datetime
from PyQt5.QtWidgets import QAbstractItemView
from Controlador.ArregloServicio import * 
from Controlador.ArregloCliente import * 
from Controlador.ArregloEmpleado import * 
from Controlador.ConexionDB import *

aServicio= ArregloServicio()
aCliente = ArregloCliente()
aEmpleado= ArregloEmpleado()
DateBase= ConexionDB()

class VentanaRegistroServicios(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaRegistroServicios,self).__init__(parent)
        loadUi("UI/REGISTRO-SERVICIOS.ui",self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.listSugerencias.setVisible(False)
        self.ocultarColumnas()
        self.tblServicios.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.btnCerrar.clicked.connect(self.cerrarVentana)
        self.btnMinimizar.clicked.connect(self.showMinimized)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.tblServicios.cellClicked.connect(self.cargarDatos)
        self.listSugerencias.itemClicked.connect(self.sugerenciaClick)
        self.btnListar.clicked.connect(self.listar)
        self.dateServicio.setDate(QDate.currentDate())
        self.tblServicios.cellDoubleClicked.connect(self.cambiarEstado)
        self.txtCliente.textChanged.connect(self.cargarSugerencias)
        

        self.Editar=False
        self.txtEmpleado.setText(str(empleado[0][3])+" "+str(empleado[0][4]))
        self.txtEmpleado.setEnabled(False)
        self.fechaActual=datetime.now().strftime("%Y-%m-%d")
        self.listar()
        #self.move(self.acomodarVentana().x() -979, self.acomodarVentana().y() - 475)
        self.show()
        
    def validacion(self):
        if self.cboServicios.currentText() == "--Seleccionar--":
            return "No selecciono el tipo de Servicio"
        elif self.txtID.text().strip() =="":
            self.txtID.setFocus()
            return "No se agrego Identificador"
        elif self.txtNombre.text().strip() =="":
            self.txtNombre.setFocus()
            return "No se agrego Nombre"
        elif self.txtCliente.text().strip() =="":
            self.txtCliente.setFocus()
            return "No selecciono Cliente"
        elif not self.verificarCliente():
            return "El Cliente que ingreso no existe"
        elif not re.match(r'^\d+(\.\d+)?$', self.txtCosto.text()):
            return "Ingrese correctamente el Costo del Servicio"
        elif float(self.txtCosto.text()) < 1:
            return "Ingrese correctamente el Costro del Servicio"
        elif self.txtDireccion.text().strip() == "":
            self.txtDireccion.setFocus()
            return "No se agrego Direccion"
        elif self.spnCantidad.text() == 0 or self.spnCantidad.text()=="":
            self.spnCantidad.setFocus()
            return "No se agrego Cantidad"
        else:
            return 0
    
    def sugerenciaClick(self, item):
        self.txtCliente.setText(item.text())
        self.listSugerencias.setVisible(False)

    def limpiarControles(self):
        self.listSugerencias.setVisible(False)
        self.btnRegistrar.setText("Registrar")
        self.txtID.setEnabled(True)
        self.Editar=False
        self.txtEmpleado.setText(str(empleado[0][3])+" "+str(empleado[0][4]))
        self.txtID.clear()
        self.txtCliente.clear()
        self.cboServicios.setCurrentIndex(0)
        self.dateServicio.setDate(QDate.currentDate())
        self.txtNombre.clear()
        self.txtCosto.clear()
        self.txtDireccion.clear()  
        self.spnCantidad.clear()
    
    def limpiarTabla(self):
        self.tblServicios.clearContents()
        self.tblServicios.setRowCount(0)
         
    def verificarCliente(self):
        txtCli=self.txtCliente.text()
        listCli=aCliente.listar()
        for cliente in listCli:
            if txtCli==cliente[0]:
                return True
        return False
    
    def obtenerIdCliente(self, nombre):
        conexion= pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("select * from Cliente where Nombre = ?",nombre)
        objCliente= comando.fetchone()
        return str(objCliente[0])
    """
    def cargarCboCliente(self):
        conexion= conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT NumeroDocumento, Nombre FROM Cliente")
        clientes= comando.fetchall()
        conexion.close()
        for cliente in clientes:
            num_cliente, nombre = cliente
            #define que en combo box se vera la descripcion pero el valor sera el del ID
            self.cboCliente.addItem(nombre, userData=num_cliente)
    """ 
    def cargarSugerencias(self):
        texto=self.txtCliente.text()
        conexion= pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT NumeroDocumento FROM Cliente")
        clientes= comando.fetchall()
        StrRucs = [str(cliente[0]) for cliente in clientes]
        sugerencias = []
        for ruc in StrRucs:
            if texto in ruc:
                sugerencias.append(ruc)
        self.listSugerencias.clear()
        self.listSugerencias.addItems(sugerencias)
        if texto.strip()=="":
            self.listSugerencias.clear()
            sugerencias=[]

        
        cantidadSug = len(sugerencias)
        alturaItem = 13  # tanteando con el tamaño de la letra
        espacio = 0  # espaciado entre cada elemento
        calculoAltura = cantidadSug * (alturaItem + espacio)
        
        #Toda esta webada es solo para cuando haya un elemento en la lista no se deforme
        if calculoAltura == 13:
            self.listSugerencias.setFixedHeight(30)
        else:
            self.listSugerencias.setFixedHeight(calculoAltura*2)
        self.listSugerencias.setSpacing(0)
        self.listSugerencias.setVisible(bool(sugerencias))
    
    def obtenerIdUsuario(self, nombre):
        linea=str(nombre).split(" ")
        nom=linea[0]
        apellido=linea[1].strip()
        
        conexion= conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        
        comando.execute("Select * from Empleado where Nombre = ? and Apellido = ?;",nom,apellido)
        ojtEmpleado=comando.fetchone()
        dniEmpleado=str(ojtEmpleado[0])
        
        comando.execute("Select * from Usuario where DniEmpleado = ?;", dniEmpleado)
        objUsuario=comando.fetchone()
        idUsuario=int(objUsuario[0])
        conexion.close()
        return idUsuario
        
        
    def registrar(self):
        if (self.Editar):
            if self.validacion()== 0 :
                objServicio= Servicio(self.txtID.text(),
                                        self.txtCliente.text().strip(), 
                                        self.obtenerIdUsuario(self.txtEmpleado.text()),
                                        self.txtNombre.text(),
                                        self.cboServicios.currentText(),
                                        str(self.fechaActual),
                                        self.dateServicio.date().toString("yyyy-MM-dd"),
                                        int(self.spnCantidad.text()),
                                        self.txtDireccion.text(),
                                        float(self.txtCosto.text()),
                                        "En Proceso")
                
                aServicio.modificar(objServicio)
                self.limpiarTabla()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.critical(self, "Registrar Servicio",self.validacion(), QtWidgets.QMessageBox.Ok)
        else: 
            if self.validacion()== 0 :
                objServicio= Servicio(self.txtID.text(),
                                    self.txtCliente.text().strip(),
                                    self.obtenerIdUsuario(self.txtEmpleado.text()),
                                    self.txtNombre.text(),
                                    self.cboServicios.currentText(),
                                    str(self.fechaActual),
                                    self.dateServicio.date().toString("yyyy-MM-dd"),
                                    int(self.spnCantidad.text()),
                                    self.txtDireccion.text(),
                                    float(self.txtCosto.text()),
                                    None)
                ID = self.txtID.text()
                if aServicio.verificarExistencia(ID)==False:
                    try:
                        aServicio.insertar(objServicio)
                        self.crearCarpetaServicio(objServicio)
                        self.limpiarControles()
                        self.listar()
                    except Exception as x:
                        QtWidgets.QMessageBox.critical(self, "Registrar Servicio","Ocurrio un error al registrar los datos, verifique nuevamente.", QtWidgets.QMessageBox.Ok)
                        print(x)
                else:
                    QtWidgets.QMessageBox.information(self, "Registrar Servicio", "Ya existe un Servicio ingresado con la misma Identificacion.", QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.critical(self, "Registrar Servicio",self.validacion(), QtWidgets.QMessageBox.Ok)
            
    def modificar(self):
        if len(aServicio.listar())==0:
            QtWidgets.QMessageBox.information(self, "Modificar Servicio", "No hay Servicio registrados", QtWidgets.QMessageBox.Ok)
        else:
            ID, _=QtWidgets.QInputDialog.getText(self, "Modificar Servicio", "Ingrese la Identificacion del Servicio que desea modificar") #getText es para que se abra la ventanida y te pida ingresar un dato
            
            if aServicio.verificarExistencia(ID):
                conexion= pyodbc.connect(DataBase.CadenaConexion())
                comando = conexion.cursor()
                comando.execute("select * from Servicio where IdServicio = ?", ID)
                objServicio=comando.fetchone()
                fechaFin=str(objServicio[6]).strip()
                año, mes, dia = map(int, fechaFin.split('-'))
                
                self.txtID.setEnabled(False)
                self.btnRegistrar.setText("Guardar")
                self.txtID.setText(objServicio[0])
                self.txtCliente.setText(objServicio[1])
                self.txtEmpleado.setText(self.obtenerNomEmpleado(objServicio[2]))
                self.txtNombre.setText(objServicio[3])
                self.cboServicios.setCurrentText(objServicio[4]) 
                self.dateServicio.setDate(QDate(año,mes,dia))
                self.spnCantidad.setValue(int(objServicio[7]))
                self.txtDireccion.setText(objServicio[8])
                self.txtCosto.setText(str(objServicio[9]))
                comando.close()
                self.Editar=True
            else:
                QtWidgets.QMessageBox.information(self, "Modificar Servicio", "El Codigo del Servicio que ingreso no se encuentra Registrado", QtWidgets.QMessageBox.Ok)
                
    def obtenerNomCliente(self, numeroDocuemto):
        conexion= pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("Select * from Cliente where NumeroDocumento = ?",numeroDocuemto)
        objCliente=comando.fetchone()
        return str(objCliente[1])
    
    def obtenerNomEmpleado(self, idUsuario):
        conexion= pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("Select * from Usuario where IdUsuario = ?",idUsuario)
        objUsuario=comando.fetchone()
        dniUsario=objUsuario[1]
        comando.execute("Select * from Empleado where DniEmpleado = ?",dniUsario)
        objEmpleado=comando.fetchone()
        usuario=str(objEmpleado[3])+" " + str(objEmpleado[4])
        return usuario
        
    def consultar(self): 
        self.limpiarControles()
        self.limpiarTabla()
        if len(aServicio.listar())==0:
            QtWidgets.QMessageBox.information(self, "Consultar Servicio", "Aun No Existen Servicios.", QtWidgets.QMessageBox.Ok)
        else:
            dni, _ =QtWidgets.QInputDialog.getText(self, "Consultar Servicio", "Ingrese el ID del Servicio que desea buscar")
            if aServicio.verificarExistencia(dni)==False:
                QtWidgets.QMessageBox.information(self, "Consultar Servicio", "El ID que ingreso no existe", QtWidgets.QMessageBox.Ok)
            else:
                self.tblServicios.setRowCount(1)
                self.tblServicios.setColumnCount(10)
                self.tblServicios.verticalHeader().setVisible(False)
                objServicio=aServicio.consultar(dni)
                for columna, valor in enumerate(objServicio):
                    item = QTableWidgetItem(str(valor))
                    self.tblServicios.setItem(0, columna, item)
           
    def listar(self):
        self.tblServicios.setRowCount(len(aServicio.listar()))
        self.tblServicios.setColumnCount(11)
        self.tblServicios.verticalHeader().setVisible(False)
        lista=aServicio.listar()
        #itera por cada fila atrapando el indice y el objeto
        for fila, servicio in enumerate(lista):
            for columna, valor in enumerate(servicio):
                # Convertir el valor a una cadena y establecerlo en la celda correspondiente
                item = QTableWidgetItem(str(valor))
                self.tblServicios.setItem(fila, columna, item)

    def crearCarpetaServicio(self, objServicio):
        os.mkdir("PROYECTOS/"+objServicio.getIdServicio().strip())

    #evento en el click para ocultar la lista
    def mousePressEvent(self, event):
        if not self.listSugerencias.geometry().contains(event.pos()):
            self.listSugerencias.setVisible(False)

    def ocultarColumnas(self):
        self.tblServicios.setColumnHidden(4, True)
        self.tblServicios.setColumnHidden(5, True)
        self.tblServicios.setColumnHidden(6, True)
        self.tblServicios.setColumnHidden(7, True)
        self.tblServicios.setColumnHidden(10, True)

    def cargarDatos(self):
        fila=self.tblServicios.selectedItems()
        indiceFila=fila[0].row()
        Id = self.tblServicios.item(indiceFila, 0).text()
        Cliente = self.tblServicios.item(indiceFila, 1).text()
        Usuario = self.tblServicios.item(indiceFila, 2).text()
        nomProy = self.tblServicios.item(indiceFila, 3).text()
        tipo = self.tblServicios.item(indiceFila, 4).text()
        fechaIn = self.tblServicios.item(indiceFila, 5).text()
        fechaFin = self.tblServicios.item(indiceFila, 6).text()
        cantEmpl = self.tblServicios.item(indiceFila, 7).text()
        direccion = self.tblServicios.item(indiceFila, 8).text()
        costo = self.tblServicios.item(indiceFila, 9).text()
        Estado = self.tblServicios.item(indiceFila, 10).text()

        self.datoServicio.setText(Id) 
        self.datoCliente.setText(Cliente)
        self.datoUsuario.setText(self.obtenerNomEmpleado(Usuario))
        self.datoFechaInicio.setText(fechaIn)
        self.datoDireccion.setText(direccion)
        self.datoNombre.setText(nomProy)
        self.datoCosto.setText(costo)
        self.datoEmpl.setText(cantEmpl)
        self.datoFechaFin.setText(fechaFin)
        self.datoEstado.setText(Estado)
        
    def cambiarEstado(self):
        fila=self.tblServicios.selectedItems()
        if fila:
            indiceFila=fila[0].row()
            nombre = self.tblServicios.item(indiceFila, 3).text()
            respuesta = QMessageBox.question(self, "Estado Servicio", "¿Desea Cambiar el estado del proyecto: "+nombre+"?", QMessageBox.Yes | QMessageBox.No)
            if (respuesta == QMessageBox.Yes):
                id=self.tblServicios.item(indiceFila, 0).text()
                aServicio.cambiarEstado(id)
                self.limpiarTabla()
                self.listar()
                QtWidgets.QMessageBox.information(self, "Estado Servicio", "Estado Cambiado Correctamente.", QtWidgets.QMessageBox.Ok)
            else:
                self.listar()

    def cerrarVentana(self):
        self.close()
    
                
         
