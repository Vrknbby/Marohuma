import sys 
import datetime
from PyQt5 import QtCore 
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QPropertyAnimation 
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget,QDesktopWidget
from PyQt5.uic import loadUi
from Controlador.ConexionDB import *
from PyQt5.QtWidgets import QAbstractItemView
from Controlador.ArregloMovimientoMaterial import *
from Controlador.ArregloEmpleado import empleado
from Controlador.ArregloEmpleado import *
from Controlador.ArregloMaterial import *

aMaterial= ArregloMaterial()
aEmpleado= ArregloEmpleado()
aMovimiento= ArregloMovimientoMaterial()
DataBase=ConexionDB()
class VentanaRegistroSalidas(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaRegistroSalidas,self).__init__(parent)
        loadUi("UI/SALIDA-MATERIAL.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.cargarServicios()
        self.ocultarColumnas()
        self.listar()
        self.cboServicio.currentIndexChanged.connect(self.limpiarProducto)
        self.IdMaterial.setVisible(False)
        self.btnCerrar.clicked.connect(self.cerrarVentana)
        self.txtDNIEmpleado.textChanged.connect(self.cargarSugerenciasEmpleado)
        self.listSugerenciaEmpleado.setVisible(False)
        self.listSugerenciaEmpleado.itemClicked.connect(self.sugerenciaClickEmpleado)

        self.txtIdMaterial.textChanged.connect(self.cargarSugerenciasMaterial)
        self.listSugerenciaMaterial.setVisible(False)
        self.listSugerenciaMaterial.itemClicked.connect(self.sugerenciaClickMaterial)
        self.btnInsertarSalida.clicked.connect(self.insertar)
        self.tblSalidaMaterial.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def validacion(self):
        if self.txtDNIEmpleado.text().strip() == "":
            self.txtDNIEmpleado.setFocus()
            return "No se agrego DNI"
        elif len(self.txtDNIEmpleado.text()) != 8:
            self.txtDNIEmpleado.setFocus()
            return "Ingreso de Dni invalido"
        elif not aEmpleado.verificarExistencia(self.txtDNIEmpleado.text()):
            return "El Dni que ingreso no se encuentra registrado."
        elif self.cboServicio.currentText() == "--Seleccionar--":
            return "No seleccionó el Servicio" 
        elif self.IdMaterial.text().strip() == "":
            return "El Material que ingresó no existe"
        elif self.txtFrenteSalida.text().strip() == "":
            return "No Agrego Frente"
        elif self.txtCantidadSalida.text().isdigit()==False or int(self.txtCantidadSalida.text()) < 1:
            return "Ingrese correctamente la cantidad."
        else:
            return 0

    def listar(self):
        self.tblSalidaMaterial.setRowCount(len(aMovimiento.listarSalidas()))
        self.tblSalidaMaterial.setColumnCount(8)
        self.tblSalidaMaterial.verticalHeader().setVisible(False)
        lista=aMovimiento.listarSalidas()
        for fila, pedido in enumerate(lista):
            for columna, valor in enumerate(pedido):
                item = QTableWidgetItem(str(valor))
                self.tblSalidaMaterial.setItem(fila, columna, item)

    def reiniciar(self):
        self.listar()
        self.IdMaterial.clear()
        self.cboServicio.setCurrentIndex(0)
        self.txtDNIEmpleado.clear()
        self.txtIdMaterial.clear()
        self.txtFrenteSalida.clear()
        self.txtCantidadSalida.clear()
        


    def limpiarTabla(self):
        self.tblSalidaMaterial.clearContents()
        self.tblSalidaMaterial.setRowCount(0) 

    def cargarServicios(self):
        conexion=pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT IdServicio FROM Servicio where Estado = 'En Proceso'")
        servicios = comando.fetchall()
        conexion.close()
        for servicio in servicios:
            self.cboServicio.addItem(str(servicio[0]))
    
    def cargarSugerenciasEmpleado(self):
        texto = self.txtDNIEmpleado.text()
        conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT DniEmpleado FROM Empleado where Estado = 'Activo'")
        empleados = comando.fetchall()

        sugerencias = []
        for empleado in empleados:
            if texto.upper() in str(empleado[0]).upper():
                sugerencias.append(str(empleado[0]))

        self.listSugerenciaEmpleado.clear()
        self.listSugerenciaEmpleado.addItems(sugerencias)
        if not texto.strip():
            self.listSugerenciaEmpleado.clear()
            sugerencias = []

        cantidadSug = len(sugerencias)
        alturaItem = 13
        espacio = 0
        calculoAltura = cantidadSug * (alturaItem + espacio)

        if calculoAltura == 13:
            self.listSugerenciaEmpleado.setFixedHeight(30)
        else:
            self.listSugerenciaEmpleado.setFixedHeight(calculoAltura * 2)

        self.listSugerenciaEmpleado.setSpacing(0)
        self.listSugerenciaEmpleado.setVisible(bool(sugerencias))

    def sugerenciaClickEmpleado(self, item):
        self.txtDNIEmpleado.setText(item.text())
        self.listSugerenciaEmpleado.setVisible(False)
    
    def cargarServicios(self):
        conexion=pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT IdServicio FROM Servicio where Estado = 'En Proceso'")
        servicios = comando.fetchall()
        conexion.close()
        for servicio in servicios:
            self.cboServicio.addItem(str(servicio[0]))
    
    def cargarSugerenciasMaterial(self):
        texto = self.txtIdMaterial.text()
        servicio = self.cboServicio.currentText()
        conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT IdMaterial, Nombre, IdServicio, Frente FROM Material")
        Materiales = comando.fetchall()

        sugerencias = []
        for material in Materiales:
            Idmaterial, NombreMaterial, IdServicio, Frente = material
            if servicio == IdServicio:
                if texto.upper() in str(NombreMaterial).upper():
                    sugerencias.append(str(NombreMaterial))
                if self.txtIdMaterial.text().upper().strip() == NombreMaterial.upper():
                    self.IdMaterial.setText(str(Idmaterial))
                    self.txtFrenteSalida.setText(str(Frente))
                    break
                else:
                    self.IdMaterial.clear()

        self.listSugerenciaMaterial.clear()
        self.listSugerenciaMaterial.addItems(sugerencias)
        if not texto.strip():
            self.listSugerenciaMaterial.clear()
            sugerencias = []

        cantidadSug = len(sugerencias)
        alturaItem = 13
        espacio = 0
        calculoAltura = cantidadSug * (alturaItem + espacio)

        if calculoAltura == 13:
            self.listSugerenciaMaterial.setFixedHeight(30)
        else:
            self.listSugerenciaMaterial.setFixedHeight(calculoAltura * 2)

        self.listSugerenciaMaterial.setSpacing(0)
        self.listSugerenciaMaterial.setVisible(bool(sugerencias))

    def sugerenciaClickMaterial(self, item):
        self.txtIdMaterial.setText(item.text())
        self.listSugerenciaMaterial.setVisible(False)

    def insertar(self):
        fechaHoy = datetime.datetime.now().date()
        formatoCorrecto=fechaHoy.strftime('%Y-%m-%d')
        if self.validacion()==0:
            Movimiento = MovimientoMaterial(
                None,
                self.conseguirDniUsuario(empleado[0][0]),
                int(self.IdMaterial.text()),
                self.txtDNIEmpleado.text(),
                self.cboServicio.currentText(),
                "Salida",
                self.txtFrenteSalida.text(),
                int(self.txtCantidadSalida.text()),
                formatoCorrecto
            )
            if aMaterial.reducirStock(Movimiento.getIdMaterial(), Movimiento.getCantidad()):
                aMovimiento.insertar(Movimiento)
                self.limpiarTabla()
                self.reiniciar()
            else:
                QtWidgets.QMessageBox.critical(self, "Registrar Salida", "La cantidad que ingreso supera al Stock Disponible.", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.critical(self, "Registrar Salida", self.validacion(), QtWidgets.QMessageBox.Ok)
    
    def conseguirDniUsuario(self, dniEmpl):
        conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT * FROM Usuario WHERE DniEmpleado = ?", dniEmpl)
        usuario = comando.fetchone()
        comando.close()
        return str(usuario[0])

    def ocultarColumnas(self):
        self.tblSalidaMaterial.setColumnHidden(0, True)
        self.tblSalidaMaterial.setColumnHidden(5, True)

    def limpiarProducto(self):
        self.txtIdMaterial.clear()
        self.IdMaterial.clear()
        self.txtFrenteSalida.clear()

    def cerrarVentana(self):
        self.close()