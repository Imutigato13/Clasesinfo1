cantidad_pacientes = 0
edades = []
lista_global = []
lista_individual = []
lista_perros = []
lista_gatos = []
criticos = 0
graves = 0
while True:

    print("Bienvenido a nuestra veterinaria :D".center(50))

    des = int(input("""
                        \r1- Ingresar una nueva mascota
                        \r2- Cuantos pacientes estan ingresados
                        \r3- Promedio de edades
                        \r4- Cantidad de mascotas graves y criticas
                        \r5- Buscar una mascota 
                        \r6- Mostrar todas las mascotas ingresadas
                        \r7- Salir
                        \r """))
    if des == 1:
        while True:
            
            cantidad_pacientes += 1

            nombre = str(input("¿Cual es el nombre de su mascota?: ")).lower()

            while True:
                especie = str(input("¿Cual es la especie del animal?: ")).lower()
                if especie == "gato":
                    break
                elif especie == "perro":
                    break
                else:
                    print("Solo admitimos gatos o perros en nuestra veterinaria, porfavor digite la palabra gato o perro solamente")
                    continue

            edad = int(input(f"¿Cual es la edad del {especie} ingresado?: "))
            edades.append(edad)

            while True:
                estado = str(input(f"¿Cual es el estado del {especie} ingresado?: ")).lower()
                if estado == "critico":
                    criticos += 1
                    break
                elif estado == "grave":
                    graves += 1
                    break
                else:
                    print("Digite si su mascota esta en estado critico o grave solamente")
                    continue

            if cantidad_pacientes < 10 and especie == "gato":
                codigo = "Fel00" + str(cantidad_pacientes)

            elif cantidad_pacientes < 10 and especie == "perro":
                codigo = "Can00"+ str(cantidad_pacientes)
            
            elif cantidad_pacientes < 100 and cantidad_pacientes >= 10 and especie == "gato":
                codigo = "Fel0"+ str(cantidad_pacientes)
            
            elif cantidad_pacientes < 100 and cantidad_pacientes >= 10 and especie == "perro":
                codigo = "Can0"+ str(cantidad_pacientes)
            
            elif cantidad_pacientes < 1000 and cantidad_pacientes >= 100 and especie == "gato":
                codigo = "Fel0"+ str(cantidad_pacientes)
            
            elif cantidad_pacientes < 1000 and cantidad_pacientes >= 100 and especie == "perro":
                codigo = "Can0"+ str(cantidad_pacientes)

            lista_individual =[nombre,especie,edad,estado,codigo]
            lista_global.append(lista_individual)

            if especie == "gato":
                lista_gatos.append(lista_individual)
            elif especie == "perro":
                lista_perros.append(lista_individual)
            break

    elif des == 2:
        print(f"Tenemos ingresados {(len(lista_perros))} perros y {(len(lista_gatos))} gatos en el consultorio para un total de {len(lista_global)} mascotas")

    elif des == 3:
         promedio_edades = sum(edades)/cantidad_pacientes
         print(f"El promedio de las edades de los animales ingresados es de {promedio_edades}")

    elif des == 4:
        print(f"La cantidad de mascotas graves es de {graves} y de mascotas en estado critico es de {criticos}")

    elif des == 5:
        busca_nombre =str(input("Digite el nombre de su mascota: ")).lower()
        busca_codigo = str(input("Digite el codigo que se le proporciono a su mascota: "))
        p = 0
        for x in range (cantidad_pacientes):
            if busca_nombre == lista_global[x][0] and busca_codigo == lista_global[x][4]:
                print(f"""Hemos encontrado a su mascota en la base de datos y esta registrado con los siguientes datos:
                \rNombre: {lista_global[x][0]}
                \rEspecie: {lista_global[x][1]} 
                \rEdad: {lista_global[x][2]}
                \rEstado: {lista_global[x][3]}
                \rCodigo: {lista_global[x][4]}""")
                p = 1
        if p == 0:
                print(f"lamentamos inforamr que su mascota {busca_nombre} con supuesto codigo {busca_codigo} no esta en nuestra base de datos")

    elif des == 6:
        p = 0
        for x in range (cantidad_pacientes):
            p += 1
            print(f"""El paciente numero {p} tiene los siguientes datos:
                \rNombre: {lista_global[x][0]}
                \rEspecie: {lista_global[x][1]} 
                \rEdad: {lista_global[x][2]}
                \rEstado: {lista_global[x][3]}
                \rCodigo: {lista_global[x][4]}""")

    elif des == 7:
        for x in range (2):
            salida = int(input("""
                            \r1- Confirmar salida 🤙.
                            \r2- Recharzar salida ❌.
                            """))
            
            if salida == 1:
                break
            elif salida == 2:
                break
            else:
                print("Ingrese la opción correcta 🚫.")

        if salida == 1:
            break
        elif salida == 2:
            continue
    
    else:
        print("Digite valores de entre 1 y 7 solamente")
        continue