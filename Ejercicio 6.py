masa1 = float(input("Ingresa la masa de la esfera 1: "))
vol1 = float(input("Ingresa el volumen de la esfera 1: "))

masa2 = float(input("Ingresa la masa de la esfera 2: "))
vol2 = float(input("Ingresa el volumen de la esfera 2: "))

masa3 = float(input("Ingresa la masa de la esfera 3: "))
vol3 = float(input("Ingresa el volumen de la esfera 3: "))

densidad1 = (masa1/ vol1)
densidad2 =  (masa2/ vol2)
densidad3 =  (masa3/ vol3)


if densidad1 > densidad2 and densidad1 > densidad3:
    mayor = "esfera 1"
elif densidad2 > densidad1 and densidad2 > densidad3:
    mayor= "esfera 2"
else:
    mayor = "esfera 3"

print(f"La esfera de mayor densidad es la {mayor}")





