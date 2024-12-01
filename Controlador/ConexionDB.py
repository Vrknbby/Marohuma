import pyodbc
class ConexionDB():
     def __init__(self):
         pass

     def CadenaConexion(self):
         #server = "DESKTOP-GPBU513\SQLEXPRESS"
         server = "DESKTOP-GPBU513\SQLEXPRESS"
         DataBase="ProyectoMarohuma"
         SinPassword="yes"
         cadena=(
             f"DRIVER={{SQL Server}};"
             f"SERVER={server};"
             f"DATABASE={DataBase};"
             f"Trusted_Connection={SinPassword}")
         return cadena

     def identificarRol(self,dniEmpleado):
        conexion=pyodbc.connect(self.CadenaConexion())
        comando= conexion.cursor()
        comando.execute("select * from Empleado where DniEmpleado="+str(dniEmpleado))
        objEmpleado = comando.fetchone()
        comando.execute("select * from Rol where IdRol="+str(objEmpleado[2]))
        objRol=comando.fetchone()
        return str(objRol[1])

     def identificarCorreo(self,dni):
        conexion=pyodbc.connect(self.CadenaConexion())
        comando= conexion.cursor()
        comando.execute("select * from Empleado where DniEmpleado="+str(dni))
        objEmpleado = comando.fetchone()
        return str(objEmpleado[7])