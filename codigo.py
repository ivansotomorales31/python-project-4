Num_Vehiculo = []
Registro_Cedulas = []
opc = 0

while opc != "1":
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
        opc = input("Seleccione una opcion: ")

        if opc == "1":
            print()
            print("Agrega el vehiculo que deseas")
            Marca = input("Ingrese la marca del vehiculo: ")
            Año = input("Ingrese el año del vehiculo: ")
            Modelo = input("Ingrese el modelo del vehiculo: ")
            cilindraje = input("Ingrese el cilindraje del modelo: ")
            Precio_alquiler = float(input("Ingrese el precio de al alquiler: "))
            Precio_auto = float(input("Ingrese el precio del auto: "))
            placa = input("Ingrese el numero de placa")

            Num_Vehiculo = [Marca, Año, Modelo, cilindraje, Precio_alquiler, Precio_auto]
            print(Num_Vehiculo)
            print("Vehiculo agregado con exito ")

        elif opc == "2":
            print("Inhabilitar vehiculos")
            print("----Menu-----")
            print("[1] Vehiculo dañado ")
            print("[2] Vehiculo reservado")

    elif opc == "2":
        print("Gestion de clientes")
        print("----Menu-----")
        print("[1] Ingresar como invitado")
        print("[2] Ingresar como cliente registrado")
        cli_opc = input("Seleccione una opción para la gestión de clientes: ")

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

