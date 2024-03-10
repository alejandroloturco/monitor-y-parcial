import datetime as datetime


class Implantes:

  def __init__(self, material, tamaño, medico, estado):
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

  def asignarMaterial(self, m):
    self.__material = m

  def asignarTamaño(self, t):
    self.__tamaño = t

  def asignarMedico(self, med):
    self.__tamaño = med

  def asignarEstado(self, e):
    self.__tamaño = e


class Marcapasos(Implantes):

  def __init__(self, electrodos, conectividad, frecuencia):
    super().__init__(None, None, None, None)
    self.__electrodos = electrodos
    self.__conectividad = conectividad
    self.__frecuencia = frecuencia

  def verElectrodos(self):
    return self.__electrodos

  def verConectividad(self):
    return self.__conectividad

  def verFrecuencia(self):
    return self.__frecuencia

  def asignarElectrodos(self, e):
    self.__electrodos = e

  def asignarConectividad(self, c):
    self.__conectividad = c

  def asignarFrecuencia(self, f):
    self.__frecuencia = f


class StendCoronario(Implantes):

  def __init__(self, material, longitud, diametro):
    super().__init__(material, None, None, None)
    self.__longitud = longitud
    self.__diametro = diametro

  def verLongitud(self):
    return self.__longitud

  def verDiametro(self):
    return self.__diametro

  def asignarLongitud(self, l):
    self.__longitud = l

  def asignarDiametro(self, d):
    self.__diametro = d


class ImplanteDental(Implantes):

  def __init__(self, forma, fijacion_s, material):
    super().__init__(material, None, None, None)
    self.__forma = forma
    self.__fijacion_s = fijacion_s

  def verForma(self):
    return self.__forma

  def verFijacion_s(self):
    return self.__fijacion_s

  def asignarForma(self, f):
    self.__forma = f

  def asignarFijacion_s(self, f):
    self.__fijacion_s = f


class ImplanteRodilla(Implantes):

  def __init__(self, material, fijacion_t, tamaño):
    super().__init__(material, tamaño, None, None)
    self.__fijacion_t = fijacion_t

  def verFijacion_t(self):
    return self.__fijacion_t

  def asignarFijacion_t(self, f):
    self.__fijacion_t = f


class ImplanteCadera(ImplanteRodilla):

  def __init__(self, material, fijacion_t, tamaño):
    super().__init__(material, fijacion_t, tamaño)


class Paciente():

  def __init__(self, nombre, cedula):
    self.__nombre = nombre
    self.__cedula = cedula

  def verNombre(self):
    return self.__nombre

  def verCedula(self):
    return self.__cedula

  def asignarNombre(self, n):
    self.__nombre = n

  def asignarCedula(self, c):
    self.__cedula = c


class Sistema:

  def __init__(self):
    self.__inventario = {}

  def verInventario(self):
    return self.__inventario

  def verificarPaciente(self, paciente):
    if paciente in self.__inventario:
      return True
    return False

  def verificarImplante(self, implante):
    if implante in self.__inventario:
      return True
    return False

  def ingresarPaciente(self, paciente):
    if self.verificarPaciente(paciente):
      print("El paciente ya existe")
    else:
      self.__inventario[paciente] = []

  def agregarImplantes(self, paciente, implantes):
    if self.verificarPaciente(paciente):
      self.__inventario[paciente].append(implantes)
    else:
      print("El paciente no existe")

  def eliminarImplantes(self, paciente, implantes):
    if self.verificarPaciente(paciente):
      self.__inventario[paciente].remove(implantes)
    else:
      print("El paciente no existe")


