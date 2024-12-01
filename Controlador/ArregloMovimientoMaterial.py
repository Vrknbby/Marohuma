from Controlador.MovimientoMaterial import *
from Controlador.ConexionDB import ConexionDB
import pyodbc
DataBase = ConexionDB()

class ArregloMovimientoMaterial():
    def __init__(self):
        pass

    def listar(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM MovimientoMaterial")
            movimientos_material = comando.fetchall()
            comando.close()
            return movimientos_material
        except Exception as e:
            print("Error al listar movimientos de material:", str(e))
            return []

        
    def listarSalidas(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM VistaMovimientoMaterial where TipoMovimiento = 'Salida'")
            movimientos_material = comando.fetchall()
            comando.close()
            return movimientos_material
        except Exception as e:
            print("Error al listar movimientos de material:", str(e))
            return []

    def insertar(self, objMovimientoMaterial):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("INSERT INTO MovimientoMaterial (IdUsuario, IdMaterial, DniEmpleado, IdServicio, TipoMovimiento, Frente, cantidad, Fecha) VALUES (?,?,?,?,?,?,?,?)",
                            objMovimientoMaterial.getIdUsuario(), objMovimientoMaterial.getIdMaterial(), objMovimientoMaterial.getDniEmpleado(),
                            objMovimientoMaterial.getIdServicio(), objMovimientoMaterial.getTipoMovimiento(), objMovimientoMaterial.getFrente(),
                            objMovimientoMaterial.getCantidad(), objMovimientoMaterial.getFecha())
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al insertar movimiento de material:", str(e))

    def eliminar(self, idMovimiento):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("DELETE FROM MovimientoMaterial WHERE IdMovimiento = ?", idMovimiento)
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al eliminar movimiento de material:", str(e))

    def modificar(self, objMovimientoMaterial):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("UPDATE MovimientoMaterial SET IdUsuario = ?, IdMaterial = ?, DniEmpleado = ?, IdServicio = ?, TipoMovimiento = ?, Frente = ?, cantidad = ?, fecha = ? WHERE IdMovimiento = ?",
                            objMovimientoMaterial.getIdUsuario(), objMovimientoMaterial.getIdMaterial(), objMovimientoMaterial.getDniEmpleado(),
                            objMovimientoMaterial.getIdServicio(), objMovimientoMaterial.getTipoMovimiento(), objMovimientoMaterial.getFrente(),
                            objMovimientoMaterial.getCantidad(), objMovimientoMaterial.getFecha(), objMovimientoMaterial.getIdMovimiento())
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al modificar movimiento de material:", str(e))

    def consultar(self, idMovimiento):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM MovimientoMaterial WHERE IdMovimiento = ?", idMovimiento)
            movimiento_material = comando.fetchone()
            comando.close()
            return movimiento_material
        except Exception as e:
            print("Error al consultar movimiento de material:", str(e))
            return None

    def verificarExistencia(self, idMovimiento):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM MovimientoMaterial WHERE IdMovimiento = ?", idMovimiento)
            movimiento_material = comando.fetchone()
            if movimiento_material:
                comando.close()
                return True
            else:
                comando.close()
                return False
        except Exception as e:
            print("Error al verificar existencia del movimiento de material:", str(e))
            return False

    def listarPor(self, tipo):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM VistaMovimientoMaterial WHERE TipoMovimiento = ?", str(tipo))
            movimientos = comando.fetchall()
            conexion.close()
            return movimientos
        except Exception as e:
            print("Error al listar materiales por servicio:", str(e))
            return []
    
    def listarVista(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM VistaMovimientoMaterial")
            movimientos_material = comando.fetchall()
            comando.close()
            return movimientos_material
        except Exception as e:
            print("Error al listar movimientos de material:", str(e))
            return []