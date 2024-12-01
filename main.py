import sys
from PyQt5 import QtWidgets
from UI.Imagenes import recursos
from Vista.Login import Login

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    sys.exit(app.exec())    