from Controlador.ConexionDB import *
from Controlador.DetalleCompra import *
from PyQt5 import QtCore, QtGui, QtWidgets

DataBase = ConexionDB()

class ArregloDetalleCompra():
    def __init__(self):
        pass

    def listar(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM DetalleCompra")
            detallesCompra = comando.fetchall()
            comando.close()
            return detallesCompra
        except Exception as e:
            print("Error al listar detalles de compra:", str(e))
            return []

    def listarVista(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM VistaDetalleCompra")
            detallesCompra = comando.fetchall()
            comando.close()
            return detallesCompra
        except Exception as e:
            print("Error al listar vista de detalles de compra:", str(e))
            return []

    def insertar(self, objDetalleCompra):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("INSERT INTO DetalleCompra (IdServicio, NumPedido, IdMaterial, Cantidad, PrecioU, PrecioP, MetodoPago, Estado) VALUES (?,?,?,?,?,?,?,?)",
                            objDetalleCompra.getIdServicio(), objDetalleCompra.getNumPedido(), objDetalleCompra.getIdMaterial(),
                            objDetalleCompra.getCantidad(), objDetalleCompra.getPrecioU(), objDetalleCompra.getPrecioP(),
                            objDetalleCompra.getMetodoPago(), objDetalleCompra.getEstado())
            comando.commit()
            comando.close()
            return True
        except Exception as e:
            print("Error al insertar detalle de compra:", str(e))
            return False
    
    def listarPor(self, estado):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM VistaDetalleCompra WHERE Estado = ?", estado)
            listadetalle = comando.fetchall()
            conexion.close()
            return listadetalle
        except Exception as e:
            print("Error al listar detalles de compra por estado:", str(e))
            return []

    def eliminar(self, idDetalle):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("DELETE FROM DetalleCompra WHERE IdDetalle = ?", idDetalle)
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al eliminar detalle de compra:", str(e))

    def modificar(self, objDetalleCompra):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("UPDATE DetalleCompra SET IdServicio = ?, NumPedido = ?, IdMaterial = ?, Cantidad = ?, PrecioU = ?, PrecioP = ?, MetodoPago = ?, Estado = ? WHERE IdDetalle = ?",
                             objDetalleCompra.getIdServicio(), objDetalleCompra.getNumPedido(), objDetalleCompra.getIdMaterial(),
                             objDetalleCompra.getCantidad(), objDetalleCompra.getPrecioU(), objDetalleCompra.getPrecioP(),
                             objDetalleCompra.getMetodoPago(), objDetalleCompra.getEstado(), objDetalleCompra.getIdDetalle())
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al modificar detalle de compra:", str(e))
        
    def consultar(self, idDetalle):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM DetalleCompra WHERE IdDetalle = ?", idDetalle)
            objDetalleCompra = comando.fetchone()
            comando.close()
            return objDetalleCompra
        except Exception as e:
            print("Error al consultar detalle de compra:", str(e))
            return None
    
    def verificarExistencia(self, idDetalle):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM DetalleCompra WHERE IdDetalle = ?", idDetalle)
            objDetalleCompra = comando.fetchone()
            conexion.close()
            return bool(objDetalleCompra)
        except Exception as e:
            print("Error al verificar existencia del detalle de compra:", str(e))
            return False

    def cambiaEstado(self, idDetalle):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT Estado FROM DetalleCompra WHERE IdDetalle = ?", idDetalle)
            estadoActual = comando.fetchone()[0]
            
            if estadoActual == "Espera":
                comando.execute("UPDATE DetalleCompra SET Estado = 'Recibido' WHERE IdDetalle = ?", idDetalle)
                conexion.commit()
                comando.close()
                return True
            else:
                return False
        except Exception as e:
            print("Error al cambiar el estado del detalle de compra:", str(e))
            return False

            
