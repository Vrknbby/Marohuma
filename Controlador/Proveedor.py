class Proveedor():
    def __init__(self,Ruc, Nombre,RazSocial, Direccion, Telefono):
        self.__Ruc=Ruc
        self.__Nombre=Nombre
        self.__RazSocial=RazSocial
        self.__Direccion=Direccion
        self.__Telefono=Telefono
    
    def getRuc(self):
        return self.__Ruc

    def getNombre(self):
        return self.__Nombre

    def getRazSocial(self):
        return self.__RazSocial

    def getDireccion(self):
        return self.__Direccion

    def getTelefono(self):
        return self.__Telefono

    def setRuc(self, Ruc):
        self.__Ruc = Ruc

    def setNombre(self, Nombre):
        self.__Nombre = Nombre

    def setRazSocial(self, RazSocial):
        self.__RazSocial = RazSocial

    def setDireccion(self, Direccion):
        self.__Direccion = Direccion

    def setTelefono(self, Telefono):
        self.__Telefono = Telefono