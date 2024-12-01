from Controlador.Empleado import *
from Controlador.ConexionDB import *
from Controlador.ArregloUsuario import *

DataBase = ConexionDB()
aUsuario = ArregloUsuario()
empleado = []

class ArregloEmpleado():
    def __init__(self):
        pass

    def cargar(self, dni):
        objEmpleado=self.consultar(dni)
        empleado.append(objEmpleado)

    def listarEmpleados(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Empleado")
            empleados = comando.fetchall()
            return empleados
        except Exception as e:
            print("Error al listar empleados:", str(e))
            return []

    def listarVista(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from viewEmpleados")
            empleados = comando.fetchall()
            return empleados
        except Exception as e:
            print("Error al listar empleados vista:", str(e))
            return []

    ########################################################################
    def insertar(self, objEmpleado):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("INSERT INTO Empleado (DniEmpleado, IdEspecialidad, IdRol, Nombre, Apellido, FechaNacimiento, Sueldo, eMail, Estado)" +
                            " VALUES (?,?,?,?,?,?,?,?,?)", objEmpleado.getDniEmpleado(), objEmpleado.getIdEspecialidad(), objEmpleado.getIdRol(), objEmpleado.getNombre(), objEmpleado.getApellido(), objEmpleado.getFechaNacimiento(), objEmpleado.getSueldo(), objEmpleado.getEmail(), "Activo")
            comando.commit()
            aUsuario.crearUsuario(objEmpleado.getDniEmpleado(), objEmpleado.getNombre(), objEmpleado.getApellido())
            comando.close()
        except Exception as e:
            print("Error al insertar empleado:", str(e))

    def eliminar(self, dni):
        try:
            self.EliminarUsuario(dni)
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("delete from Empleado where DniEmpleado = ?", dni)
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al eliminar empleado:", str(e))

    def EliminarUsuario(self, dni):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("delete from Usuario where DniEmpleado = ?", str(dni))
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al eliminar usuario:", str(e))

    def modificar(self, objEmpleado):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("update Empleado set IdEspecialidad = ?, idRol = ?, Nombre = ?, Apellido = ?, FechaNacimiento = ?, Sueldo = ?, eMail = ?, Estado = Estado where DniEmpleado = ?",
                            objEmpleado.getIdEspecialidad(), objEmpleado.getIdRol(), objEmpleado.getNombre(), objEmpleado.getApellido(), objEmpleado.getFechaNacimiento(), objEmpleado.getSueldo(), objEmpleado.getEmail(), objEmpleado.getDniEmpleado())
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al modificar empleado:", str(e))

    def consultar(self, dni):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from viewEmpleados where DniEmpleado = ?", dni)
            objEmpleado = comando.fetchone()
            return objEmpleado
        except Exception as e:
            print("Error al consultar empleado:", str(e))
            return None

    def verificarExistencia(self, dni):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Empleado where DniEmpleado = ?", dni)
            objEmpleado = comando.fetchone()
            if objEmpleado:
                comando.close()
                return True
            else:
                comando.close()
                return False
        except Exception as e:
            print("Error al verificar existencia del empleado:", str(e))
            return False

    def guardarEmple(self, dni):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Empleado where DniEmpleado = ?", dni)
            objEmpleado = comando.fetchone()
            return objEmpleado
        except Exception as e:
            print("Error al guardar empleado:", str(e))
            return None

    def cambiarEstadoEmpleado(self, dni):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT Estado FROM Empleado WHERE DniEmpleado = ?", dni)
            EstadoActual = comando.fetchone()[0]
        
            NuevoEstado = "Activo" if EstadoActual == "Inactivo" else "Inactivo"
    
            comando.execute("UPDATE Empleado SET Estado = ? WHERE DniEmpleado = ?", NuevoEstado, dni)
            conexion.commit()
            comando.close()
        except Exception as e:
            print("Error al cambiar el estado del empleado:", str(e))

    def listarPorEstado(self, estado):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM viewEmpleados WHERE Estado = ?", estado)
            empleados = comando.fetchall()
            conexion.close()
            return empleados
        except Exception as e:
            print("Error al listar empleados por estado:", str(e))
            return []
