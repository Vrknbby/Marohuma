class Empleado: 
    def __init__ (self, dniEmpleado, idEspecialidad, idRol, nombre, apellido, fechaNacimiento, sueldo, eMail, estado):
        self.__dniEmpleado = dniEmpleado
        self.__idEspecialidad = idEspecialidad
        self.__idRol = idRol
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fechaNacimiento = fechaNacimiento
        self.__sueldo = sueldo
        self.__eMail = eMail
        self.__estado = estado

    # Métodos Get
    def getDniEmpleado(self):
        return self.__dniEmpleado
    
    def getIdEspecialidad(self):
        return self.__idEspecialidad
    
    def getIdRol(self):
        return self.__idRol
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getFechaNacimiento(self):
        return self.__fechaNacimiento
    
    def getSueldo(self):
        return self.__sueldo
    
    def getEmail(self):
        return self.__eMail
    
    def getEstado(self):
        return self.__estado

    # Métodos Set
    def setDniEmpleado(self, dniEmpleado):
        self.__dniEmpleado = dniEmpleado
    
    def setIdEspecialidad(self, idEspecialidad):
        self.__idEspecialidad = idEspecialidad
    
    def setIdRol(self, idRol):
        self.__idRol = idRol
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setApellido(self, apellido):
        self.__apellido = apellido
    
    def setFechaNacimiento(self, fechaNacimiento):
        self.__fechaNacimiento = fechaNacimiento
    
    def setSueldo(self, sueldo):
        self.__sueldo = sueldo
    
    def setEmail(self, eMail):
        self.__eMail = eMail
    
    def setEstado(self, estado):
        self.__estado = estado
