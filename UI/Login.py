# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, Imagenes

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, -10, 621, 601))
        self.widget.setStyleSheet("QPushButton#Ingresar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#Ingresar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150,123,111,219), stop:1 rgba(85,81,84,226));\n"
"\n"
"}\n"
"\n"
"QPushButton#Ingresar:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton#cambio{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#cambio:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150,123,111,219), stop:1 rgba(85,81,84,226));\n"
"\n"
"}\n"
"\n"
"QPushButton#cambio:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton#Facebook{\n"
"    background-color: rgba(0,0,0,0);\n"
"    color:rgba(85,98,112,255);\n"
"}\n"
"\n"
"QPushButton#Facebook:hover{\n"
"    color:rgba(131,96,53,255);\n"
"}\n"
"\n"
"QPushButton#Facebook:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91,88,53,255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton#Instagram{\n"
"    background-color: rgba(0,0,0,0);\n"
"    color:rgba(85,98,112,255);\n"
"}\n"
"\n"
"QPushButton#Instagram:hover{\n"
"    color:rgba(131,96,53,255);\n"
"}\n"
"\n"
"QPushButton#Instagram:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91,88,53,255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton#WhatsApp{\n"
"    background-color: rgba(0,0,0,0);\n"
"    color:rgba(85,98,112,255);\n"
"}\n"
"\n"
"QPushButton#WhatsApp:hover{\n"
"    color:rgba(131,96,53,255);\n"
"}\n"
"\n"
"QPushButton#WhatsApp:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91,88,53,255);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#Web{\n"
"    background-color: rgba(0,0,0,0);\n"
"    color:rgba(85,98,112,255);\n"
"}\n"
"\n"
"QPushButton#Web:hover{\n"
"    color:rgba(131,96,53,255);\n"
"}\n"
"\n"
"QPushButton#Web:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91,88,53,255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(19, 30, 301, 521))
        self.label.setStyleSheet("border-image: url(:/imagenes/colegio.jpg);\n"
"border-top-left-radius:50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(-12, 30, 321, 541))
        self.label_2.setStyleSheet("border-top-left-radius:50px;\n"
"border-image: url(:/newPrefix/marohuma.jpg);")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 321, 541))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(228, 222, 211);\n"
"border-bottom-right-radius:50px;\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 480, 201, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Facebook = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Facebook.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.Facebook.setFont(font)
        self.Facebook.setObjectName("Facebook")
        self.horizontalLayout.addWidget(self.Facebook)
        self.Instagram = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Instagram.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.Instagram.setFont(font)
        self.Instagram.setObjectName("Instagram")
        self.horizontalLayout.addWidget(self.Instagram)
        self.WhatsApp = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.WhatsApp.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.WhatsApp.setFont(font)
        self.WhatsApp.setObjectName("WhatsApp")
        self.horizontalLayout.addWidget(self.WhatsApp)
        self.Web = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Web.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.Web.setFont(font)
        self.Web.setObjectName("Web")
        self.horizontalLayout.addWidget(self.Web)
        self.IniciarSesion = QtWidgets.QWidget(self.widget)
        self.IniciarSesion.setGeometry(QtCore.QRect(270, 90, 300, 400))
        self.IniciarSesion.setStyleSheet("QPushButton#iniciar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(239, 161, 20), stop:1  rgba(166, 108, 12));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#iniciar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(252, 204, 124), stop:1  rgba(124, 110, 89));\n"
"}\n"
"\n"
"QPushButton#iniciar:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"")
        self.IniciarSesion.setObjectName("IniciarSesion")
        self.label_4 = QtWidgets.QLabel(self.IniciarSesion)
        self.label_4.setGeometry(QtCore.QRect(40, 50, 231, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0,0,0,200);\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.IniciarSesion)
        self.label_5.setGeometry(QtCore.QRect(45, 270, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("line-height: 0.5;\n"
"color:rgba(0,0,0,210)")
        self.label_5.setObjectName("label_5")
        self.txtPassword = QtWidgets.QLineEdit(self.IniciarSesion)
        self.txtPassword.setGeometry(QtCore.QRect(40, 180, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPassword.setFont(font)
        self.txtPassword.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(166, 108, 12);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.txtUsuario = QtWidgets.QLineEdit(self.IniciarSesion)
        self.txtUsuario.setGeometry(QtCore.QRect(40, 110, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtUsuario.setFont(font)
        self.txtUsuario.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(166, 108, 12);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.txtUsuario.setObjectName("txtUsuario")
        self.btnIniciar = QtWidgets.QPushButton(self.IniciarSesion)
        self.btnIniciar.setGeometry(QtCore.QRect(40, 230, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnIniciar.setFont(font)
        self.btnIniciar.setObjectName("btnIniciar")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(520, 30, 70, 40))
        self.label_9.setStyleSheet("background-color:rgba(0,0,0,100);\n"
"border-radius:2px;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalWidget_2 = QtWidgets.QWidget(self.widget)
        self.horizontalWidget_2.setGeometry(QtCore.QRect(520, 30, 70, 40))
        self.horizontalWidget_2.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0,0,0,0);\n"
"    color:rgb(255,255,255);\n"
"    border-radius:1px;\n"
"    font-size:18px;\n"
"    font-family:dripicons-v2;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(49,48,53)\n"
"}\n"
"\n"
"QPushButton#cerrar:hover{\n"
"    background-color:rgb(232,17,25)\n"
"}\n"
"\n"
"QpushButton:pressed{\n"
"    padding-top:5px;\n"
"     padding-left:5px;\n"
"}\n"
"")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnMinimizar = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btnMinimizar.setMinimumSize(QtCore.QSize(30, 30))
        self.btnMinimizar.setMaximumSize(QtCore.QSize(30, 30))
        self.btnMinimizar.setObjectName("btnMinimizar")
        self.horizontalLayout_2.addWidget(self.btnMinimizar)
        self.btnCerrar = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btnCerrar.setMinimumSize(QtCore.QSize(30, 30))
        self.btnCerrar.setMaximumSize(QtCore.QSize(30, 30))
        self.btnCerrar.setObjectName("btnCerrar")
        self.horizontalLayout_2.addWidget(self.btnCerrar)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(0, 30, 271, 131))
        self.label_12.setStyleSheet("background-color: rgba(255, 255, 255, 128);\n"
"border-top-left-radius:30px;\n"
"\n"
"")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 231, 121))
        self.label_6.setStyleSheet("border-image: url(:/newPrefix/Marohuma_icono.png);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Marohuma icono.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Facebook.setText(_translate("MainWindow", "Î"))
        self.Instagram.setText(_translate("MainWindow", "Ú"))
        self.WhatsApp.setText(_translate("MainWindow", "Õ"))
        self.Web.setText(_translate("MainWindow", "Å"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Iniciar Sesión</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">¿Ha olvidado su usuario o contraseña?</span></p></body></html>"))
        self.txtPassword.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.txtUsuario.setPlaceholderText(_translate("MainWindow", "Usuario"))
        self.btnIniciar.setText(_translate("MainWindow", "Iniciar"))
        self.btnMinimizar.setText(_translate("MainWindow", ""))
        self.btnCerrar.setText(_translate("MainWindow", "9"))

    