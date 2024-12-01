import sys 
import re
import datetime
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5 import QtCore 
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QPropertyAnimation 
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget,QDesktopWidget
from PyQt5.uic import loadUi
from Controlador.ConexionDB import *
from Controlador.ArregloDetalleCompra import *
from Controlador.ArregloPedido import *
from Controlador.ArregloMaterial import *
from Controlador.ArregloMovimientoMaterial import *
from Vista.VentanaRegistroMaterial import *
from Controlador.ArregloEmpleado import empleado

aMovimientoMat = ArregloMovimientoMaterial()
aMaterial=ArregloMaterial()
aPedido = ArregloPedido()
aDetalleCompra=ArregloDetalleCompra()
DataBase=ConexionDB()

class VentanaDetalleCompra(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaDetalleCompra,self).__init__(parent)
        loadUi("UI/DETALLE-COMPRA.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.IdMaterial.setVisible(False)
        self.ocultarColumnas()
        self.cargarServicios()
        self.listar("--Todos--")
        self.rutaSalida=""
        self.rutaArch=""
        self.cboListar.currentIndexChanged.connect(self.detectarCboListar)
        self.txtPrecioUnitario.setValidator(QIntValidator())
        self.btnCerrar.clicked.connect(self.cerrarVentana)
        self.listPedidoCompra.setVisible(False)
        self.txtPedidoCompra.textChanged.connect(self.cargarSugerencias)
        self.listPedidoCompra.itemClicked.connect(self.sugerenciaClick)
        self.listSugerenciaMaterial.setVisible(False)
        self.txtIdMaterial.textChanged.connect(self.cargarSugerenciasMaterial)
        self.listSugerenciaMaterial.itemClicked.connect(self.sugerenciaClickMaterial)
        self.tblDetalleCompra.cellDoubleClicked.connect(self.cambiarEstado)
        self.btnRegistrarMaterial.clicked.connect(self.abrirVentanaRegistroMaterial)
        self.btnInsertar.clicked.connect(self.insertar)
        self.cboServicio.currentIndexChanged.connect(self.limpiarProducto)
        self.btnSubir.clicked.connect(self.subirArchivo)
        self.tblDetalleCompra.setEditTriggers(QAbstractItemView.NoEditTriggers)
    def validacion(self):
        if self.rutaArch=="":
            return "Olvido subir la Factura"
        elif self.cboServicio.currentText() == "--Seleccionar--":
            return "No seleccionó el Servicio"
        elif self.txtPedidoCompra.text().strip() == "":
            return "No ingresó el código de pedido"
        elif not self.verificarPedido():
            return "El código de pedido que ingresó no existe"
        elif self.IdMaterial.text().strip() == "":
            return "El Material que ingresó no existe"
        elif int(self.sbCantidad.text()) < 1 or self.sbCantidad.text().strip() == "":
            return "Ingrese correctamente la cantidad"
        elif not re.match(r'^\d+(\.\d+)?$', self.txtPrecioUnitario.text()):
            return "Ingrese correctamente el Precio por Unidad (debe ser un número válido)"
        elif float(self.txtPrecioUnitario.text()) < 1:
            return "Ingrese correctamente el Precio por Unidad (debe ser mayor o igual a 1)"
        elif self.cboMetodoPago.currentText() == "--Seleccionar--":
            return "No seleccionó un método de Pago"
        else:
            return 0

    def limpiarProducto(self):
        self.txtIdMaterial.clear()
        self.IdMaterial.clear()

    def reiniciar(self):
        self.rutaSalida=""
        self.rutaArch=""
        self.listar(self.cboListar.currentText())
        self.btnInsertar.setText("Insertar")
        self.cboServicio.setCurrentIndex(0)
        self.txtPedidoCompra.clear()
        self.txtIdMaterial.clear()
        self.IdMaterial.clear()
        self.sbCantidad.setValue(0)
        self.txtPrecioUnitario.clear()
        self.cboMetodoPago.setCurrentIndex(0)


    def limpiarTabla(self):
        self.tblDetalleCompra.clearContents()
        self.tblDetalleCompra.setRowCount(0)  

    def insertar(self):
        if self.validacion() == 0:
            objDetalle = DetalleCompra(
                None,
                self.cboServicio.currentText(),
                self.txtPedidoCompra.text(),
                self.IdMaterial.text(),
                self.sbCantidad.value(),
                float(self.txtPrecioUnitario.text()),
                float(self.calcularPrecioParcial()),
                self.cboMetodoPago.currentText(),
                "Espera"
            )   
            if aDetalleCompra.insertar(objDetalle):
                aPedido.actualizarDetalleRegistrado(objDetalle.getNumPedido())
                self.definirSalida(self.rutaArch, objDetalle)
                if self.rutaArch:
                    try:
                        shutil.copy(self.rutaArch,self.rutaSalida)
                        self.reiniciar()
                    except IOError as e:
                        print(e)
                self.limpiarTabla()
                self.reiniciar()
            else:
                QtWidgets.QMessageBox.critical(self, "Error en Detalle de Compra", "El número de pedido ingresado ya ha sido registrado. Por favor, ingrese un número de pedido disponible.", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.critical(self, "Registrar Detalle de Compra", self.validacion(), QtWidgets.QMessageBox.Ok)


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
        comando.execute("SELECT IdMaterial, Nombre, IdServicio FROM Material")
        Materiales = comando.fetchall()

        sugerencias = []
        for material in Materiales:
            Idmaterial, NombreMaterial, IdServicio = material
            if servicio == IdServicio:
                if texto.upper() in str(NombreMaterial).upper():
                    sugerencias.append(str(NombreMaterial))
                if self.txtIdMaterial.text().upper().strip() == NombreMaterial.upper():
                    self.IdMaterial.setText(str(Idmaterial))
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


    def cargarSugerencias(self):
        texto=self.txtPedidoCompra.text()
        conexion= pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT NumPedido FROM Pedido WHERE DetalleRegistrado = 0")
        Pedidos= comando.fetchall()
        Ids = [str(pedido[0]) for pedido in Pedidos]
        sugerencias = []
        for ruc in Ids:
            if texto in ruc:
                sugerencias.append(ruc)
        self.listPedidoCompra.clear()
        self.listPedidoCompra.addItems(sugerencias)
        if texto.strip()=="":
            self.listPedidoCompra.clear()
            sugerencias=[]
        
        cantidadSug = len(sugerencias)
        alturaItem = 13  
        espacio = 0  
        calculoAltura = cantidadSug * (alturaItem + espacio)
        
        if calculoAltura == 13:
            self.listPedidoCompra.setFixedHeight(30)
        else:
            self.listPedidoCompra.setFixedHeight(calculoAltura*2)
        self.listPedidoCompra.setSpacing(0)
        self.listPedidoCompra.setVisible(bool(sugerencias))

    def sugerenciaClick(self, item):
        self.txtPedidoCompra.setText(item.text())
        self.listPedidoCompra.setVisible(False)

    def mousePressEvent(self, event):
        if not self.listPedidoCompra.geometry().contains(event.pos()):
            self.listPedidoCompra.setVisible(False)
        if not self.listSugerenciaMaterial.geometry().contains(event.pos()):
            self.listSugerenciaMaterial.setVisible(False)

    def calcularPrecioParcial(self):
        parcial= float(self.sbCantidad.text())* float(self.txtPrecioUnitario.text())
        return parcial

    def verificarPedido(self):
        txtPedido=self.txtPedidoCompra.text()
        listPedidos=aPedido.listar()
        for pedido in listPedidos:
            if txtPedido==pedido[0]:
                return True
        return False

    def abrirVentanaRegistroMaterial(self):
        vMaterial=VentanaRegistroMaterial(self)
        vMaterial.show()
    
    def conseguirDniUsuario(self, dniEmpl):
        conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT * FROM Usuario WHERE DniEmpleado = ?", dniEmpl)
        usuario = comando.fetchone()
        comando.close()
        return str(usuario[0])

    def conseguirFrenteMaterial(self, idMat):
        conexion = pyodbc.connect(DataBase.CadenaConexion())
        comando = conexion.cursor()
        comando.execute("SELECT * FROM Material WHERE IdMaterial = ?", idMat)
        Material = comando.fetchone()
        comando.close()
        return str(Material[6])

    def cancelar(self):
        self.reiniciar()
        self.limpiarTabla()


    def detectarCboListar(self):
        serv=self.cboListar.currentText()
        self.listar(serv)

    def listar(self, servicio):
        if self.cboListar.currentText()=="--Todos--":
            self.tblDetalleCompra.setRowCount(len(aDetalleCompra.listarVista()))
            self.tblDetalleCompra.setColumnCount(9)
            self.tblDetalleCompra.verticalHeader().setVisible(False)
            lista=aDetalleCompra.listarVista()
            for fila, detalle in enumerate(lista):
                for columna, valor in enumerate(detalle):
                    item = QTableWidgetItem(str(valor))
                    self.tblDetalleCompra.setItem(fila, columna, item)

        else:
            self.tblDetalleCompra.setRowCount(len(aDetalleCompra.listarPor(servicio)))
            self.tblDetalleCompra.setColumnCount(9)
            self.tblDetalleCompra.verticalHeader().setVisible(False)
            lista=aDetalleCompra.listarPor(servicio)
            for fila, Documento in enumerate(lista):
                    for columna, valor in enumerate(Documento):
                        item = QTableWidgetItem(str(valor))
                        self.tblDetalleCompra.setItem(fila, columna, item)

    def ocultarColumnas(self):
        self.tblDetalleCompra.setColumnHidden(0, True)
        self.tblDetalleCompra.setColumnHidden(5, True)
        self.tblDetalleCompra.setColumnHidden(7, True)

    def cambiarEstado(self):
        fechaHoy = datetime.datetime.now().date()
        formatoCorrecto=fechaHoy.strftime('%Y-%m-%d')
        fila=self.tblDetalleCompra.selectedItems()
        if fila:
            indiceFila=fila[0].row()
            respuesta = QMessageBox.question(self, "Estado de Compra", "¿Desea Cambiar el estado de la Compra?", QMessageBox.Yes | QMessageBox.No)
            if (respuesta == QMessageBox.Yes):
                id=self.tblDetalleCompra.item(indiceFila, 0).text()
                detalle=aDetalleCompra.consultar(id)
                objDetalle = DetalleCompra(
                int(detalle[0]),
                str(detalle[1]),
                str(detalle[2]),
                int(detalle[3]),
                int(detalle[4]),
                float(detalle[5]),
                float(detalle[6]),
                str(detalle[7]),
                str(detalle[8])
                )
                objMovimiento=MovimientoMaterial(
                    None,
                    self.conseguirDniUsuario(empleado[0][0]),
                    objDetalle.getIdMaterial(),
                    empleado[0][0],
                    objDetalle.getIdServicio(),
                    "Entrada",
                    self.conseguirFrenteMaterial(objDetalle.getIdMaterial()),
                    objDetalle.getCantidad(),
                    formatoCorrecto
                )    
                if aDetalleCompra.cambiaEstado(id):
                    aMovimientoMat.insertar(objMovimiento)
                    aMaterial.aumentarStock(objDetalle.getIdMaterial(),objDetalle.getCantidad())
                    self.limpiarTabla()
                    self.listar(self.cboListar.currentText())
                    QtWidgets.QMessageBox.information(self, "Estado Servicio", "Estado Cambiado Correctamente.", QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.information(self, "Estado Servicio", "No puede cambiar el estado del pedido porque ya fue registrado como recibido.", QtWidgets.QMessageBox.Ok)
            else:
                self.listar(self.cboListar.currentText())

    def subirArchivo(self):
        self.rutaArch,_ = QFileDialog.getOpenFileName(self,"Seleccione la Factura","","Archivos PDF (*.pdf)")

    def definirSalida(self, rutaFac, objDetalle):
        columna = str(rutaFac).split("/")
        nombre= columna[-1]
        if not (os.path.exists("PROYECTOS/"+objDetalle.getIdServicio()+"/Facturas/")):
            os.mkdir("PROYECTOS/"+objDetalle.getIdServicio()+"/Facturas/")
        self.rutaSalida="PROYECTOS/"+objDetalle.getIdServicio()+"/Facturas/"+nombre

    def cerrarVentana(self):
        self.close()