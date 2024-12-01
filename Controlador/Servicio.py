class Servicio:
    def __init__ (self, IdServicio, NumeroDocumento, IdUsuario, NombreProyecto, TipoServicio, InicioProyecto, FinProyecto, CantEmpleados, DireccionProyectos, Costo, Estado="En Proceso"):
        self.__IdServicio = IdServicio
        self.__NumeroDocumento = NumeroDocumento
        self.__IdUsuario = IdUsuario
        self.__NombreProyecto = NombreProyecto
        self.__TipoServicio = TipoServicio
        self.__InicioProyecto = InicioProyecto
        self.__FinProyecto = FinProyecto
        self.__CantEmpleados = CantEmpleados
        self.__DireccionProyectos = DireccionProyectos
        self.__Costo = Costo
        self.__Estado = Estado
    
    # Métodos Get    
    def getIdServicio(self):
        return self.__IdServicio
    
    def getNumeroDocumento(self):
        return self.__NumeroDocumento
    
    def getIdUsuario(self):
        return self.__IdUsuario
    
    def getNombreProyecto(self):
        return self.__NombreProyecto
    
    def getTipoServicio(self):
        return self.__TipoServicio
    
    def getInicioProyecto(self):
        return self.__InicioProyecto
    
    def getFinProyecto(self):
        return self.__FinProyecto
    
    def getCantEmpleados(self):
        return self.__CantEmpleados
    
    def getDireccionProyectos(self):
        return self.__DireccionProyectos
    
    def getCosto(self):
        return self.__Costo
    
    def getEstado(self):
        return self.__Estado

    # Métodos Set
    def setIdServicio(self, IdServicio):
        self.__IdServicio = IdServicio
    
    def setNumeroDocumento(self, NumeroDocumento):
        self.__NumeroDocumento = NumeroDocumento
    
    def setIdUsuario(self, IdUsuario):
        self.__IdUsuario = IdUsuario
    
    def setNombreProyecto(self, NombreProyecto):
        self.__NombreProyecto = NombreProyecto
        
    def setTipoServicio(self, TipoServicio):
        self.__TipoServicio = TipoServicio
    
    def setInicioProyecto(self, InicioProyecto):
        self.__InicioProyecto = InicioProyecto
        
    def setFinProyecto(self, FinProyecto):
        self.__FinProyecto = FinProyecto
    
    def setCantEmpleados(self, CantEmpleados):
        self.__CantEmpleados = CantEmpleados
        
    def setDireccionProyectos(self, DireccionProyectos):
        self.__DireccionProyectos = DireccionProyectos
        
    def setCosto(self, Costo):
        self.__Costo = Costo
    
    def setEstado(self, Estado):
        self.__Estado = Estado
