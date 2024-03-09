class Implantes:
    def __init__(self,material,tamaño):
        self.__material = material
        self.__tamaño = tamaño
        #Metodos get
    def verMaterial(self):
        return self.__material
    def verTamaño(self):
        return self.__tamaño
    #Metodos set
    def asignarMaterial(self,m):
        self.__material = m
    def asignarTamaño(self,t):
        self.__tamaño = t

class Protesis_Cadera(Implantes):
    def __init__(self,material,tamaño,fijacion):
        super().__init__(material,tamaño)
        self.fijacion =  fijacion 

class Marcapasos:
    def __init__(self,electrodos,conectividad,frecuencia):
        self.electrodos = electrodos
        self.conectividad = conectividad
        self.frecuencia = frecuencia

class StendCoronario(Implantes):
    def __init__(self,longitud,material,diametro):
        super().__init__(material,None)
        self.longitud = longitud
        self.diametro = diametro

class ImplanteDental(Implantes):
    def __init__(self,forma,fijacion,material):
        super().__init__(material,None)
        self.forma = forma
        self.fijacion = fijacion

class ImplanteRodilla(Implantes):
    def __init__(self,material,fijacion,tamaño):
        super().__init__(material,tamaño)
        self.fijacion = fijacion

class ImplanteCadera(Implantes):
    def __init__(self,material,fijacion,tamaño):
        super().__init__(material,tamaño)
        self.fijacion = fijacion

class Sistema:
    def __init__(self):
        self.



