from Controlador.ConexionDB import *
from Controlador.Documento import *

DataBase = ConexionDB()

class ArregloDocumento():
    def __init__(self):
        pass

    def insertar(self, objDocumento):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("INSERT INTO Documento (ID, IdServicio, Tipo, Descripcion, Fecha)"+
                            " VALUES (?,?,?,?,?)", objDocumento.getID(), objDocumento.getIdServicio(), objDocumento.getTipo(), objDocumento.getDescripcion(), objDocumento.getFecha())
            comando.commit()
            comando.close()
            return True
        except Exception as e:
            print("Error al insertar documento:", str(e))
            return False
    
    def insertarSinFecha(self, objDocumento):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("INSERT INTO Documento (ID, IdServicio, Tipo, Descripcion)"+
                            " VALUES (?,?,?,?)", objDocumento.getID(), objDocumento.getIdServicio(), objDocumento.getTipo(), objDocumento.getDescripcion())
            comando.commit()
            comando.close()
            return True
        except Exception as e:
            print("Error al insertar documento sin fecha:", str(e))
            return False

    def listar(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Documento")
            documentos = comando.fetchall()
            comando.close()
            return documentos
        except Exception as e:
            print("Error al listar documentos:", str(e))
            return []

    def listarPor(self, Servicio):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Documento where IdServicio = ?", str(Servicio))
            listdocumentos = comando.fetchall()
            conexion.close()
            return listdocumentos 
        except Exception as e:
            print("Error al listar documentos por servicio:", str(e))
            return []

    def verificarExistencia(self, id):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Documento where ID = ?", id)
            objDocumento = comando.fetchone()
            conexion.close()
            return bool(objDocumento)
        except Exception as e:
            print("Error al verificar existencia del documento:", str(e))
            return False
