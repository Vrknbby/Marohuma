from Controlador.Proveedor import *
from Controlador.ConexionDB import *

DataBase= ConexionDB()

class ArregloProveedor():
    def __init__(self):
        pass

    def listar(self):
        try:
            conexion= pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Proveedor")
            Proveedores= comando.fetchall()
            conexion.close()
            return Proveedores
        except Exception as e:
            print("Error al listar proveedores:", str(e))
            return []

    def insertar(self, objProveedor):
        try:
            conexion= pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("insert into Proveedor (Ruc, Nombre, RazSocial, Direccion, Telefono)"+
                            " VALUES (?,?,?,?,?)", objProveedor.getRuc(),objProveedor.getNombre(),objProveedor.getRazSocial(),objProveedor.getDireccion(),objProveedor.getTelefono())
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al insertar proveedor:", str(e))

    def modificar(self, objProveedor):
        try:
            conexion= pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("update Proveedor set Nombre = ?, RazSocial = ?, Direccion = ?, Telefono = ? where Ruc = ?",
                            objProveedor.getNombre(),objProveedor.getRazSocial(),objProveedor.getDireccion(),objProveedor.getTelefono(),objProveedor.getRuc())
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al modificar proveedor:", str(e))

    def verificarExistencia(self, Ruc):
        try:
            conexion= pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Proveedor where Ruc = ?", Ruc)
            objprovee=comando.fetchone()
            if (objprovee):
                comando.close()
                return True
            else:
                comando.close()
                return False
        except Exception as e:
            print("Error al verificar existencia del proveedor:", str(e))
            return False
