class Material:
    def __init__(self, IdMaterial, IdServicio, Nombre, Descripcion, Stock, UnidadMedida, Frente):
        self.__IdMaterial = IdMaterial
        self.__IdServicio = IdServicio
        self.__Nombre = Nombre
        self.__Descripcion = Descripcion
        self.__Stock = Stock
        self.__UnidadMedida = UnidadMedida
        self.__Frente = Frente

    def getIdMaterial(self):
        return self.__IdMaterial

    def getIdServicio(self):
        return self.__IdServicio

    def getNombre(self):
        return self.__Nombre

    def getDescripcion(self):
        return self.__Descripcion

    def getStock(self):
        return self.__Stock

    def getUnidadMedida(self):
        return self.__UnidadMedida

    def getFrente(self):
        return self.__Frente

    def setIdMaterial(self, IdMaterial):
        self.__IdMaterial = IdMaterial

    def setIdServicio(self, IdServicio):
        self.__IdServicio = IdServicio

    def setNombre(self, Nombre):
        self.__Nombre = Nombre

    def setDescripcion(self, Descripcion):
        self.__Descripcion = Descripcion

    def setStock(self, Stock):
        self.__Stock = Stock

    def setUnidadMedida(self, UnidadMedida):
        self.__UnidadMedida = UnidadMedida

    def setFrente(self, Frente):
        self.__Frente = Frente