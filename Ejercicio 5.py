a = str(input("Nombre completo: " ))
b = int(input("Numero de inscripcion: "))
c = int(input("Patrimonio neto: "))
d = int(input("Estrato socioeconomico: "))
x = (50000)
if c >= 2000000 and d >= 3:
    x = (c*0.03) + x

print(f"Bienvenid@ a nuestra universidad {a} con numero de inscripcion {b}, tu total a pagar de matricula este semestre es de {x}")





