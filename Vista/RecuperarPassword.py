from PyQt5 import QtWidgets, uic,QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import Qt
import sys
import pyodbc
import random as rd
import smtplib
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtCore import QPropertyAnimation
from Controlador.ConexionDB import *
from Controlador.ArregloUsuario import *

aRecuperacion= ArregloUsuario()
DataBase=ConexionDB()
class RecuperarPassword (QtWidgets.QMainWindow):
    AccionCierre = pyqtSignal()
    def __init__ (self, parent = None):
        super(RecuperarPassword,self).__init__(parent)
        #self.setWindowIcon(QtGui.QIcon("UI\Imagenes\Icono.ico"))
        uic.loadUi("UI/RecuperacionPassword.ui", self)
        self.centrarEnPantalla()
        
        #Parametros de temporizador
        #inicializa QTimer
        self.temporizador=QTimer()
        #Define cada cuantos milisegundos se emitira una señal
        self.temporizador.start(1000)
        #variable para definir el tiempo
        self.tiempo= 16

        
        self.btnAceptar.clicked.connect(self.confirmar)
        self.btnCerrar.clicked.connect(self.close)
        self.btnEnviar.clicked.connect(self.buscarUsuario)
        self.btnGuardar.clicked.connect(self.guardar)
        self.correoDestino=""
        self.tipoUsuario=""
        self.codigo=""
        self.idUser=0

        #botones
        self.label_10.setVisible(False)
        self.txtCodigo.setVisible(False)
        self.btnAceptar.setVisible(False)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def buscarUsuario(self):
        try:
            busqueda = False
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Usuario")
            objUsuario=comando.fetchone()
            while objUsuario:
                if objUsuario[2]==self.txtUsuario.text().strip().upper():
                    busqueda = True
                    self.correoDestino = DataBase.identificarCorreo(str(objUsuario[1]))
                    self.tipoUsuario= DataBase.identificarRol(str(objUsuario[1]))
                    self.idUser = objUsuario[0]
                    self.mandarCorreo(str(self.correoDestino))
                    self.MostrarBotones()
                    conexion.close()
                objUsuario=comando.fetchone()
            if busqueda== False:
                QtWidgets.QMessageBox.critical(self, "ERROR", "El usuario o contraseña que ingreso son incorrectos.", QtWidgets.QMessageBox.Ok)
                conexion.close()
        except pyodbc.Error as e:
            print(e)    


    def mandarCorreo(self,destino):
        cod = self.generarCodigo()
        self.codigo = cod
        mensaje = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"+"    --Tu codigo de Recuperacion es--   \n"+"- - - - - - - - - - - - -"+cod+"- - - - - - - - - - - - -"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("proyectomarohuma@gmail.com", "b n n w z y v o r p n t s e g h")
        server.sendmail("proyectomarohuma@gmail.com", str(destino), mensaje)
        server.quit()

    def generarCodigo(self):
        caracteres = "1234567890"
        codigo = "".join(rd.choice(caracteres)for _ in range(6))
        return codigo
    
    def modificarPassword(self):
        if self.txtNewPassword.text()=="" or self.txtConfirmarPassword.text()=="":
            QtWidgets.QMessageBox.critical(self, "ERROR", "No puede dejar este campo Vacio.", QtWidgets.QMessageBox.Ok)
        elif self.txtNewPassword.text()!=self.txtConfirmarPassword.text():
            QtWidgets.QMessageBox.critical(self, "ERROR", "Las claves no coinciden", QtWidgets.QMessageBox.Ok)
        else:
            try: 
                newPass=self.txtNewPassword.text()
                conexion= conexion = pyodbc.connect(DataBase.CadenaConexion())
                comando = conexion.cursor()
                comando.execute("select * from Usuario where IdUsuario="+str(self.idUser))
                objUsuario=comando.fetchone()
                comando.execute("update Usuario set DniEmpleado = ?, NombreUsuario = ?, Contraseña = ? where IdUsuario = ?",
                            (objUsuario[1], objUsuario[2], newPass, objUsuario[0]))
                conexion.commit()#confirma los cambios en la base de datos
                self.close()
                QtWidgets.QMessageBox.information(self, "Marohuma", "Contraseña Cambiada Correctamente", QtWidgets.QMessageBox.Ok)
            except pyodbc.Error as e:
                print(e) 

    def confirmar(self):
        if self.txtCodigo.text()==self.codigo:
            self.mover_menu()
            
        else:
            QtWidgets.QMessageBox.critical(self, "ERROR", "El Codigo que ingreso es Incorrecto", QtWidgets.QMessageBox.Ok)

    def mover_menu(self):
        if True:
            height = self.FrameSuperior.height()
            normal = 0
            if height == 450:
                esconder = 0
            else:
                esconder = normal
            self.animacion = QPropertyAnimation(self.FrameSuperior, b"minimumHeight")
            self.animacion.setDuration(430)
            self.animacion.setStartValue(height)
            self.animacion.setEndValue(esconder)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
    
    def guardar(self):
        self.modificarPassword()
    
    def MostrarBotones(self):
        self.label_10.setVisible(True)
        self.txtCodigo.setVisible(True)
        self.btnAceptar.setVisible(True)
        self.btnEnviar.setEnabled(False)
        self.temporizador.timeout.connect(self.EmpezarContador)
    
    def EmpezarContador(self): 
        self.tiempo-=1
        tiempo=str(self.tiempo)
        self.ActualizarMensaje(tiempo)
        #cuando el tiempo llega a 0 el temporizador se detiene, se manda el mensaje de activacion y se reinicia el temporizador
        if self.tiempo == 0:
            self.temporizador.stop()
            self.btnEnviar.setEnabled(True)
            self.lbMensaje.setText("")
            self.ReiniciarTemporizador()
        
    def ActualizarMensaje(self,tiempo): 
        self.lbMensaje.setText(f"Espere {tiempo} segundos para volver a enviar el Codigo...")
        
    
    def ReiniciarTemporizador(self):
        self.tiempo=16
        self.temporizador.timeout.disconnect()
        self.temporizador.start(1000)
    
    def closeEvent(self, event):
        self.AccionCierre.emit()
        super().closeEvent(event)
    
    def centrarEnPantalla(self):
        TamañoPantalla = QtWidgets.QDesktopWidget().screenGeometry()
        x = int((TamañoPantalla.width() - self.width())/2)
        y = int((TamañoPantalla.height() - self.height())/2)
        self.move(int(x+(x*0.10)), int(y+(y*0.10)))