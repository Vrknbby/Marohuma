class Documento():
    def __init__ (self, ID, IdServicio, Tipo, Descripcion, Fecha=None):
        self.__ID=ID
        self.__IdSevicio=IdServicio
        self.__Tipo=Tipo
        self.__Descripcion=Descripcion
        self.__Fecha=Fecha
    
    def getID(self):
        return self.__ID
    
    def getIdServicio(self):
        return self.__IdSevicio
    
    def getTipo(self):
        return self.__Tipo
    
    def getDescripcion(self):
        return self.__Descripcion
    
    def getFecha(self):
        return self.__Fecha

    def setID(self, ID):
        self.__ID = ID
    
    def setIdServicio(self, IdServicio):
        self.__IdSevicio = IdServicio
    
    def setTipo(self, Tipo):
        self.__Tipo = Tipo
    
    def setDescripcion(self, Descripcion):
        self.__Descripcion = Descripcion
        
    def setFecha(self, Fecha):
        self.__Fecha = Fecha