import datetime as datetime

class Implantes:
    def __init__(self,material,tamaño,medico,estado):
        self.__material = material
        self.__tamaño = tamaño
        self.__fecha = datetime.datetime.now().strftime("%d/%m/%Y")
        self.__medico = medico
        self.__estado = estado
      
    def verMaterial(self):
        return self.__material
    def verTamaño(self):
        return self.__tamaño
    def verMedico(self):
      return self.__medico
    def verEstado(self):
      return self.__estado
    
    def asignarMaterial(self,m):
        self.__material = m
    def asignarTamaño(self,t):
        self.__tamaño = t    
    def asignarMedico(self,med):
        self.__tamaño = med
    def asignarEstado(self,e):
        self.__tamaño = e    

class Marcapasos(Implantes):
  def __init__(self,electrodos,conectividad,frecuencia)
    super().__init__(None,None,None,None)
    self.__electrodos = electrodos
    self.__conectividad = conectividad
    self.__frecuencia = frecuencia
    
  def verElectrodos(self):
    return self.__electrodos
  def verConectividad(self):
    return self.__conectividad
  def verFrecuencia(self):
    return self.__frecuencia
    
  def asignarElectrodos(self,e):
    self.__electrodos = e
  def asignarConectividad(self,c):
    self.__conectividad = c
  def asignarFrecuencia(self,f):
    self.__frecuencia = f

class StendCoronario(Implantes):
  def __init__(self,material,longitud,diametro):
      super().__init__(material,None,None,None)
      self.__longitud = longitud
      self.__diametro = diametro
    
  def verLongitud(self):
    return self.__longitud
  def verDiametro(self):
    return self.__diametro
    
  def asignarLongitud(self,l): 
    self.__longitud = l
  def asignarDiametro(self,d):
    self.__diametro = d                             

class ImplanteDental(Implantes):
  def __init__(self,forma,fijacion_s,material):
      super().__init__(material,None,None,None)
      self.__forma = forma
      self.__fijacion_s = fijacion_s
    
  def verForma(self):
      return self.__forma
    
  def asignarFijacion_s(self,f):
      self.__fijacion_s = f

class ImplanteRodilla(Implantes):
  def __init__(self,material,fijacion_t,tamaño):
      super().__init__(material,tamaño,None,None)
      self.__fijacion = fijacion_t
    
  def verFijacion(self):
      return self.__fijacion_t
    
  def asignarFijacion(self,f):
      self.__fijacion_t = f

class ImplanteCadera(ImplanteRodilla):
  def __init__(self,material,fijacion_t,tamaño):
      super().__init__(material,fijacion_t,tamaño)

class Paciente():
  def __init__(self,nombre,cedula):
      self.__nombre = nombre
      self.__cedula = cedula

  def verNombre(self):
      return self.__nombre
  def verCedula(self):
      return self.__cedula

  def asignarNombre(self,n):
      self.__nombre = n
  def asignarCedula(self,c):
      self.__cedula = c
  
class Sistema:
  def __init__(self):
      self.__inventario = {} 
  def verInventario(self):
    return self.__inventario   
    
  def verificarExiste(self,paciente):
    if paciente in self.__inventario:
        return True
    return False

  def verificarExiste2(self,implante):
    if implante in self.__inventario:
        return True
    return False
    
  def ingresarPaciente(self,paciente):
    if self.verificarExiste(paciente):
        print("El paciente ya existe")
    else:
        self.__inventario[paciente] = []            

  def agregarImplantes(self,paciente,implantes):
    if self.verificarExiste(paciente):
        self.__inventario[paciente].append(implantes)
    else:
        print("El paciente no existe")

  def editarImplantes(self,paciente,implante):
    if self.verificarExiste(paciente):
      x = self.__inventario[paciente]
      for i in x:
        if i == implantes
    else:
        print("El paciente no existe")
      
  def eliminarImplantes(self,paciente,implantes):
    if self.verificarExiste(paciente):
        self.__inventario[paciente].remove(implantes)
    else:
        print("El paciente no existe")
      
   
            


  

def main():
  sis = Sistema()     
  while True:
      menu = int(input("""Escoja una opcion 
                      \r1. Ingresar Paciente
                      \r2. Modificar Informacion para un paciente
                      \rIngrese--> """))
      if menu == 1:
        nombre = input("ingrese nombre del paciente: ")
        cc = int(input("ingrese la cedula del paciente: ")        )
        pac = Paciente(nombre,cc)
        sis.ingresarPaciente(pac)
        print("Paciente Ingresado")
      elif menu ==2:
          opcion = int(input("""Escoja una opcion 
                          \r1. Agregar nuevos implantes 
                          \r2. Eliminar implantes
                          \r3. Editar informacion de implantes
                          \r4. Visualizar inventario completo
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


if __name__ == "__main__":
  main() 

