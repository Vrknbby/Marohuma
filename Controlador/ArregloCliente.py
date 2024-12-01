from Controlador.ConexionDB import *
from Controlador.Cliente import *
DataBase = ConexionDB()

class ArregloCliente():
    def __init__(self):
        pass

    def listar(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Cliente")
            clientes = comando.fetchall()
            conexion.close()
            return clientes
        except Exception as e:
            print("Error al listar clientes:", str(e))
            return []

    def insertar(self, objCliente):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("INSERT INTO Cliente (NumeroDocumento, Nombre, TipoDocumento, Direccion, Telefono)" +
                            " VALUES (?,?,?,?,?)", objCliente.getNumeroDocumento(), objCliente.getNombre(), objCliente.getTipoDocumento(), objCliente.getDireccion(), objCliente.getTelefono())
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al insertar cliente:", str(e))

    def eliminar(self, numDoc):
        try:
            self.EliminarCliente(numDoc)
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("delete from Cliente where NumeroDocumento = ?", numDoc)
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al eliminar cliente:", str(e))

    def EliminarCliente(self, numDoc):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("delete from Cliente where NumeroDocumento = ?", str(numDoc))
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al eliminar cliente:", str(e))

    def modificar(self, objCliente):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("update Cliente set Nombre = ?, TipoDocumento = ?, Direccion = ?, Telefono = ? where NumeroDocumento = ?",
                            objCliente.getNombre(), objCliente.getTipoDocumento(), objCliente.getDireccion(), objCliente.getTelefono(), objCliente.getNumeroDocumento())
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al modificar cliente:", str(e))

    def consultar(self, numDoc):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Cliente where NumeroDocumento = ?", numDoc)
            objCliente = comando.fetchone()
            return objCliente
        except Exception as e:
            print("Error al consultar cliente:", str(e))
            return None

    def verificarExistencia(self, numDoc):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Cliente where NumeroDocumento = ?", numDoc)
            objCliente = comando.fetchone()
            conexion.close()
            return bool(objCliente)
        except Exception as e:
            print("Error al verificar existencia del cliente:", str(e))
            return False

    def guardarCliente(self, numDoc):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Cliente where NumeroDocumento = ?", numDoc)
            objCliente = comando.fetchone()
            conexion.close()
            return objCliente
        except Exception as e:
            print("Error al guardar cliente:", str(e))
            return None
