class DetalleCompra:
    def __init__(self, IdDetalle, IdServicio, NumPedido, IdMaterial, Cantidad, PrecioU, PrecioP, MetodoPago, Estado):
        self.__IdDetalle = IdDetalle
        self.__IdServicio = IdServicio
        self.__NumPedido = NumPedido
        self.__IdMaterial = IdMaterial
        self.__Cantidad = Cantidad
        self.__PrecioU = PrecioU
        self.__PrecioP = PrecioP
        self.__MetodoPago = MetodoPago
        self.__Estado = Estado

    def getIdDetalle(self):
        return self.__IdDetalle

    def getIdServicio(self):
        return self.__IdServicio

    def getNumPedido(self):
        return self.__NumPedido

    def getIdMaterial(self):
        return self.__IdMaterial

    def getCantidad(self):
        return self.__Cantidad

    def getPrecioU(self):
        return self.__PrecioU

    def getPrecioP(self):
        return self.__PrecioP

    def getMetodoPago(self):
        return self.__MetodoPago

    def getEstado(self):
        return self.__Estado

    def setIdDetalle(self, IdDetalle):
        self.__IdDetalle = IdDetalle

    def setIdServicio(self, IdServicio):
        self.__IdServicio = IdServicio

    def setNumPedido(self, NumPedido):
        self.__NumPedido = NumPedido

    def setIdMaterial(self, IdMaterial):
        self.__IdMaterial = IdMaterial

    def setCantidad(self, Cantidad):
        self.__Cantidad = Cantidad

    def setPrecioU(self, PrecioU):
        self.__PrecioU = PrecioU

    def setPrecioP(self, PrecioP):
        self.__PrecioP = PrecioP

    def setMetodoPago(self, MetodoPago):
        self.__MetodoPago = MetodoPago

    def setEstado(self, Estado):
        self.__Estado = Estado
