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
from datetime import datetime, timedelta
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import QObject, pyqtSignal
from Controlador.ArregloEmpleado import * 
from Controlador.ArregloUsuario import * 

aEmpleado = ArregloEmpleado()
aUsuario = ArregloUsuario()
class VentanaRegistroEmpleado(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaRegistroEmpleado,self).__init__(parent)
        loadUi("UI/REGISTRO-EMPLEADO.ui",self)
        #Permite el ingreso de todo menos numeros
        formato = QRegExp("[^0-9]*")
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.btnCerrar.clicked.connect(self.cerrarVentana)
        self.txtDni.setValidator(QIntValidator())
        self.txtSueldo.setValidator(QIntValidator())
        self.txtNombre.setValidator(QRegExpValidator(formato))
        self.txtApellido.setValidator(QRegExpValidator(formato))
        self.cboListar.currentIndexChanged.connect(self.detectarCboListar)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnGuardar.clicked.connect(self.grabar)
        self.tblEmpleado.cellDoubleClicked.connect(self.cambiarEstado)
        self.btnGuardar.setVisible(False)
        self.deFechaNacimiento.setDate(QDate.currentDate())
        self.cargarCboEspecialidad()
        self.cargarCboRol()
        self.cboEspecialidad.currentIndexChanged.connect(self.verificarEspecialidad)
        self.listar("--Todos--")
        self.tblEmpleado.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #self.move(self.acomodarVentana().x() -979, self.acomodarVentana().y() - 475)
        self.show()
        
    def validacion(self):
        if self.txtDni.text().strip() == "":
            self.txtDni.setFocus()
            return "No se agrego DNI"
        elif len(self.txtDni.text()) != 8:
            self.txtDni.setFocus()
            return "Ingreso de Dni invalido"
        elif self.cboRol.currentText() == "--Seleccionar--":
            return "No selecciono rol"
        elif self.txtNombre.text().strip() == "":
            self.txtNombre.setFocus()
            return "No se agrego Nombre"
        elif self.txtApellido.text().strip() == "":
            self.txtApellido.setFocus()
            return "No se agrego Apellidos"
        elif not self.verificarMayorDeEdad(self.deFechaNacimiento.date().toString("yyyy-MM-dd")):
            return "La Fecha que ingreso no es adecuada."
        elif self.txtEmail.text().strip() == "":
            self.txtEmail.setFocus()
            return "No se agrego eMail"
        elif self.txtSueldo.text().strip() == "":
            self.txtSueldo.setFocus()
            return "No se agrego Sueldo"
        else:
            return 0 
    
    def verificarMayorDeEdad(self, fecha_nacimiento):
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        
        fecha_actual = datetime.now()
        edad = fecha_actual - fecha_nacimiento
        
        if edad < timedelta(days=365*18):
            return False
        else:
            return True
        
    def limpiarControles(self):
        self.listar(self.cboListar.currentText())
        self.btnRegistrar.setVisible(True)
        self.btnGuardar.setVisible(False)
        self.txtDni.clear()
        self.cboEspecialidad.setCurrentIndex(0)
        self.txtNombre.clear()
        self.txtApellido.clear()
        self.cboRol.setCurrentIndex(0)
        self.deFechaNacimiento.setDate(QDate.currentDate())
        self.txtEmail.clear()
        self.txtSueldo.clear()
        self.txtDni.setEnabled(True) 
    
    def limpiarTabla(self):
        self.tblEmpleado.clearContents()
        self.tblEmpleado.setRowCount(0)   
                 
    def registrar(self):
        if self.validacion()== 0 :
            objEmpleado= Empleado(self.txtDni.text(),
                                self.obtenerIdEspecialidad(self.cboEspecialidad.currentText()),
                                self.obtenerIdRol(self.cboRol.currentText()),
                                self.txtNombre.text(),
                                self.txtApellido.text(),
                                self.deFechaNacimiento.date().toString("yyyy-MM-dd"),
                                float(self.txtSueldo.text()),
                                self.txtEmail.text(),
                                None)
            dni = self.txtDni.text()
            if aEmpleado.verificarExistencia(dni)==False:
                try:
                    aEmpleado.insertar(objEmpleado)
                    self.limpiarTabla()
                    self.limpiarControles()
                except Exception as x:
                    QtWidgets.QMessageBox.critical(self, "Registrar Empleado","Ocurrio un error al registrar los datos, verifique nuevamente.", QtWidgets.QMessageBox.Ok)
                    print(x)
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Empleado", "Ya existe un Empleado ingresado con la misma Identificacion.", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.critical(self, "Registrar Empleado",self.validacion(), QtWidgets.QMessageBox.Ok)

    def detectarCboListar(self):
        serv=self.cboListar.currentText()
        self.listar(serv)

    def listar(self, estado):
        if self.cboListar.currentText()=="--Todos--":
            self.tblEmpleado.setRowCount(len(aEmpleado.listarEmpleados()))
            self.tblEmpleado.setColumnCount(9)
            self.tblEmpleado.verticalHeader().setVisible(False)
            lista=aEmpleado.listarVista()
            for fila, detalle in enumerate(lista):
                for columna, valor in enumerate(detalle):
                    item = QTableWidgetItem(str(valor))
                    self.tblEmpleado.setItem(fila, columna, item)
        else:
            self.tblEmpleado.setRowCount(len(aEmpleado.listarPorEstado(estado)))
            self.tblEmpleado.setColumnCount(9)
            self.tblEmpleado.verticalHeader().setVisible(False)
            lista=aEmpleado.listarPorEstado(estado)
            for fila, Documento in enumerate(lista):
                    for columna, valor in enumerate(Documento):
                        item = QTableWidgetItem(str(valor))
                        self.tblEmpleado.setItem(fila, columna, item)

    def modificar(self):
        if len(aEmpleado.listarEmpleados())==0:
            QtWidgets.QMessageBox.information(self, "Modificar Empleado", "No hay Empleado registrados", QtWidgets.QMessageBox.Ok)
        else:
            dni, _=QtWidgets.QInputDialog.getText(self, "Modificar Empleado", "Ingrese la Identificacion del Empleado que desea modificar") #getText es para que se abra la ventanida y te pida ingresar un dato
            
            if aEmpleado.verificarExistencia(dni):
                conexion= conexion = pyodbc.connect(DataBase.CadenaConexion())
                comando = conexion.cursor()
                comando.execute("select * from Empleado where DniEmpleado = ?", dni)
                objEmpleado=comando.fetchone()
                fechaNa = str(objEmpleado[5]).strip()  
                año, mes, dia = map(int, fechaNa.split('-'))

                self.btnRegistrar.setVisible(False)
                self.btnGuardar.setVisible(True)
                self.txtDni.setEnabled(False) 
                self.label_4.setEnabled(False)
                self.txtDni.setText(objEmpleado[0])
                self.cboEspecialidad.setCurrentIndex(int(objEmpleado[1]))
                self.cboRol.setCurrentIndex(int(objEmpleado[2]))
                self.txtNombre.setText(objEmpleado[3])
                self.txtApellido.setText(objEmpleado[4])
                self.deFechaNacimiento.setDate(QDate(año, mes, dia))
                self.txtSueldo.setText(str(objEmpleado[6])) 
                self.txtEmail.setText(objEmpleado[7])  
                comando.close()
            else:
                QtWidgets.QMessageBox.information(self, "Modificar Empleado", "El Codigo del Empleado que ingreso no se encuentra Registrado", QtWidgets.QMessageBox.Ok)
         
    def consultar(self): 
        self.limpiarControles()
        if len(aEmpleado.listarEmpleados())==0:
            QtWidgets.QMessageBox.information(self, "Consultar Empleado", "Aun No Existen Empleados.", QtWidgets.QMessageBox.Ok)
        else:
            dni, _ =QtWidgets.QInputDialog.getText(self, "Consultar Empleado", "Ingrese el DNI del Empleado que desea buscar")
            if aEmpleado.verificarExistencia(dni)==False:
                QtWidgets.QMessageBox.information(self, "Consultar Empleado", "El DNI que ingreso no existe", QtWidgets.QMessageBox.Ok)
            else:
                self.tblEmpleado.setRowCount(1)
                self.tblEmpleado.setColumnCount(9)
                self.tblEmpleado.verticalHeader().setVisible(False)
                objEmpleado=aEmpleado.consultar(dni)
                for columna, valor in enumerate(objEmpleado):
                    item = QTableWidgetItem(str(valor))
                    self.tblEmpleado.setItem(0, columna, item)
                
    def grabar(self):
            objEmpleado= Empleado(self.txtDni.text(),
                                self.obtenerIdEspecialidad(self.cboEspecialidad.currentText()),
                                self.obtenerIdRol(self.cboRol.currentText()),
                                self.txtNombre.text(),
                                self.txtApellido.text(),
                                self.deFechaNacimiento.date().toString("yyyy-MM-dd"),
                                float(self.txtSueldo.text()),
                                self.txtEmail.text(),
                                None)
            
            aEmpleado.modificar(objEmpleado)
            self.btnModificar.setVisible(True)
            self.limpiarTabla()
            self.limpiarControles()  
    
    def centrarEnPantalla(self):
        TamañoPantalla = QtWidgets.QDesktopWidget().screenGeometry()
        x = int((TamañoPantalla.width() - self.width())/2)
        y = int((TamañoPantalla.height() - self.height())/2)
        self.move(int(x+(x*0.10)), int(y+(y*0.10)))

    def cargarCboEspecialidad(self):
        conexion= conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT IdEspecialidad, Descripcion FROM Especialidad")
        especialidades= comando.fetchall()
        conexion.close()
        for especialidad in especialidades:
            id_especialidad, descripcion = especialidad
            #define que en combo box se vera la descripcion pero el valor sera el del ID
            self.cboEspecialidad.addItem(descripcion, userData=id_especialidad)
    
    def obtenerIdEspecialidad(self, descripcion):
        conexion= conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("select * from especialidad where Descripcion = ?", descripcion)
        objEsp= comando.fetchone()
        id=int(objEsp[0])
        comando.close()
        return id

    def cargarCboRol(self):
        conexion= conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT IdRol, Descripcion FROM Rol")
        Rol= comando.fetchall()
        conexion.close()
        for rol in Rol:
            id_Rol, descripcion = rol
            #define que en combo box se vera la descripcion pero el valor sera el del ID
            self.cboRol.addItem(descripcion, userData=id_Rol)

    def obtenerIdRol(self, descripcion):
        conexion= conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("select * from Rol where Descripcion = ?", descripcion)
        objRol= comando.fetchone()
        id=int(objRol[0])
        comando.close()
        return id
    
    def acomodarVentana(self): 
        centro_pantalla = QDesktopWidget().availableGeometry().center()
        desplazamiento_x = 50
        desplazamiento_y = 50
        centro_desplazado = QPoint(centro_pantalla.x() + desplazamiento_x, centro_pantalla.y() + desplazamiento_y)
        return centro_desplazado
    
    def verificarEspecialidad(self):
        self.cboRol.clear()
        self.cboRol.addItem("--Seleccionar--")
        self.cargarCboRol()
        if self.cboEspecialidad.currentText()!="UsuarioSistema":
            self.cboRol.setCurrentIndex(3)
            self.cboRol.setEnabled(False)
        else:
            self.cboRol.setCurrentIndex(0)
            self.cboRol.setEnabled(True)
            self.cboRol.removeItem(3)

    def cambiarEstado(self):
        fila=self.tblEmpleado.selectedItems()
        if fila:
            indiceFila=fila[0].row()
            nombre = self.tblEmpleado.item(indiceFila, 3).text()
            respuesta = QMessageBox.question(self, "Estado Empleado", "¿Desea Cambiar el estado del Empleado de nombre: "+nombre+"?", QMessageBox.Yes | QMessageBox.No)
            if (respuesta == QMessageBox.Yes):
                dni=self.tblEmpleado.item(indiceFila, 0).text()
                aEmpleado.cambiarEstadoEmpleado(dni)
                self.limpiarTabla()
                self.listar(self.cboListar.currentText())
                QtWidgets.QMessageBox.information(self, "Estado Empleado", "Estado Cambiado Correctamente.", QtWidgets.QMessageBox.Ok)
            else:
                self.listar(self.cboListar.currentText())
        
    def cerrarVentana(self):
        self.close()

