import datetime as datetime
class Implantes:

  def __init__(self, material, tamaño, medico, estado,fecha_r):
    self.__material = material
    self.__tamaño = tamaño
    self.__fecha_i = datetime.datetime.now().strftime("%d/%m/%Y")
    self.__fecha_r = fecha_r
    self.__medico = medico
    self.__revision = {} 
    self.__estado = estado
    self.__mantenimiento = ""


  def verMaterial(self):
    return self.__material
  def verTamaño(self):
    return self.__tamaño
  def verMedico(self):
    return self.__medico
  def verEstado(self):
    return self.__estado
  def verRevision(self):
    return self.__revision
  def fecha_r(self):
    return self.__fecha_r
  def fecha_i(self):
    return self.__fecha_i
  def verMantenimiento(self):
    return self.__mantenimiento

  def asignarMaterial(self, m):
    self.__material = m
  def asignarTamaño(self, t):
    self.__tamaño = t
  def asignarMedico(self, med):
    self.__tamaño = med
  def asignarEstado(self, e):
    self.__tamaño = e
  def asignarFecha_r(self, r):
    self.__fecha_r = r
  def asignarRevision(self,sis2 ,fecha, manten):
    if fecha in sis2:
      self.__revision[fecha].append(manten)     
    else:
      self.__revision[fecha] = []
      self.__revision[fecha].append(manten)
    print("mantenimiento registrado exitosamente\n")

  def asignarMantenimiento(self,m):
    self.__mantenimiento = m


class Marcapasos(Implantes):

  def __init__(self, electrodos, conectividad, frecuencia, medico, estado):
    super().__init__(None, None, medico, estado,None)
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

  def __init__(self, material, longitud, diametro,medico,estado,):
    super().__init__(material,None,medico,estado,None)
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

  def __init__(self, forma, fijacion_s, material,medico,estado):
    super().__init__(material, None, medico, estado,None)
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

  def __init__(self, material, fijacion_t, tamaño,medico,estado):
    super().__init__(material, tamaño, medico, estado, None)
    self.__fijacion_t = fijacion_t

  def verFijacion_t(self):
    return self.__fijacion_t
    
  def asignarFijacion_t(self, f):
    self.__fijacion_t = f


class ImplanteCadera(ImplanteRodilla):

  def __init__(self, material, fijacion_t, tamaño,medico,estado):
    super().__init__(material, fijacion_t, tamaño,medico,estado)


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

  def ingresarPaciente(self, paciente):
    if self.verificarPaciente(paciente):
      print("El paciente ya existe")
    else:
      self.__inventario[paciente] = []

  def agregarImplantes(self, paciente, implantes):
    if self.verificarPaciente(paciente):
      self.__inventario[paciente].append(implantes)
      print("Implante asignado al paciente correctamente\n")
    else:
      print("El paciente no existe\n")

  def eliminarImplantes(self, paciente, implantes):
    if self.verificarPaciente(paciente):
      self.__inventario[paciente].remove(implantes)
    else:
      print("El paciente no existe\n")

  def verificarImplante(self,object,tipo):
      if isinstance(object,tipo):
        return False
      return True

