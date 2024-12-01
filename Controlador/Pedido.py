class Pedido:
    def __init__(self, NumPedido, RucPro, TipoDoc, Fecha, DetalleRegistrado=0):
        self.__NumPedido = NumPedido
        self.__RucPro = RucPro
        self.__TipoDoc = TipoDoc
        self.__Fecha = Fecha
        self.__DetalleRegistrado = DetalleRegistrado
        
    def getNumPedido(self):
        return self.__NumPedido
    
    def getRucPro(self):
        return self.__RucPro
    
    def getTipoDoc(self):
        return self.__TipoDoc
    
    def getFecha(self):
        return self.__Fecha

    def getDetalleRegistrado(self):
        return self.__DetalleRegistrado

    def setNumPedido(self, NumPedido):
        self.__NumPedido = NumPedido
    
    def setRucPro(self, RucPro):
        self.__RucPro = RucPro
    
    def setTipoDoc(self, TipoDoc):
        self.__TipoDoc = TipoDoc
    
    def setFecha(self, Fecha):
        self.__Fecha = Fecha
    
    def setDetalleRegistrado(self, DetalleRegistrado):
        self.__DetalleRegistrado = DetalleRegistrado


        