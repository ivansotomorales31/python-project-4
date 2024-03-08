inventario_vehiculos = {}
Registro_Cedulas = []

def agregar_vehiculo(marca, año, modelo, cilindraje, precio_alquiler, precio_vehiculo, placa, cantidad):
    if placa not in inventario_vehiculos:
        inventario_vehiculos[placa] = {'marca': marca,
                                        'año': año,
                                        'modelo': modelo,
                                        'cilindraje': cilindraje,
                                        'precio_alquiler': precio_alquiler,
                                        'precio_vehiculo': precio_vehiculo,
                                        'cantidad_disponible': cantidad,
                                        'habilitado': True}
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

def menu_administrador():
    opc = ""
    while opc != "3":
        print()
        print("-----Menu-----")
        print("[1] Gestion inventario Vehiculos")
        print("[2] Gestion de clientes")
        print("[3] Visualizar vehiculos ")
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
                agregar_vehiculo(Marca, Año, Modelo, cilindraje, Precio_alquiler, Precio_auto, placa, cantidad)
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
            
            elif cli_opc == "2":
                print("Iniciar sesion")
                Nombre = input("Ingrese su nombre:")
                NumCedula = input("Ingrese su numero de cedula:")

                if NumCedula in Registro_Cedulas:
                    print("Bienvenido de nuevo",Nombre)
                
                else:
                    print("Cedula no encontrada, porfavor registrese")
                    Registro_Cedulas.append(NumCedula)
                    Nombre = input("Ingrese su nombre:")
                    Telefono = input("Ingrese su numero de telefono:")
                    print("Se registro correctamente ")

        elif opc == "3":
            print("Visualizar vehículos")
            for i in inventario_vehiculos:
                print(i)
            print("Estos son los vehiculos")

menu_administrador()