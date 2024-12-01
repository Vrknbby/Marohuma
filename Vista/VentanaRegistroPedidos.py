import sys 
import pyodbc
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore 
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QPropertyAnimation 
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget,QDesktopWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QAbstractItemView
from Controlador.ArregloPedido import * 
aPedido = ArregloPedido()
class VentanaRegistroPedido(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaRegistroPedido,self).__init__(parent)
        loadUi("UI/REGISTRO-PEDIDO.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.btnCerrar.clicked.connect(self.cerrarVentana)
        self.lbID.setVisible(False)
        self.cargarCboProveedor()
        self.tblPedido.cellDoubleClicked.connect(self.cargarDatos)
        self.btnCancelar.clicked.connect(self.reiniciar)
        self.btnGuardar.clicked.connect(self.insertar)
        self.dtFecha.setDate(QDate.currentDate())
        self.tblPedido.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Edit=False
        self.listar()
        self.show()

    def limpiarTabla(self):
        self.tblPedido.clearContents()
        self.tblPedido.setRowCount(0)  

    def reiniciar(self):
        self.btnGuardar.setText("Insertar")
        self.btnCancelar.setVisible(False)
        self.Edit=False
        self.txtNroDocumento.setEnabled(True)
        self.cboProveedor.setCurrentIndex(0)
        self.txtNroDocumento.clear()
        self.dtFecha.setDate(QDate.currentDate())
    
    def validacion(self):
        if self.cboProveedor.currentText() == "--Seleccionar--":
            return "No selecciono Proveedor"
        elif self.txtNroDocumento.text().strip() == "" or self.txtNroDocumento.text().isdigit()==False:
            self.txtNroDocumento.setFocus()
            return "Error en numero de documento"
        
        else:
            return 0

    def cargarDatos(self):
        fila=self.tblPedido.selectedItems()
        indiceFila=fila[0].row()
        numDoc = self.tblPedido.item(indiceFila, 0).text()
        Proveedor = self.tblPedido.item(indiceFila, 1).text()
        fecha = self.tblPedido.item(indiceFila, 3).text()

        fech=str(fecha).strip()
        año, mes, dia = map(int, fech.split('-'))

        self.btnGuardar.setText("Guardar")
        self.txtNroDocumento.setEnabled(False)
        self.cboProveedor.setCurrentText(Proveedor)
        self.txtNroDocumento.setText(numDoc)
        self.dtFecha.setDate(QDate(año,mes,dia))

        self.btnCancelar.setVisible(True)
        self.Edit=True

    def insertar(self):
        if self.validacion() == 0:
            if (self.Edit):
                pedido= Pedido(self.txtNroDocumento.text(),
                            self.obtenerRucProveedor(self.cboProveedor.currentText()),
                            "Factura",
                            self.dtFecha.date().toString("yyyy-MM-dd"),
                            None)
                aPedido.modificar(pedido)
                self.reiniciar()
                self.limpiarTabla()
                self.listar()
            else:
                pedido= Pedido(self.txtNroDocumento.text(),
                            self.obtenerRucProveedor(self.cboProveedor.currentText()),
                            "Factura",
                            self.dtFecha.date().toString("yyyy-MM-dd"),
                            None)
                aPedido.insertar(pedido)
                self.reiniciar()
                self.limpiarTabla()
                self.listar()
        else:
            QtWidgets.QMessageBox.critical(self, "Registrar Pedido", self.validacion(), QtWidgets.QMessageBox.Ok)



    def listar(self):
        self.tblPedido.setRowCount(len(aPedido.listar()))
        self.tblPedido.setColumnCount(4)
        self.tblPedido.verticalHeader().setVisible(False)
        lista=aPedido.listarVista()
        #itera por cada fila atrapando el indice y el objeto
        for fila, pedido in enumerate(lista):
            for columna, valor in enumerate(pedido):
                # Convertir el valor a una cadena y establecerlo en la celda correspondiente
                item = QTableWidgetItem(str(valor))
                self.tblPedido.setItem(fila, columna, item)
                
    def cargarCboProveedor(self):
        conexion= conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT Ruc, Nombre FROM Proveedor")
        proveedores= comando.fetchall()
        conexion.close()
        for proveedor in proveedores:
            num_proveedor, nombre = proveedor
            #define que en combo box se vera la descripcion pero el valor sera el del ID
            self.cboProveedor.addItem(nombre, userData=num_proveedor)

    def obtenerRucProveedor(self, Nombre):
        conexion= conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("select * from Proveedor where Nombre = ?", Nombre)
        objProvee= comando.fetchone()
        id=str(objProvee[0])
        comando.close()
        return id

    def cancelar(self):
        self.reiniciar()
        self.limpiarTabla()
        self.listar()

    def verificarDocumento(self):
        documento=self.txtNroDocumento.text()
        if self.cboComprobante.currentText()=="Boleta":
            if len(documento) != 8:
                QtWidgets.QMessageBox.critical(self, "Registrar Pedido", "¡La boleta debe tener 8 digitos!", QtWidgets.QMessageBox.Ok)
                return False
        elif self.cboComprobante.currentText()=="Factura":
            if len(documento) != 11:
                QtWidgets.QMessageBox.critical(self, "Registrar Pedido", "¡La Factura debe tener 11 digitos!", QtWidgets.QMessageBox.Ok)
                return False   
        return True

    def cerrarVentana(self):
        self.close()













