from Controlador.Usuario import *
from Controlador.ConexionDB import *

DataBase = ConexionDB()

class ArregloUsuario:
    def __init__(self):
        pass
    
    def cargar(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Usuario")
            objUsuario = comando.fetchone()
            while objUsuario:
                self.agregarUsuario(objUsuario)
                objUsuario = comando.fetchone()
            conexion.close()
        except Exception as e:
            print("Error al cargar usuarios:", str(e))

    def listarTodos(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Usuario")
            usuarios = comando.fetchall()
            conexion.close()
            return usuarios    
        except Exception as e:
            print("Error al listar todos los usuarios:", str(e))
            return []

    def crearUsuario(self, dni, nombre, Apellido):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            nomUser = str(Apellido[0].upper()) + str(nombre[0].upper()) + str(dni)
            password = str(dni)
            comando.execute("insert into Usuario values(?,?,?)", dni, nomUser, password)
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al crear usuario:", str(e))
