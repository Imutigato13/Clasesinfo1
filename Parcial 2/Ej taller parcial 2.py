diccionario = {}
producto_individual = []
cont = 0

def validar (msj):
    while True:
        try:
            a = int (input(msj))
            return a
        except:
            print("Solo valores numericos")

print("Bienvenido al sistema de almacenamiento de activos hospitalarios")

while True:
    cont += 1
    des = int(input("""
                    \r1. Ingrese un activo
                    \r2. Buscar un activo
                    \r3. Modificar un activo
                    \r4. Salir
                    \r: """))
    
    if des == 1:
        while True:
            
            zone = int(input("""¿A que zona esta destinado este activo?
                             \r1. Biomedica
                             \r2. Sistemas
                             \r3. Infraestructura
                             \r: """))
            nombre = input("Introduzca el nombre de la activo: ").capitalize()
            marca = input("Introduzca la marca del activo: ").capitalize()
            serial = validar("Introduzca el serial de activo: ")
            d = int(input("Introduzca la frecuencia de mantenimiento del activo (En meses): "))
            
            if zone == 1:

                calibrar = input("Introduzca la frecuencia de calibracion del activo: ")

