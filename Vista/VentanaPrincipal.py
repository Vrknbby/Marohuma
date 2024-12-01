import sys 
from PyQt5 import QtCore 
from PyQt5.QtCore import QPropertyAnimation 
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget,QDesktopWidget
from PyQt5 import QtWidgets, uic,QtCore
from Vista.VentanaRegistroClientes import * 
from Vista.VentanaRegistroEmpleados import *
from Controlador.ArregloEmpleado import *
from Controlador.ArregloEmpleado import empleado
from Vista.VentanaRegistroDocumentos import *
from Vista.VentanaRegistroServicios import *
from Vista.VentanaRegistroProveedores import *
from Vista.VentanaRegistroPedidos import *
from Vista.VentanaDetalleCompra import *
from Vista.VentanaRegistroSalidas import *
from Vista.VentanaInventario import *
from Vista.VentanaMovimientos import *
aEmpleado = ArregloEmpleado()
class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self,parent = None):     
        super(VentanaPrincipal,self).__init__(parent)
        uic.loadUi("UI/VENTANA-PRINCIPAL.ui", self) 
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.btnMinimizar.clicked.connect(self.showMinimized)
        self.btnCerrar.clicked.connect(sys.exit)
        self.btnMenu.clicked.connect(self.mostrarMenu)
        self.btnRegistro.clicked.connect(self.subMenuRegistro)
        self.btnClientes.clicked.connect(self.abrirVentanaRegistroCliente)
        self.btnREmpleados.clicked.connect(self.abrirVentanaRegistroEmpleado)
        self.btnDocumentos.clicked.connect(self.abrirVentanaDocumentos)
        self.btnServicio.clicked.connect(self.abrirVentanaServicios)
        self.btnTienda.clicked.connect(self.abrirVentanaProveedor)
        self.btnPedido.clicked.connect(self.abrirVentanaPedido)
        self.btnDetallePedido.clicked.connect(self.abrirVentanaDetalleCompra)
        self.btnSalidas.clicked.connect(self.abrirVentanaSalidas)
        self.btnInventario.clicked.connect(self.abrirVentanaInventario)
        self.btnMovimientos.clicked.connect(self.abrirVentanaMovimientos)
        self.txtRolEmpl.setText(str(empleado[0][2]))
        self.txtNombre.setText(str(empleado[0][3])+" "+str(empleado[0][4]))
        self.detectarRol()
        self.center()
        self.show()
        
    def abrirVentanaRegistroCliente(self):
        vClientes = VentanaRegistroClientes(self)
        vClientes.show()  
    
    def abrirVentanaMovimientos(self):
        vMovimientos = VentanaMovimientos(self)
        vMovimientos.show() 
    
    def abrirVentanaRegistroEmpleado(self):
        vEmpleado = VentanaRegistroEmpleado(self)
        vEmpleado.show()    
    
    def abrirVentanaDocumentos(self):
        vDocumentos = VentanaRegistroDocumentos(self)
        vDocumentos.show()
    
    def abrirVentanaServicios(self):
        vServicios = VentanaRegistroServicios(self)
        vServicios.show()    

    def abrirVentanaProveedor(self):
        vProveedores= VentanaRegistroProveedores(self)
        vProveedores.show()

    def abrirVentanaPedido(self):
        vPedido= VentanaRegistroPedido(self)
        vPedido.show()

    def abrirVentanaDetalleCompra(self):
        vDetalle=VentanaDetalleCompra(self)
        vDetalle.show()

    def abrirVentanaSalidas(self):
        vSalida=VentanaRegistroSalidas(self)
        vSalida.show()
    
    def abrirVentanaInventario(self):
        vInventario=VentanaInventario(self)
        vInventario.show()

    def detectarRol(self):
        if self.txtRolEmpl.text()!= "Administrador":
            self.btnDocumentos.setEnabled(False)
            self.btnClientes.setEnabled(False)
            self.btnREmpleados.setEnabled(False)
            self.btnServicio.setEnabled(False)
            


    def mostrarMenu(self):
        if self.frmOpciones.isVisible():
            self.animacion = QPropertyAnimation(self.frmOpciones, b"minimumWidth")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(self.frmOpciones.minimumWidth())
            self.animacion.setEndValue(0)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.finished.connect(self.frmOpciones.hide)
            self.animacion.start()
            self.frmRegistro.hide()
        else:
            self.frmOpciones.show()
            self.animacion = QPropertyAnimation(self.frmOpciones, b"minimumWidth")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(0)
            self.animacion.setEndValue(200)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.frmOpciones.show()
            self.animacion.start()
               
    def subMenuRegistro(self):
         if self.frmRegistro.isVisible():
            self.animacion = QPropertyAnimation(self.frmRegistro, b"minimumWidth")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(self.frmOpciones.minimumWidth())
            self.animacion.setEndValue(0)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.finished.connect(self.frmRegistro.hide)
            self.animacion.start()
         else:
            self.frmRegistro.show()
            self.animacion = QPropertyAnimation(self.frmRegistro, b"minimumWidth")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(self.frmOpciones.minimumWidth())
            self.animacion.setEndValue(400)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.frmRegistro.show()
            self.animacion.start()
        

    def center(self):
        # Obtener la geometría de la pantalla
        TamañoPantalla = QtWidgets.QDesktopWidget().screenGeometry()
        # Calcular la posición central de la ventana
        x = int((TamañoPantalla.width() - self.width())/2)
        y = int((TamañoPantalla.height() - self.height())/2)
        # Mover la ventana al centro
        self.move(x, y)   

        
        


        






















