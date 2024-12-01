class Cliente:
    def __init__ (self,NumeroDocumento,Nombre,TipoDocumento,Direccion,Telefono):
        self.__NumeroDocumento=NumeroDocumento
        self.__Nombre=Nombre
        self.__TipoDocumento=TipoDocumento
        self.__Direccion=Direccion
        self.__Telefono=Telefono
        
    def getNumeroDocumento(self):
        return self.__NumeroDocumento

    def getNombre(self):
        return self.__Nombre
    
    def getTipoDocumento(self):
        return self.__TipoDocumento
    
    def getDireccion(self):
        return self.__Direccion
    
    def getTelefono(self):
        return self.__Telefono
    
    def setNumeroDocumento(self,numDocumento):
        self.__NumeroDocumento= numDocumento
        
    def setNombre(self, Nombre):
        self.__Nombre = Nombre
    
    def setTipoDocumento(self, TipoDocumento):
        self.__TipoDocumento = TipoDocumento
    
    def setDireccion(self, Direccion):
        self.__Direccion = Direccion
    
    def setTelefono(self, Telefono):
        self.__Telefono = Telefono