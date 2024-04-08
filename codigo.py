inventario_vehiculos = {}
Registro_Cedulas = []
reserva = []

sede_San_José=[["Registro de Tiempos"],["Registro De autos"] ]
sede_Alajuela=[ ["Registro de Tiempos"],["Registro De autos"]]
sede_Guanacaste=[ ["Registro de Tiempos"],["Registro De autos"]]
sede_Limón=[["Registro de Tiempos"],["Registro De autos"] ]
sede_Puntarenas=[ ["Registro de Tiempos"],["Registro De autos"]]
sede_Pérez_Zeledón=[["Registro de Tiempos"],["Registro De autos"] ]
sedes_Lista=[sede_San_José,sede_Alajuela,sede_Guanacaste,sede_Limón,sede_Puntarenas,sede_Pérez_Zeledón]



def Definir_Sede():
    import time
    print ("Horas Actuales \n",time.strftime("%H:%M:%S") )
    print ("",time.strftime("%I:%M:%S") )
    tiempo_actual=int(time.strftime("%H"))
    print("----------------------")
    print("---horario de sedes---")
    print("1. San José: 24 horas, los 7 días de la semana.")
    print("2. Alajuela: 24 horas, los 7 días de la semana.")
    print("3. Guanacaste: Abren a las 4 am, cierran a las 11 pm.")
    print("4. Limón: Abren a las 6 am, cierran a las 10 pm.")
    print("5. Puntarenas: Abren a las 5 am, cierran a las 10 pm.")
    print("6. Pérez Zeledón: Abren a las 7 am, cierran a las 10 pm.")
    print("----------------------")
    print("----------------------")
          
    print("Porfavor seleccione la sede en la que se encuentra del 1 al 6: ")
    print("1. San José")
    print("2. Alajuela")
    print("3. Guanacaste")
    print("4. Limón")
    print("5. Puntarenas")
    print("6. Pérez Zeledón")
    sede_destino=int(input())
    
    if sede_destino==1:
        menu_administrador(sedes_Lista[0],tiempo_actual)
        
    elif sede_destino==2 : 
        menu_administrador(sedes_Lista[1],tiempo_actual)
         
    elif sede_destino==3 :
        if  tiempo_actual>3 and tiempo_actual<23:
            menu_administrador(sedes_Lista[2],tiempo_actual)
        else:
            print("sede de Guanacaste: Abren a las 4 am, cierran a las 11 pm.\n Ahora debe estar serrado, disculpas")
         
    elif sede_destino==4 :
        if tiempo_actual>5 and tiempo_actual<22:
            menu_administrador(sedes_Lista[3],tiempo_actual)
        else:
            print("Sede de Limón: Abren a las 6 am, cierran a las 10 pm.\n Ahora debe estar serrado, disculpas")
         
    elif sede_destino==5 :
        if tiempo_actual>4 and tiempo_actual<22:
            menu_administrador(sedes_Lista[4],tiempo_actual)
        else:
            print("Sede de Puntarenas: Abren a las 5 am, cierran a las 10 pm.\n Ahora debe estar serrado, disculpas")
         
    elif sede_destino==6 : 
        if tiempo_actual>6 and tiempo_actual<22:
            menu_administrador(sedes_Lista[5],tiempo_actual)
        else:
            print("Sede de Pérez Zeledón: Abren a las 7 am, cierran a las 10 pm.\n Ahora debe estar serrado, disculpas")
    else:
        print("Sede inexistente,una disculpa")
    

def agregar_vehiculo(marca, año, modelo, cilindraje, precio_alquiler, precio_vehiculo, placa, cantidad,Sede):
    if placa not in inventario_vehiculos:
        inventario_vehiculos[placa] = {'marca': marca,
                                        'año': año,
                                        'modelo': modelo,
                                        'cilindraje': cilindraje,
                                         'precio_alquiler': precio_alquiler,
                                        'precio_vehiculo': precio_vehiculo,
                                        'cantidad_disponible': cantidad,
                                        'habilitado': True}
        Sede[1].append(inventario_vehiculos[placa])
        
        print("Vehiculo agregado exitosamente")
         
def reservar_vehiculo(placa, cantidad):
    if placa in inventario_vehiculos:
        if inventario_vehiculos[placa]['habilitado']:
            if inventario_vehiculos[placa]['cantidad_disponible'] >= cantidad:
                inventario_vehiculos[placa]['cantidad_disponible'] -= cantidad
                print("Reserva realizada correctamente.")
            else:
                print("No hay suficientes vehiculos ")
        else:
            print("El vehiculo esta inhabilitado.")
    else:
        print("No existe ningun vehiculo con esa placa.")

def inhabilitar_vehiculo(placa):
    if placa in inventario_vehiculos:
        inventario_vehiculos[placa]['habilitado'] = False
        print("Vehiculo inhabilitado correctamente.")
    else:
        print("No se encontro ningun vehiculo con esa placa.")