def main():
  sis = Sistema()
  while True:
    menu = int(
        input("""Escoja una opcion 
                            \r1. Ingresar Paciente
                            \r2. Modificar Informacion para un paciente
                            \rIngrese--> """))
    if menu == 1:
      nombre = input("ingrese nombre del paciente: ").lower()
      cc = int(input("ingrese la cedula del paciente: "))
      pac_new = Paciente(nombre, cc)
      sis.ingresarPaciente(pac_new)
      print(" Paciente Ingresado\n")
    elif menu == 2:
      name = input("Ingrese el nombre del paciente: ")
      doc = input("Ingrese el documento del paciente: ")
      inventario = sis.verInventario()
      for patient in sis.verInventario().keys():        
        if patient.verNombre().lower() == name.lower() and patient.verCedula() == int(doc):
          opcion = int(
              input("""Escoja una opcion 
                                        \r1. Agregar nuevos implantes 
                                        \r2. Eliminar implantes
                                        \r3. Editar informacion de implantes 
                                        \r4. Visualizar inventario completo
                                        \r5. Revision
                                        \r6. Mantenimiento
                                        \r7. Salir
                                        \rIngrese--> """))

          if opcion == 1:
            while True:
              print("""Protesis
                                \r1. Marcapasos 
                                \r2. Stend Coronario
                                \r3. Implante Dental
                                \r4. Implante Rodilla
                                \r5. Implante Cadera""")
              opcion_f = int(input("Seleccione el tipo de protesis que desea agregar: "))
              if opcion_f == 1:                            
                      
                      elec = input("Ingrese la cantidad de electrodos: ")
                      conec = input("Ingrese la conectividad: ")
                      frec = input("Ingrese la frecuencia: ")
                      med = input("Ingrese el medico: ")
                      est = input("Ingrese el estado: ")
                      mar = Marcapasos(elec, conec, frec,med,est)
                      sis.agregarImplantes(patient, mar)
                      subopcion = int(input("""Desea ingresar otro implante 
                                            \r1. Si 
                                            \r2. No 
                                            \rIngrese su opcion: """))
                      if subopcion == 1:
                        continue
                      elif subopcion == 2 :
                        break                     
                
              elif opcion_f == 2:                                
                    mat = input("Ingrese el material: ")
                    long = input("Ingrese la longitud: ")
                    diam = input("Ingrese el diametro: ")
                    med = input("Ingrese el medico: ")
                    est = input("Ingrese el estado: ")
                    stend = StendCoronario(mat, long, diam,med,est)
                    sis.agregarImplantes(patient, stend)
                    print("Protesis agregada correctamente ")
                    sis.agregarImplantes(patient, mar)  
                    subopcion = int(input("""Desea ingresar otro implante 
                                            \r1. Si 
                                            \r2. No 
                                            \rIngrese su opcion: """))
                    if subopcion == 1:
                        continue
                    elif subopcion == 2 :
                        break
                
              elif opcion_f == 3:
                                  
                    form = input("Ingrese la forma: ")
                    sf = input("Ingrese el sistema de fijacion: ")
                    mat = input("Ingrese el material: ")
                    med = input("Ingrese el medico: ")
                    est = input("Ingrese el estado: ")
                    im_dent = ImplanteDental(form, sf, mat,med,est)
                    sis.agregarImplantes(patient, im_dent)
                    print("Protesis agregada correctamente ")
                    subopcion = int(input("""Desea ingresar otro implante 
                                            \r1. Si 
                                            \r2. No 
                                            \rIngrese su opcion: """))
                    if subopcion == 1:
                        continue
                    elif subopcion == 2 :
                        break
                
              elif opcion_f == 4:
                                  
                    mat = input("Ingrese el material: ")
                    tf = input("Ingrese el tipo de fijacion: ")
                    tam = input("Ingrese el tamaño: ")
                    med = input("Ingrese el medico: ")
                    est = input("Ingrese el estado: ")
                    im_rod = ImplanteRodilla(mat, tf, tam,med,est)
                    sis.agregarImplantes(patient, im_rod)
                    print("Protesis agregada correctamente ")
                    subopcion = int(input("""Desea ingresar otro implante 
                                            \r1. Si 
                                            \r2. No 
                                            \rIngrese su opcion: """))
                    if subopcion == 1:
                        continue
                    elif subopcion == 2 :
                        break
                
              elif opcion_f == 5:
                                  
                    mat = input("Ingrese el material: ")
                    tf = input("Ingrese el tipo de fijacion: ")
                    tam = input("Ingrese el tamaño: ")
                    med = input("Ingrese el medico: ")
                    est = input("Ingrese el estado: ")
                    im_cad = ImplanteCadera(mat, tf, tam,med,est)
                    sis.agregarImplantes(patient, im_cad)
                    subopcion = int(input("""Desea ingresar otro implante 
                                            \r1. Si 
                                            \r2. No 
                                            \rIngrese su opcion: """))
                    if subopcion == 1:
                        continue
                    elif subopcion == 2 :
                        break
                
              else:
                print("Ingrese una opcion valida")
              
          elif opcion == 2:
            while True:
              print("""Protesis
                                  \r1. Marcapasos 
                                  \r2. Stend Coronario
                                  \r3. Implante Denal
                                  \r4. Implante Rodilla
                                  \r5. Implante Cadera""")
              opcion_f = int(
                  input("Seleccione el tipo de protesis que desea eliminar: "))
              if opcion_f == 1:
                for implante in inventario[patient][:]:                  
                  if isinstance(implante, Marcapasos):
                    sis.eliminarImplantes(patient, implante)
                    print("Marcapasos eliminado correctamente ")
                subopcion = int(input("""Desea eliminar otro implante 
                                            \r1. Si 
                                            \r2. No 
                                            \rIngrese su opcion: """))
                if subopcion == 1:
                  continue
                elif subopcion == 2 :
                  break
                
                  
              elif opcion_f == 2:
                for implante in inventario[patient][:]:
                  if isinstance(implante, StendCoronario):
                    sis.eliminarImplantes(patient, implante)
                    print("Stend coronario eliminado correctamente")
                subopcion = int(input("""Desea eliminar otro implante 
                                            \r1. Si 
                                            \r2. No 
                                            \rIngrese su opcion: """))
                if subopcion == 1:
                  continue
                elif subopcion == 2 :
                  break
              elif opcion_f == 3:
                for implante in inventario[patient][:]:
                  
                  if isinstance(implante, ImplanteDental):
                    sis.eliminarImplantes(patient, implante)
                    print("Implante dental eliminado correctamente")
                subopcion = int(input("""Desea eliminar otro implante 
                                            \r1. Si 
                                            \r2. No 
                                            \rIngrese su opcion: """))
                if subopcion == 1:
                  continue
                elif subopcion == 2 :
                  break
              elif opcion_f == 4:
                for implante in inventario[patient][:]:
                  if isinstance(implante, ImplanteRodilla):
                    sis.eliminarImplantes(patient, implante)
                    print("Implante de rodilla eliminado correctamente")
                subopcion = int(input("""Desea eliminar otro implante 
                                            \r1. Si 
                                            \r2. No 
                                            \rIngrese su opcion: """))
                if subopcion == 1:
                  continue
                elif subopcion == 2 :
                  break
              elif opcion_f == 5:
                for implante in inventario[patient][:]:
                  if isinstance(implante, ImplanteCadera):
                    sis.eliminarImplantes(patient, implante)
                    print("Implante de cadera eliminado correctamente")
                subopcion = int(input("""Desea eliminar otro implante 
                                            \r1. Si 
                                            \r2. No 
                                            \rIngrese su opcion: """))
                if subopcion == 1:
                  continue
                elif subopcion == 2 :
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
            s_opcion = int(input("Seleccione el implante a editar:"))
            if s_opcion == 1:
              for stend in inventario[patient]:
                if isinstance(stend, StendCoronario):
                  print("""Seleccione la informacion de a editar:
                                  \r1. Electrodos
                                  \r2. Conectividad    
                                  \r3. Frecuencia
                                  \r4. Medico
                                  \r5. Estado
                                  """)
                  op_m = int(input("Seleccione la opcion: "))
                  if op_m == 1:
                    mar.asignarElectrodos(input("Ingrese la cantidad de electrodos: "))
                    print("Caracteristica editada")
                    break
                  elif op_m == 2:
                    mar.asignarConectividad(input("Ingrese la conectividad: "))
                    print("Caracteristica editada")
                    break
                  elif op_m == 3:
                    mar.asignarFrecuencia(input("Ingrese la frecuencia: "))
                    print("Caracteristica editada")
                  elif op_m == 4:
                    mar.asignarMedico(input("Ingrese el medico: "))
                    print("Caracteristica editada")
                    break
                  elif op_m == 5:
                    mar.asignarEstado(input("Ingrese el estado: ")) 
                    print("Caracteristica editada")
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
                                  \r4. Medico
                                  \r5. Estado
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
                  elif op_m == 4:
                    stend.asignarMedico(input("Ingrese el medico: "))
                    break
                  elif op_m == 5:
                    stend.asignarEstado(input("Ingrese el estado: ")) 
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
                                  \r4. Medico
                                  \r5. Estado
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
                  elif op_m == 4:
                    i_d.asignarMedico(input("Ingrese el medico: "))
                    break
                  elif op_m == 5:
                    i_d.asignarEstado(input("Ingrese el estado: ")) 
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
                                    \r4. Medico
                                    \r5. Estado
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
                  elif op_m == 4:
                    i_r.asignarMedico(input("Ingrese el medico: "))
                    break
                  elif op_m == 5:
                    i_r.asignarEstado(input("Ingrese el estado: ")) 
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
                                  \r4. Medico
                                  \r5. Estado
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
                  elif op_m == 4:
                    i_c.asignarMedico(input("Ingrese el medico: "))
                    break
                  elif op_m == 5:
                    i_c.asignarEstado(input("Ingrese el estado: ")) 
                    break
                  else:
                    print("Ingrese una opcion valida")
                    break

          elif opcion == 4:
            for implante in inventario[patient]:
              if isinstance(implante, Marcapasos):
                sis2 = implante.verRevision()
                print("MARCAPASOS")
                print("Electrodos: "+implante.verElectrodos())
                print("Conectividad: "+implante.verConectividad())
                print("Frecuencia: "+implante.verFrecuencia())                
                for key in sis2.keys():
                  for n in  sis2[key]:
                    print(f'{key}: {n}')
                print("")
                continue
              elif isinstance(implante, StendCoronario):
                sis2 = implante.verRevision()
                print("STEND CORONARIO")
                print("Longitud: "+implante.verLongitud())
                print("Diametro: "+implante.verDiametro())
                print("Material: "+implante.verMaterial())
                for key in sis2.keys():
                  for n in  sis2[key]:
                    print(f'{key}: {n}')
                print("")
                continue
              elif isinstance(implante, ImplanteDental):
                sis2 = implante.verRevision()
                print("IMPLANTE DENTAL")
                print("Forma: "+implante.verForma())
                print("Fijacion: "+implante.verFijacion_s())
                print("Material: "+implante.verMaterial())
                for key in sis2.keys():
                  for n in  sis2[key]:
                    print(f'{key}: {n}')
                print("")
                continue
              elif isinstance(implante, ImplanteRodilla):
                sis2 = implante.verRevision()
                print("IMPLANTE RODILLA")
                print("Material: "+implante.verMaterial())
                print("Fijacion: : "+implante.verFijacion_t())
                print("Tamaño: "+implante.verTamaño())
                for key in sis2.keys():
                  for n in  sis2[key]:
                    print(f'{key}: {n}')
                print("")
                continue
              elif isinstance(implante, ImplanteCadera):
                sis2 = implante.verRevision()
                print("IMPLANTE CADERA")
                print("Material: "+implante.verMaterial())
                print("Fijacion: "+implante.verFijacion_t())
                print("Tamaño: "+implante.verTamaño())
                for key in sis2.keys():
                  for n in  sis2[key]:
                    print(f'{key}: {n}')
                print("")
                continue
          elif opcion == 5:
            selec = int(
              input("""Tipo de Implante:
                                \r1. Marcapasos 
                                \r2. Stend Coronario
                                \r3. Implante Dental
                                \r4. Implante Rodilla
                                \r5. Implante Cadera
                    \rIngrese una opcion:"""))
            if selec == 1:
              for mar in inventario[patient]:
                if isinstance(mar, Marcapasos):
                  sis2 = mar.verRevision()
                  fecha_revision = (f'{datetime.datetime.now().strftime("%d/%m/%Y")}')
                  mantenimiento = input("Ingrese la revision realizada al implante: ")
                  mar.asignarRevision(sis2,fecha_revision,mantenimiento)
            elif selec == 2:
              for ste in inventario[patient]:
                if isinstance(ste, StendCoronario):
                  sis2 = ste.verRevision()
                  ste.verRevision()
                  fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                  mantenimiento = input("Ingrese la revision realizada al implante: ")
                  ste.asignarRevision(sis2,fecha_revision,mantenimiento)
            elif selec == 3:
              for impd in inventario[patient]:
                if isinstance(impd, ImplanteDental):
                  sis2 = impd.verRevision()
                  impd.verRevision()
                  fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                  mantenimiento = input("Ingrese la revision realizada al impdlante: ")
                  impd.asignarRevision(sis2,fecha_revision,mantenimiento)
            elif selec == 4:
              for impr in inventario[patient]:
                if isinstance(impr, ImplanteRodilla):
                  sis2 = impr.verRevision()
                  impr.verRevision()
                  fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                  mantenimiento = input("Ingrese la revision realizada al implante: ")
                  impr.asignarRevision(sis2,fecha_revision,mantenimiento)
            elif selec == 5:
              for ic in inventario[patient]:
                if isinstance(ic, ImplanteCadera):
                  sis2 = ic.verRevision()
                  ic.verRevision()
                  fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                  mantenimiento = input("Ingrese la revision realizada al implante: ")
                  ic.asignarRevision(sis2,fecha_revision,mantenimiento)

          elif opcion == 6:
              while True:
                print("""Protesis
                                        \r1. Marcapasos 
                                        \r2. Stend Coronario
                                        \r3. Implante Dental
                                        \r4. Implante Rodilla
                                        \r5. Implante Cadera""")
                s_opcion = input("Seleccione la opcion deseada: ")
                if s_opcion == 1:
                  for mar in inventario[patient]:
                    if isinstance(mar, Marcapasos):
                      mantenimiento = input("Ingrese mantenimiento: ")
                      mar.asignarMantenimiento(mantenimiento)
                      subopcion = int(input("""Desea realizar otro mantenimiento
                                              \r1. Si 
                                              \r2. No 
                                              \rIngrese su opcion: """))
                      if subopcion == 1:
                        continue
                      elif subopcion == 2 :
                        break
                elif s_opcion == 2:
                    for ste in inventario[patient]:
                      if isinstance(ste, StendCoronario):
                        mantenimiento = input("Ingrese mantenimiento: ")
                        ste.asignarMantenimiento(mantenimiento)
                        subopcion = int(input("""Desea realizar otro mantenimiento
                                                \r1. Si 
                                                \r2. No 
                                                \rIngrese su opcion: """))
                        if subopcion == 1:
                          continue
                        elif subopcion == 2 :
                          break

                elif s_opcion == 3:
                    for i_d in inventario[patient]:
                      if isinstance(i_d, ImplanteDental):
                        mantenimiento = input("Ingrese mantenimiento: ")
                        i_d.asignarMantenimiento(mantenimiento)
                        subopcion = int(input("""Desea realizar otro mantenimiento
                                                \r1. Si 
                                                \r2. No 
                                                \rIngrese su opcion: """))
                        if subopcion == 1:
                          continue
                        elif subopcion == 2 :
                          break
                elif s_opcion == 4:
                    for i_r in inventario[patient]:
                      if isinstance(i_r, ImplanteRodilla):
                        mantenimiento = input("Ingrese mantenimiento: ")
                        i_r.asignarMantenimiento(mantenimiento)
                        subopcion = int(input("""Desea realizar otro mantenimiento
                                                \r1. Si 
                                                \r2. No 
                                                \rIngrese su opcion: """))
                        if subopcion == 1:
                          continue
                        elif subopcion == 2 :
                          break
                elif s_opcion == 5:
                    for i_c in inventario[patient]:
                      if isinstance(i_c, ImplanteCadera):
                        mantenimiento = input("Ingrese mantenimiento: ")
                        i_c.asignarMantenimiento(mantenimiento)
                        subopcion = int(input("""Desea realizar otro mantenimiento
                                                \r1. Si 
                                                \r2. No 
                                                \rIngrese su opcion: """))
                        if subopcion == 1:
                          continue
                        elif subopcion == 2 :
                          break
                
          elif opcion == 7:
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

