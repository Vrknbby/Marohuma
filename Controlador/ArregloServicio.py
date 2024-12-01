from Controlador.ConexionDB import *
from Controlador.Servicio import *
from Controlador.ArregloCliente import *

DataBase= ConexionDB()

class ArregloServicio():
    def __init__(self):
        pass
        
    def listar(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Servicio")
            servicio = comando.fetchall()
            conexion.close()
            return servicio
        except Exception as e:
            print("Error al listar servicios:", str(e))
            return []

    def insertar(self, objServicio):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("INSERT INTO Servicio (IdServicio, NumeroDocumento, IdUsuario, NombreProyecto, TipoServicio, InicioProyecto,FinProyecto,CantEmpleados,DireccionProyecto,Costo, Estado)"+
                            " VALUES (?,?,?,?,?,?,?,?,?,?,?)", objServicio.getIdServicio(),objServicio.getNumeroDocumento(),objServicio.getIdUsuario(),objServicio.getNombreProyecto(),
                            objServicio.getTipoServicio(),objServicio.getInicioProyecto(),objServicio.getFinProyecto(),objServicio.getCantEmpleados(),objServicio.getDireccionProyectos(),objServicio.getCosto(), "En Proceso")
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al insertar servicio:", str(e))

    def modificar(self, objServicio):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("update Servicio set NumeroDocumento = ?, IdUsuario = ?, NombreProyecto = ?, TipoServicio = ?, InicioProyecto = ?, FinProyecto = ?, CantEmpleados = ?, DireccionProyecto = ?, Costo = ?, Estado = ? where IdServicio = ?",
                            objServicio.getNumeroDocumento(),objServicio.getIdUsuario(),objServicio.getNombreProyecto(),
                            objServicio.getTipoServicio(),objServicio.getInicioProyecto(),objServicio.getFinProyecto(),
                            objServicio.getCantEmpleados(),objServicio.getDireccionProyectos(),objServicio.getCosto(), objServicio.getEstado(), objServicio.getIdServicio())
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al modificar servicio:", str(e))

    def verificarExistencia(self, idSer):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Servicio where IdServicio = ?", idSer)
            objServicio = comando.fetchone()
            if objServicio:
                comando.close()
                return True
            else:
                comando.close()
                return False
        except Exception as e:
            print("Error al verificar existencia del servicio:", str(e))
            return False

    def guardar(self, idSer):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Servicio where IdServicio = ?", idSer)
            objServicio = comando.fetchone()
            return objServicio 
        except Exception as e:
            print("Error al guardar servicio:", str(e))
            return None

    def consultar(self, idSer):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("select * from Servicio where IdServicio = ?", idSer)
            objServicio = comando.fetchone()
            return objServicio 
        except Exception as e:
            print("Error al consultar servicio:", str(e))
            return None

    def cambiarEstado(self, idServicio):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT Estado FROM Servicio WHERE IdServicio = ?", idServicio)
            estado_actual = comando.fetchone()[0]
            
            nuevo_estado = "Terminado" if estado_actual == "En Proceso" else "En Proceso"
            comando.execute("UPDATE Servicio SET Estado = ? WHERE IdServicio = ?", nuevo_estado, idServicio)
            conexion.commit()
            conexion.close()
        except Exception as e:
            print("Error al cambiar el estado del servicio:", str(e))