y = []
for i in range(1124):
    z = []
    nombre = str(input("Introduzca su nombre: ")).upper()
    id = int(input("Introduzca su documento de identidad: "))
    edad = int(input("Introduzca su edad: "))
    EPS = str(input("Introduzca su EPS: ")).upper() 

    z.append(EPS)
    z.append(edad)
    z.append(id)
    z.append(nombre)
    y.append(z)
    while True:
        op = int(input("¿Decea ingresar la info de otro0 paciente? digite 1 para si y 2 para no. "))
        if op == 1:
            break
        elif op == 2:
            break
        else:
            print("Solo se aceptan los digitos 1 y 2 como respuesta")
    if op == 2:
        break
    elif op == 1:
        continue

print(f"Estos son los datos de todos los pacientes ingresados: {y}") 