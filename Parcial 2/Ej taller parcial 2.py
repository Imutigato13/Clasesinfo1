Activos = {}
cont = 0

def validar (msj):
    while True:
        try:
            a = int (input(msj))
            return a
        except:
            print("Solo valores numericos")

def AcCode (zone,cont):
    if zone == 1:
        a = (f"B-2023-{cont}")
        return a
    elif zone == 2:
        a = (f"I-2023-{cont}")
        return a
    elif zone == 3:
        a = (f"S-2023-{cont}")
        return a

print("Bienvenido al sistema de almacenamiento de activos hospitalarios")

while True:
    cont += 1
    des = validar("""
                    \r1. Ingrese un activo
                    \r2. Buscar un activo
                    \r3. Modificar un activo
                    \r4. Salir
                    \r: """)
    
    if des == 1:
            zone = validar("""¿A que zona esta destinado este activo?
                             \r1. Biomedica
                             \r2. Sistemas
                             \r3. Infraestructura
                             \r: """)
            nombre = input("Introduzca el nombre de la activo: ").capitalize()
            marca = input("Introduzca la marca del activo: ").capitalize()
            serial = validar("Introduzca el serial de activo: ")
            frecuencia = validar("Introduzca la frecuencia de mantenimiento del activo (En meses): ")
            n_activo = AcCode(zone,cont)
            if zone == 1:
                calibrar = input("Introduzca la frecuencia de calibracion del activo: ")
                Activos[serial] = [serial,nombre,marca,frecuencia,calibrar,n_activo]
            elif zone == 2:
                Activos[serial] = [serial,nombre,marca,frecuencia,n_activo]
            elif zone == 3:
                Activos[serial] = [serial,nombre,marca,frecuencia,n_activo]
# Estudiar map y filter
    elif des == 2:
        busca = validar("Introduzca el seriado el equipo a buscar")
        info_busca = Activos.get(busca)

        if info_busca != None:
                