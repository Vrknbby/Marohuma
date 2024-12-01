from Controlador.ConexionDB import *
from Controlador.Material import *
DataBase = ConexionDB()

class ArregloMaterial():
    def __init__(self):
        pass

    def listar(self):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM Material")
            materiales = comando.fetchall()
            comando.close()
            return materiales
        except Exception as e:
            print("Error al listar materiales:", str(e))
            return []

    def insertar(self, objMaterial):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("INSERT INTO Material (IdServicio, Nombre, Descripcion, Stock, UnidadMedida, Frente) VALUES (?,?,?,?,?,?)",
                            objMaterial.getIdServicio(), objMaterial.getNombre(), objMaterial.getDescripcion(),
                            objMaterial.getStock(), objMaterial.getUnidadMedida(), objMaterial.getFrente())
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al insertar material:", str(e))

    def eliminar(self, idMaterial):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("DELETE FROM Material WHERE IdMaterial = ?", idMaterial)
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al eliminar material:", str(e))

    def modificar(self, objMaterial):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("UPDATE Material SET IdServicio = ?, Nombre = ?, Descripcion = ?, Stock = ?, UnidadMedida = ?, Frente = ? WHERE IdMaterial = ?",
                            objMaterial.getIdServicio(), objMaterial.getNombre(), objMaterial.getDescripcion(),
                            objMaterial.getStock(), objMaterial.getUnidadMedida(), objMaterial.getFrente(), objMaterial.getIdMaterial())
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al modificar material:", str(e))

    def consultar(self, idMaterial):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM Material WHERE IdMaterial = ?", idMaterial)
            material = comando.fetchone()
            comando.close()
            return material
        except Exception as e:
            print("Error al consultar material:", str(e))
            return None  

    def verificarExistencia(self, idMaterial):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM Material WHERE IdMaterial = ?", idMaterial)
            material = comando.fetchone()
            if material:
                comando.close()
                return True
            else:
                comando.close()
                return False
        except Exception as e:
            print("Error al verificar existencia del material:", str(e))
            return False

    def aumentarStock(self, idMaterial, cantidad):
        try:
            if not isinstance(cantidad, int) or cantidad <= 0:
                raise ValueError("La cantidad debe ser un entero positivo.")
            
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("UPDATE Material SET Stock = Stock + ? WHERE IdMaterial = ?", cantidad, idMaterial)
            comando.commit()
            comando.close()
        except Exception as e:
            print("Error al aumentar el stock del material:", str(e))

    def listarPorServicio(self, IdServicio):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()
            comando.execute("SELECT * FROM Material WHERE IdServicio = ?", str(IdServicio))
            materiales = comando.fetchall()
            conexion.close()
            return materiales
        except Exception as e:
            print("Error al listar materiales por servicio:", str(e))
            return []
    
    def reducirStock(self, idMaterial, cantidad):
        try:
            if not isinstance(cantidad, int) or cantidad <= 0:
                raise ValueError("La cantidad debe ser un entero positivo.")

            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()

            comando.execute("SELECT Stock FROM Material WHERE IdMaterial = ?", idMaterial)
            stock_actual = comando.fetchone()[0]
            nuevo_stock = stock_actual - cantidad
            if nuevo_stock < 0:
                raise ValueError("La cantidad a reducir excede el stock disponible.")
                
            comando.execute("UPDATE Material SET Stock = ? WHERE IdMaterial = ?", nuevo_stock, idMaterial)
            comando.commit()
            comando.close()
            return True
        except Exception as e:
            print("Error al reducir el stock del material:", str(e))
            return False
    
    def verificarNombre(self, IdServicio, nombre):
        try:
            conexion = pyodbc.connect(DataBase.CadenaConexion())
            comando = conexion.cursor()

            comando.execute("select IdServicio,Nombre from Material WHERE IdServicio = ?", IdServicio)
            materiales= comando.fetchall()
            for id, nom in materiales:
                if str(nom).upper() == nombre.upper():
                    return True
            return False
        except Exception as e:
            print("Error al consultar.:", str(e))
            return False