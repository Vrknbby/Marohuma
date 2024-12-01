from Controlador.ConexionDB import *
from Controlador.Pedido import *
DataBase = ConexionDB()

class ArregloPedido():
    def __init__(self):
        pass

    def listar(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM Pedido")
            Pedidos = comando.fetchall()
            conexion.close()
            return Pedidos
        except Exception as e:
            print("Error al listar pedidos:", str(e))
            return []

    def listarVista(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM VistaPedido")
            Pedidos = comando.fetchall()
            conexion.close()
            return Pedidos
        except Exception as e:
            print("Error al listar pedidos desde la vista:", str(e))
            return []
        
    def insertar(self, objPedido):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("INSERT INTO Pedido (NumPedido, RucPro, TipoDoc, Fecha, DetalleRegistrado) VALUES (?,?,?,?,?)",
                            objPedido.getNumPedido(), objPedido.getRucPro(), objPedido.getTipoDoc(), objPedido.getFecha(), 0)
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al insertar pedido:", str(e))

    def modificar(self, objPedido):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("UPDATE Pedido SET RucPro = ?, TipoDoc = ?, Fecha = ?, DetalleRegistrado = DetalleRegistrado WHERE NumPedido = ?",
                            objPedido.getRucPro(), objPedido.getTipoDoc(), objPedido.getFecha(), objPedido.getNumPedido())
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al modificar pedido:", str(e))

    def actualizarDetalleRegistrado(self, numPedido):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("UPDATE Pedido SET DetalleRegistrado = 1 WHERE NumPedido = ?", numPedido)
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al actualizar detalle registrado del pedido:", str(e))

