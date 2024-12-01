class Usuario: 
    def __init__ (self, IdUsuario, DniEmpleado, NombreUsuario, Contraseña):
        self.__IdUsuario=IdUsuario
        self.__DniEmpleado=DniEmpleado
        self.__NombreUsuario=NombreUsuario
        self.__Contraseña=Contraseña

    # Métodos Get
    def getIdUsuario(self):
        return self.__IdUsuario
    
    def getDniEmpleado(self):
        return self.__DniEmpleado
    
    def getNombreUsuario(self):
        return self.__NombreUsuario
    
    def getPassword(self):
        return self.__Contraseña

    # Métodos Set
    def setIdUsuario(self, IdUsuario):
        self.__IdUsuario = IdUsuario
    
    def setDniEmpleado(self, DniEmpleado):
        self.__DniEmpleado = DniEmpleado
    
    def setNombreUsuario(self, NombreUsuario):
        self.__NombreUsuario = NombreUsuario
    
    def setPassword(self, Contraseña):
        self.__Contraseña = Contraseña
