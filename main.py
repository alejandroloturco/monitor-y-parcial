class Implantes:
    def __init__(self):
        self.material = ""
        self.tamaño = 0
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
    def __init__(self):
        super().__init__()
        self.fijacion = ""