def menu_administrador(Sede,tiempo_actual):
    import time
    Hora_entrada= time.strftime("%H:%M:%S")
    Sede[0].append(Hora_entrada)
    
    opc = ""
    while opc != "4":
        Hora_Salida_Calcu=int(time.strftime("%H"))
        print()
        print("Hora de entrada:",time.strftime("%I:%M:%S"))
        print("-----Menu-----")
        print("[1] Gestion inventario Vehiculos")
        print("[2] Gestion de clientes")
        print("[3] Visualizar vehiculos ")
        print("[4] Gestión de sedes")
        opc = input("Seleccione una opcion: ")

        if opc == "1":
            print("----Gestion inventario vehiculos---")
            print("[1] Agregar vehiculos")
            print("[2] Inhabilitar vehiculos")
            opc_inventario = input("Seleccione una opcion: ")

            if opc_inventario == "1":
                print()
                print("Agrega el vehiculo que deseas")
                Marca = input("Ingrese la marca del vehiculo: ")
                Año = input("Ingrese el año del vehiculo: ")
                Modelo = input("Ingrese el modelo del vehiculo: ")
                cilindraje = input("Ingrese el cilindraje del modelo: ")
                Precio_alquiler = float(input("Ingrese el precio de al alquiler: "))
                Precio_auto = float(input("Ingrese el precio del auto: "))
                placa = input("Ingrese el numero de placa")
                cantidad = float(input("Ingrese la cantidad de vehiculos disponibles"))
                agregar_vehiculo(Marca, Año, Modelo, cilindraje, Precio_alquiler, Precio_auto, placa, cantidad,Sede)
            elif opc_inventario == "2":
                placa = input("Ingrese la placa del vehiculo a inhabilitar: ")
                inhabilitar_vehiculo(placa)

        elif opc == "2":
            print("Gestion de clientes")
            print("----Menu-----")
            print("[1] Ingresar como invitado")
            print("[2] Ingresar como cliente registrado")
            cli_opc = input("Seleccione una opcion para la gestion de clientes: ")

            if cli_opc == "1":
                print("Cliente invitado")
                print("Seleccione una opcion")
                print("[1] Ver un listado de marcas de vehiculo")
                print("[2] Ver un listado de reservas")
                reserva = input("Seleccione que desear ver")

            elif cli_opc == "2":
                print("Iniciar sesion")
                Nombre = input("Ingrese su nombre:")
                NumCedula = input("Ingrese su numero de cedula:")

                if NumCedula in Registro_Cedulas:
                    print("Bienvenido de nuevo",Nombre)
                    print("Seleccione una opcion")
                    print("[1] Ver un listado de marcas de vehiculo")
                    print("[2] Ver un listado de reservas")
                    reserva = input("Seleccione la opcion que deseas ver")
                    print("")
                
                else:
                    print("Cedula no encontrada, porfavor registrese")
                    Registro_Cedulas.append(NumCedula)
                    Nombre = input("Ingrese su nombre:")
                    Telefono = input("Ingrese su numero de telefono:")
                    print("Se registro correctamente ")

        elif opc == "3":
            print("Visualizar vehículos")
            i= Sede[1]
            for e in i:
                print(e)
            print("Estos son los vehiculos")
            
        elif opc == "4":
            eleccion_Sede=int(input("Elija una opcion: \n [1]Cambiar de sede \n [2] Ver resgistro de entrada y salida"))
            if eleccion_Sede==1:
                print("Cambiar de sede")
                print("Hora de salida",time.strftime("%I:%M:%S") )
                Hora_Salida=time.strftime("%H:%M:%S")
                Sede[0].append(Hora_Salida)
                break
            if eleccion_Sede==2:
                print(Sede[0])
            
        else:
            print("Opción inválida")
 
        if Sede==sedes_Lista[2] and (tiempo_actual+Hora_Salida_Calcu>23 or tiempo_actual+Hora_Salida_Calcu==23):
            Hora_Salida=time.strftime("%H:%M:%S")
            Sede[0].append(Hora_Salida)
            break

        elif Sede==sedes_Lista[3] and (tiempo_actual+Hora_Salida_Calcu>22 or tiempo_actual+Hora_Salida_Calcu==22):
            Hora_Salida=time.strftime("%H:%M:%S")
            Sede[0].append(Hora_Salida)
            break

        elif Sede==sedes_Lista[4] and (tiempo_actual+Hora_Salida_Calcu>22 or tiempo_actual+Hora_Salida_Calcu==22):
            Hora_Salida=time.strftime("%H:%M:%S")
            Sede[0].append(Hora_Salida)
            break

        elif Sede==sedes_Lista[5] and (tiempo_actual+Hora_Salida_Calcu>22 or tiempo_actual+Hora_Salida_Calcu==22):
            Hora_Salida=time.strftime("%H:%M:%S")
            Sede[0].append(Hora_Salida)
            break


while True:
    Definir_Sede()


