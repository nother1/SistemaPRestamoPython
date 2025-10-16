class prestamo:
    def __init__(self, idUser ,fechaPrestamo, estadoPrestamo):
        self._idUser = idUser
        self._fechaPrestamo = fechaPrestamo
        self._estadoPrestamo = estadoPrestamo
        
    @property
    def idUser(self):
        return self._idUser
    
    @property
    def fechaPrestamo(self):
        return self._fechaPrestamo
    
    @property
    def estadoPrestamo(self):
        return self._estadoPrestamo
    
        
    @idUser.setter
    def idUser(self, val):
        self._idUser = val
        
    @fechaPrestamo.setter
    def fechaPrestamo(self, val):
        self._fechaPrestamo = val
        
    @estadoPrestamo.setter
    def estadoPrestamo(self, val):
        self._estadoPrestamo = val