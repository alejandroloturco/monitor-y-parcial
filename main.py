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

class Sistema:
    def __init__(self):
        self.__inventario = {}
     

def main():
    sis = Sistema()     
    while True:
        menu = int(input("""Escoja una opcion 
                        \r1. Ingresar Paciente
                        \r2. Modificar Informacion para un paciente
                        \rIngrese--> """))
        if menu == 1:
            pass
        elif menu ==2:
            opcion = int(input("""Escoja una opcion 
                            \r1. Agregar nuevos implantes 
                            \r2. Eliminar implantes
                            \r3. Editar informacion de implantes
                            \r4. Visulaizar inventario completo
                            \r5. Salir
                            \rIngrese--> """)) 
            
            if opcion == 1:            
                print("""Seleccione el tipo de protesis:
                    \r1. Marcapasos 
                    \r2. Stend Coronario
                    \r3. Implante Denal
                    \r4. Implante Rodilla
                    \r5. Implante Cadera""" ) 
                opcion_f = int(input(""))    
            elif opcion == 2:
                pass
            
            elif opcion == 3:
                pass 

            elif opcion == 4:
                pass 
            
            elif opcion == 5:
                print("Ha salido del sistema")
                break 
            
            else:
                print("Opcion no valida, ingrese de nuevo")
                continue 
        else:
            print("Opcion no valida, ingrese de nuevo")
                continue

#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main() 