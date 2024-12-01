from PyQt5 import QtWidgets, uic,QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import webbrowser
from PyQt5.QtCore import Qt
import sys
import os 
import datetime
import time
import pyodbc #Basedatos, Se tiene q Instalar
from Controlador.ConexionDB import *
from UI.Imagenes import QT_imagenes
from Vista.VentanaPrincipal import VentanaPrincipal
from Vista.RecuperarPassword import RecuperarPassword
from Controlador.ArregloEmpleado import *
from Controlador.ArregloEmpleado import empleado

aEmpleado= ArregloEmpleado()
DataBase=ConexionDB()
class Login(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        #self.setWindowIcon(QtGui.QIcon("UI\Imagenes\Icono.ico"))
        uic.loadUi("UI\Login.ui", self)
        self.contador=3
        self.btnIniciar.clicked.connect(self.iniciarSesion)
        self.btnRecuperar.clicked.connect(self.abrirVentanaRecuperacion)

        #Abrir Url
        self.setObjectName("Form")
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.btnMinimizar.clicked.connect(self.showMinimized)
        self.btnCerrar.clicked.connect(sys.exit)
        
        self.Facebook.clicked.connect(self.abrirFacebook)
        self.Instagram.clicked.connect(self.abrirInstagram)
        self.WhatsApp.clicked.connect(self.abrirWhatsApp)
        self.Web.clicked.connect(self.abrirWeb)
        self.btnIniciar.setVisible(True)
        self.centrarEnPantalla()
        self.show()

    
    def iniciarSesion(self):
        if self.verificarBloqueo():
            try:
                login = False
                conexion = pyodbc.connect(DataBase.CadenaConexion())
                comando = conexion.cursor()
                comando.execute("select * from Usuario")
                objUsuario=comando.fetchone()
                if self.contador>0:
                    while objUsuario:
                        if objUsuario[2]==self.txtUsuario.text().upper().strip():
                            if objUsuario[3]==self.txtPassword.text():
                                rol = DataBase.identificarRol(str(objUsuario[1]))
                                conexion.close()
                                aEmpleado.cargar(objUsuario[1])
                                estado= str(empleado[0][-1])
                                especialidad=str(empleado[0][1])
                                if especialidad == "UsuarioSistema":
                                    if estado=="Activo":
                                        self.abrirVentanaPrincipal()
                                        login = True
                                    else:
                                        QtWidgets.QMessageBox.critical(self, "Error de Acceso", "El usuario con el que intenta acceder se encuentra Inactivo.\n\nPor favor, póngase en contacto con el administrador del sistema para recibir asistencia.", QtWidgets.QMessageBox.Ok)
                                        empleado.clear()
                                else:
                                    empleado.clear()
                                    QtWidgets.QMessageBox.critical(self, "Error de Acceso", "El usuario con el que ingreso no tiene permitido el acceso al Sistema.", QtWidgets.QMessageBox.Ok)
                            else:
                                QtWidgets.QMessageBox.critical(self, "Error de Acceso", "Contraseña Incorrecta.\nADVERTENCIA:\nLe quedan "+str(self.contador)+" Intentos", QtWidgets.QMessageBox.Ok)
                                conexion.close()
                                empleado.clear()
                                self.contador-=1
                        objUsuario=comando.fetchone()
                    if login== False:
                        QtWidgets.QMessageBox.critical(self, "Error de Acceso", "El usuario que ingreso no Existe", QtWidgets.QMessageBox.Ok)
                        conexion.close()
                else:
                    QtWidgets.QMessageBox.critical(self, "Error de Acceso", "Se a bloqueado su usuario Temporalmente.", QtWidgets.QMessageBox.Ok)
                    self.Bloquear(2)
                    self.txtUsuario.clear()
                    self.txtPassword.clear()
                    self.contador=3
            except pyodbc.Error as e:
                print(e)
        else:
            QtWidgets.QMessageBox.critical(self, "Error de Acceso", "Usted esta bloqueado hasta las "+ self.LeerHoraBloqueo()+" horas.", QtWidgets.QMessageBox.Ok)



        
    def keyPressEvent(self, event):   
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:   
            self.iniciarSesion()
        if event.key()== Qt.Key_Escape:
            sys.exit()

    def abrirFacebook(self):
        url = 'https://www.facebook.com/marohuma'
        webbrowser.open(url)
    
    def abrirInstagram(self):
        url = 'https://www.instagram.com/'
        webbrowser.open(url)
        
    def abrirWhatsApp(self):
        url = 'https://web.whatsapp.com/'
        webbrowser.open(url)
    
    def abrirWeb(self):
        url = 'https://www.google.com.pe/?hl=es'
        webbrowser.open(url)

    def abrirVentanaPrincipal(self):
        self.close() 
        self.vPrincipal = VentanaPrincipal()  
        self.vPrincipal.show()


    def centrarEnPantalla(self):
        # Obtener la geometría de la pantalla
        TamañoPantalla = QtWidgets.QDesktopWidget().screenGeometry()
        # Calcular la posición central de la ventana
        x = int((TamañoPantalla.width() - self.width())/2)
        y = int((TamañoPantalla.height() - self.height())/2)
        # Mover la ventana al centro
        self.move(x, y)
    
    def abrirVentanaRecuperacion(self):
        self.vRecuperacion = RecuperarPassword()
        #La variable VentanaCerrada esta a la espera para Mandar una señal cuando la ventana de recuperar Password se cierre
        self.vRecuperacion.AccionCierre.connect(self.ActivarVentanaLogin)
        self.vRecuperacion.show()
        self.setVisible(False)
        
    def ActivarVentanaLogin(self):
        self.setVisible(True)
    


    def verificarBloqueo(self):
    #solo para verificar si el archivo esta vacio
        if os.path.getsize("Modelo\DatosBloqueo.txt") == 0:
            return True
        
        with open("Modelo\DatosBloqueo.txt", "r", encoding="utf=8") as notaBloqueo:
            for linea in notaBloqueo.readlines():
                columna=linea.split(",")
                hora=columna[0]
                fecha= columna[1].strip()

                fechaAct=datetime.date.today()
                formato= time.localtime()
                horaActual= time.strftime("%H:%M",formato)
                TerminacionBloqueo=time.strptime((hora.strip()),"%H:%M")
                HoraActualEstructurado=time.strptime(horaActual, "%H:%M")
                if HoraActualEstructurado>=TerminacionBloqueo or str(fechaAct) != str(fecha):
                    return True
                else:
                    return False
    
    def calcularFinBloqueo(self, horaactual, duracion):
        columna = str(horaactual).split(":")
        horas = columna[0]
        minutos = columna[1].strip()
        minutos = int(minutos)
        duracion = int(duracion)
        NuevosMinutos = minutos + duracion
        if NuevosMinutos < 10:
            NuevosMinutosSTR = "0" + str(NuevosMinutos)
        else:
            NuevosMinutosSTR = str(NuevosMinutos)

        if NuevosMinutos >= 60:
            NuevasHoras = int(horas) + NuevosMinutos // 60 #Divicion para calcular La cantidad de horas que debe aumentar
            NuevosMinutos = NuevosMinutos % 60
            if NuevosMinutos < 10:
                NuevosMinutosSTR = "0" + str(NuevosMinutos)
            else:
                NuevosMinutosSTR = str(NuevosMinutos)
            if NuevasHoras == 24:
                NuevasHoras = "00"
            horas = str(NuevasHoras)
        return horas + ":" + NuevosMinutosSTR

    def Bloquear(self,duracion):
        with open("Modelo\DatosBloqueo.txt", "w+", encoding="utf=8") as notaBloqueo:
            formato= time.localtime()
            inicioBloqueo=time.strftime("%H:%M",formato)
            finBloqueo= self.calcularFinBloqueo(inicioBloqueo,duracion)
            fechaActual= datetime.date.today()

            notaBloqueo.write(str(finBloqueo)+",")
            notaBloqueo.write(str(fechaActual)+"\n")
            

    def LeerHoraBloqueo(self):
        with open("Modelo\DatosBloqueo.txt", "r", encoding="utf=8") as notaBloqueo:
            for linea in notaBloqueo.readlines():
                columna=linea.split(",")
                hora=columna[0]
                return str(hora.strip())