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

class Paciente():
    def __init__(self,nombre,cedula):
        self.__nombre = nombre
        self.__cedula = cedula
    
    def verNombre(self):
        return self.__nombre
    def VerCedula(self):
        return self.__cedula
    
    def AsignarNombre(self,n):
        self.__nombre = n
    def AsignarCedula(self,c):
        self.__cedula = c



class Sistema:
    def __init__(self):
        self.__inventario = {}
    
    
    def verificarExiste(self,paciente):
        if paciente in self.__inventario:
            return True
        return False


