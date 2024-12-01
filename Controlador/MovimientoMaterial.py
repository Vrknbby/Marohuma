class MovimientoMaterial:
    def __init__(self, IdMovimiento, IdUsuario, IdMaterial, DniEmpleado, IdServicio, TipoMovimiento, Frente, cantidad, fecha):
        self.IdMovimiento = IdMovimiento
        self.IdUsuario = IdUsuario
        self.IdMaterial = IdMaterial
        self.DniEmpleado = DniEmpleado
        self.IdServicio = IdServicio
        self.TipoMovimiento = TipoMovimiento
        self.Frente = Frente
        self.cantidad = cantidad
        self.fecha = fecha

    def getIdMovimiento(self):
        return self.IdMovimiento

    def getIdUsuario(self):
        return self.IdUsuario

    def getIdMaterial(self):
        return self.IdMaterial

    def getDniEmpleado(self):
        return self.DniEmpleado

    def getIdServicio(self):
        return self.IdServicio

    def getTipoMovimiento(self):
        return self.TipoMovimiento

    def getFrente(self):
        return self.Frente

    def getCantidad(self):
        return self.cantidad

    def getFecha(self):
        return self.fecha

    def setIdMovimiento(self, IdMovimiento):
        self.IdMovimiento = IdMovimiento

    def setIdUsuario(self, IdUsuario):
        self.IdUsuario = IdUsuario

    def setIdMaterial(self, IdMaterial):
        self.IdMaterial = IdMaterial

    def setDniEmpleado(self, DniEmpleado):
        self.DniEmpleado = DniEmpleado

    def setIdServicio(self, IdServicio):
        self.IdServicio = IdServicio

    def setTipoMovimiento(self, TipoMovimiento):
        self.TipoMovimiento = TipoMovimiento

    def setFrente(self, Frente):
        self.Frente = Frente

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def setFecha(self, fecha):
        self.fecha = fecha
