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
from Controlador.ArregloCliente import * 

aCliente = ArregloCliente()

class VentanaRegistroClientes(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaRegistroClientes,self).__init__(parent)
        loadUi("UI/REGISTRO-CLIENTE.ui",self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.btnMinimizar.clicked.connect(self.showMinimized)
        self.btnCerrar.clicked.connect(self.cerrarVentana)
        self.txtCelular.setValidator(QIntValidator())
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnListar.clicked.connect(self.listar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnGuardar.clicked.connect(self.grabar)
        self.tblCliente.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listar()
        self.btnGuardar.setVisible(False)
        #self.move(self.acomodarVentana().x() -979, self.acomodarVentana().y() - 475)
        self.show()

    def validacion(self):
        if self.txtNroIdentificacion.text().strip() == "" or self.txtNroIdentificacion.text().isdigit()==False:
            self.txtNroIdentificacion.setFocus()
            return "Error en el Numero de Identificacion"
        elif self.cboTipoIdentificacion.currentText() == "--Seleccionar--":
            return "No se selecciono Tipo Identificacion"
        elif self.txtNombre.text().strip() == "":
            self.txtNombre.setFocus()
            return "No se agrego Nombre"
        elif len(self.txtCelular.text()) !=9:
            self.txtCelular.setFocus()
            return "Error en Numero Celular"
        elif self.txtDireccion.text().strip() == "":
            self.txtDireccion.setFocus()
            return "No se agrego Direccion"
        else:
            return 0 
    
    def limpiarControles(self):
        self.btnGuardar.setVisible(False)
        self.txtNroIdentificacion.setEnabled(True)
        self.txtNroIdentificacion.clear()
        self.cboTipoIdentificacion.setCurrentIndex(0)
        self.txtNombre.clear()
        self.txtCelular.clear()
        self.txtDireccion.clear()  
    
    def limpiarTabla(self):
        self.tblCliente.clearContents()
        self.tblCliente.setRowCount(0)   
           
                 
    def registrar(self):
        if self.validacion()== 0 :
            if self.verificarDocumento():
                objCliente= Cliente(self.txtNroIdentificacion.text(),
                                    self.txtNombre.text(),
                                    self.cboTipoIdentificacion.currentText(),
                                    self.txtDireccion.text(),
                                    self.txtCelular.text())
                nroIdentificacion = self.txtNroIdentificacion.text()
                if aCliente.verificarExistencia(nroIdentificacion)==False:
                    aCliente.insertar(objCliente)
                    self.limpiarControles()
                    self.listar()
                else:
                    QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Ya existe un Cliente ingresado con la misma Identificacion.", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Al parecer "+ self.validacion(), QtWidgets.QMessageBox.Ok)

    def listar(self):
        self.tblCliente.setRowCount(len(aCliente.listar()))
        self.tblCliente.setColumnCount(5)
        self.tblCliente.verticalHeader().setVisible(False)
        listCliente= aCliente.listar()
        for fila, cliente in enumerate(listCliente):
            for columna, valor in enumerate(cliente):
                item = QTableWidgetItem(str(valor))
                self.tblCliente.setItem(fila, columna, item)

    def modificar(self):
        if len(aCliente.listar())==0:
            QtWidgets.QMessageBox.information(self, "Modificar Cliente", "No hay Cliente registrados", QtWidgets.QMessageBox.Ok)
        else:
            nroIdentificacion, _=QtWidgets.QInputDialog.getText(self, "Modificar Cliente", "Ingrese la Identificacion del Cliente que desea modificar") #getText es para que se abra la ventanida y te pida ingresar un dato
            if aCliente.verificarExistencia(nroIdentificacion):
                conexion= conexion = pyodbc.connect(DataBase.CadenaConexion())
                comando = conexion.cursor()
                comando.execute("select * from Cliente where NumeroDocumento = ?", nroIdentificacion)
                clie=comando.fetchone()
                objCliente=Cliente(str(clie[0]),str(clie[1]),str(clie[2]),str(clie[3]),str(clie[4]))

                self.btnGuardar.setVisible(True)
                self.txtNroIdentificacion.setText(objCliente.getNumeroDocumento())
                self.txtNroIdentificacion.setEnabled(False)
                self.cboTipoIdentificacion.setCurrentText(objCliente.getTipoDocumento())
                self.txtNombre.setText(objCliente.getNombre())
                self.txtCelular.setText(objCliente.getTelefono())
                self.txtDireccion.setText(objCliente.getDireccion())
                
    
    def consultar(self):
        self.limpiarControles()
        self.limpiarTabla()
        if len(aCliente.listar())==0:
            QtWidgets.QMessageBox.information(self, "Consultar Cliente", "Aun No Existen Clientes.", QtWidgets.QMessageBox.Ok)
        else:
            nroIdentificacion, _ =QtWidgets.QInputDialog.getText(self, "Consultar Cliente", "Ingrese el Nro de Identificacion del Cliente que desea buscar")
            if aCliente.verificarExistencia(nroIdentificacion)==False:
                QtWidgets.QMessageBox.information(self, "Consultar Cliente", "El Nro de Identificacion que ingreso no existe", QtWidgets.QMessageBox.Ok)
            else:
                self.tblCliente.setRowCount(1)
                self.tblCliente.setColumnCount(5)
                self.tblCliente.verticalHeader().setVisible(False)
                objCliente=aCliente.consultar(nroIdentificacion)
                for columna, valor in enumerate(objCliente):
                    item = QTableWidgetItem(str(valor))
                    self.tblCliente.setItem(0, columna, item)

    def eliminar(self):
        if len(aCliente.listar())==0:
            QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "No hay Cliente registrados", QtWidgets.QMessageBox.Ok)
        else:
            fila=self.tblCliente.selectedItems()
            if fila:
                indiceFila=fila[0].row()
                nombre = self.tblCliente.item(indiceFila, 1).text()
                respuesta = QMessageBox.question(self, "Eliminar Empleado", "¿Seguro que quieres eliminar al Cliente de nombre: "+nombre+"?", QMessageBox.Yes | QMessageBox.No)
                if (respuesta == QMessageBox.Yes):
                    numDocumento=self.tblCliente.item(indiceFila, 0).text()
                    aCliente.eliminar(numDocumento)
                    self.limpiarTabla()
                    self.listar()
                    QtWidgets.QMessageBox.information(self, "Eliminar Empleado", "Empleado Eliminado Correctamente.", QtWidgets.QMessageBox.Ok)
                else:
                    self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "Seleccione una fila", QtWidgets.QMessageBox.Ok)
                

    def grabar(self):
            if self.validacion()== 0:
                if self.verificarDocumento():
                    objCliente= Cliente(self.txtNroIdentificacion.text(),
                                        self.txtNombre.text(),
                                        self.cboTipoIdentificacion.currentText(),
                                        self.txtDireccion.text(),
                                        self.txtCelular.text())
                    aCliente.modificar(objCliente)
                    self.limpiarTabla()
                    self.limpiarControles()
                    self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Al parecer "+ self.validacion(), QtWidgets.QMessageBox.Ok)


            
    def acomodarVentana(self): 
        centro_pantalla = QDesktopWidget().availableGeometry().center()
        desplazamiento_x = 50
        desplazamiento_y = 50
        centro_desplazado = QPoint(centro_pantalla.x() + desplazamiento_x, centro_pantalla.y() + desplazamiento_y)
        return centro_desplazado    
        
    def verificarDocumento(self):
        documento=self.txtNroIdentificacion.text()
        if self.cboTipoIdentificacion.currentText()=="DNI":
            if len(documento) != 8:
                QtWidgets.QMessageBox.information(self, "Registrar Cliente", "¡El DNI debe tener 8 digitos!", QtWidgets.QMessageBox.Ok)
                return False
        elif self.cboTipoIdentificacion.currentText()=="RUC":
            if len(documento) != 11:
                QtWidgets.QMessageBox.information(self, "Registrar Cliente", "¡El RUC debe tener 11 digitos!", QtWidgets.QMessageBox.Ok)
                return False   
        return True
    def cerrarVentana(self):
        self.close()