def main():
  sis = Sistema()
  while True:
    menu = int(
        input("""Escoja una opcion 
                            \r1. Ingresar Paciente
                            \r2. Modificar Informacion para un paciente
                            \rIngrese--> """))
    if menu == 1:
      nombre = input("ingrese nombre del paciente: ")
      cc = int(input("ingrese la cedula del paciente: "))
      pac_new = Paciente(nombre, cc)
      sis.ingresarPaciente(pac_new)
      print("Paciente Ingresado")
    elif menu == 2:
      name = input("Ingrese el nombre del paciente: ")
      doc = input("Ingrese el docuemnto del paciente: ")
      inventario = sis.verInventario()
      for patient in sis.verInventario().keys():
        if patient.verNombre().lower() == name.lower() and patient.verCedula() == int(doc):
          opcion = int(
              input("""Escoja una opcion 
                                        \r1. Agregar nuevos implantes 
                                        \r2. Eliminar implantes✅
                                        \r3. Editar informacion de implantes ✅
                                        \r4. Visualizar inventario completo✅
                                        \r5. Salir✅
                                        \rIngrese--> """))

          if opcion == 1:
            print("""Protesis
                              \r1. Marcapasos 
                              \r2. Stend Coronario
                              \r3. Implante Dental
                              \r4. Implante Rodilla
                              \r5. Implante Cadera""")
            opcion_f = int(
                input("Seleccione el tipo de protesis que desea agregar: "))
            if opcion_f == 1:
              elec = int(input("Ingrese la cantidad de electrodos: "))
              conec = input("Ingrese la conectividad: ")
              frec = int(input("Ingrese la frecuencia: "))
              mar = Marcapasos(elec, conec, frec)
              sis.agregarImplantes(patient, mar)
              break
            elif opcion_f == 2:
              mat = input("Ingrese el material: ")
              long = int(input("Ingrese la longitud: "))
              diam = int(input("Ingrese el diametro: "))
              stend = StendCoronario(mat, long, diam)
              sis.agregarImplantes(patient, stend)
              break
            elif opcion_f == 3:
              form = input("Ingrese la forma: ")
              sf = input("Ingrese el sistema de fijacion: ")
              mat = input("Ingrese el material: ")
              im_dent = ImplanteDental(form, sf, mat)
              sis.agregarImplantes(patient, im_dent)
              break
            elif opcion_f == 4:
              mat = input("Ingrese el material: ")
              tf = input("Ingrese el tipo de fijacion: ")
              tam = int(input("Ingrese el tamaño: "))
              im_rod = ImplanteRodilla(mat, tf, tam)
              sis.agregarImplantes(patient, im_rod)
              break
            elif opcion_f == 5:
              mat = input("Ingrese el material: ")
              tf = input("Ingrese el tipo de fijacion: ")
              tam = int(input("Ingrese el tamaño: "))
              im_cad = ImplanteCadera(mat, tf, tam)
              sis.agregarImplantes(patient, im_cad)
              break
            else:
              print("Ingrese una opcion valida")

          elif opcion == 2:
            print("""Protesis
                                \r1. Marcapasos 
                                \r2. Stend Coronario
                                \r3. Implante Denal
                                \r4. Implante Rodilla
                                \r5. Implante Cadera""")
            opcion_f = int(
                input("Seleccione el tipo de protesis que desea eliminar: "))
            if opcion_f == 1:
              for implante in inventario[patient]:
                if isinstance(implante, Marcapasos):
                  sis.eliminarImplantes(patient, implante)
                  break
            elif opcion_f == 2:
              for implante in inventario[patient]:
                if isinstance(implante, StendCoronario):
                  sis.eliminarImplantes(patient, implante)
                  break
            elif opcion_f == 3:
              for implante in inventario[patient]:
                if isinstance(implante, ImplanteDental):
                  sis.eliminarImplantes(patient, implante)
                  break
            elif opcion_f == 4:
              for implante in inventario[patient]:
                if isinstance(implante, ImplanteRodilla):
                  sis.eliminarImplantes(patient, implante)
                  break
            elif opcion_f == 5:
              for implante in inventario[patient]:
                if isinstance(implante, ImplanteCadera):
                  sis.eliminarImplantes(patient, implante)
                  break
            else:
              print("Ingrese una opcion valida")
              break

          elif opcion == 3:
            print("""Tipo de Implante:
                                \r1. Marcapasos 
                                \r2. Stend Coronario
                                \r3. Implante Denal
                                \r4. Implante Rodilla
                                \r5. Implante Cadera""")
            s_opcion = int(input("Seleccione el implante:"))
            if s_opcion == 1:
              for mar in inventario[patient]:
                if isinstance(mar, Marcapasos):
                  print("""Seleccione la informacion de a editar:
                                  \r1. Electrodos
                                  \r2. Conectividad    
                                  \r3. Frecuencia
                                  """)
                  op_m = int(input("Seleccione la opcion: "))
                  if op_m == 1:
                    mar.asignarElectrodos(
                        int(input("Ingrese la cantidad de electrodos: ")))
                    break
                  elif op_m == 2:
                    mar.asignarConectividad(input("Ingrese la conectividad: "))
                    break
                  elif op_m == 3:
                    mar.asignarFrecuencia(int(
                        input("Ingrese la frecuencia: ")))
                    break
                  else:
                    print("Ingrese una opcion valida")
                    break
                  
            elif s_opcion == 2:
              for stend in inventario[patient]:
                if isinstance(stend, StendCoronario):
                  print("""informacion a editar:
                                  \r1. Longitud
                                  \r2. Diametro    
                                  \r3. Material
                                  """)
                  op_s = int(input("Seleccione la opcion:"))
                  if op_s == 1:
                    stend.asignarLongitud(int(input("Ingrese la longitud:")))
                    break
                  elif op_s == 2:
                    stend.asignarDiametro(int(input("Ingrese el diametro: ")))
                    break
                  elif op_s == 3:
                    stend.asignarMaterial(input("Ingrese el material:"))
                    break
                  else:
                    print("Ingrese una opcion valida")
                    break

            elif s_opcion == 3:
              for i_d in inventario[patient]:
                if isinstance(i_d, ImplanteDental):
                  print("""Informacion a editar:
                                  \r1. Forma
                                  \r2. Sistema de fijacion    
                                  \r3. Material
                                  """)
                  op_id = int(input("Seleccione la opcion:"))
                  if op_id == 1:
                    i_d.asignarForma(input("Ingrese la forma:"))
                    break
                  elif op_id == 2:
                    i_d.asignarFijacion_s(
                        input("Ingrese el sistema de fijacion: "))
                    break
                  elif op_id == 3:
                    i_d.asignarMaterial(input("Ingrese el material:"))
                    break
                  else:
                    input("Ingrese una opcion valida")
                    break

            elif s_opcion == 4:
              for i_r in inventario[patient]:
                if isinstance(i_r, ImplanteRodilla):
                  print("""Informacion a editar:
                                    \r1. Material
                                    \r2. Tipo de fijacion  
                                    \r3. Tamaño
                                    """)
                  op_ir = int(input("Seleccione la opcion:"))
                  if op_ir == 1:
                    i_r.asignarMaterial(input("Ingrese el material:"))
                    break
                  elif op_ir == 2:
                    i_r.asignarFijacion_t(
                        input("Ingrese el tipo de fijacion: "))
                    break
                  elif op_ir == 3:
                    i_r.asignarTamaño(int(input("Ingrese el tamaño:")))
                    break
                  else:
                    print("Ingrese una opcion valida")
                    break

            elif s_opcion == 5:
              for i_c in inventario[patient]:
                if isinstance(i_c, ImplanteCadera):
                  print("""Informacion a editar:
                                  \r1. Material
                                  \r2. Tipo de fijacion  
                                  \r3. Tamaño
                                  """)
                  op_ic = int(input("Seleccione la opcion:"))
                  if op_ic == 1:
                    i_c.asignarMaterial(input("Ingrese el material:"))
                    break
                  elif op_ic == 2:
                    i_c.asignarFijacion_t(
                        input("Ingrese el tipo de fijacion: "))
                    break
                  elif op_ic == 3:
                    i_c.asignarTamaño(int(input("Ingrese el tamaño:")))
                    break

          elif opcion == 4:
            for implante in inventario[patient]:
              if isinstance(implante, Marcapasos):
                print(implante.verElectrodos())
                print(implante.verConectividad())
                print(implante.verFrecuencia())
                continue
              elif isinstance(implante, StendCoronario):
                print(implante.verLongitud())
                print(implante.verDiametro())
                print(implante.verMaterial())
                continue
              elif isinstance(implante, ImplanteDental):
                print(implante.verForma())
                print(implante.verFijacion_s())
                print(implante.verMaterial())
                continue
              elif isinstance(implante, ImplanteRodilla):
                print(implante.verMaterial())
                print(implante.verFijacion_t())
                print(implante.verTamaño())
                continue
              elif isinstance(implante, ImplanteCadera):
                print(implante.verMaterial())
                print(implante.verFijacion_t())
                print(implante.verTamaño())
                continue

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
