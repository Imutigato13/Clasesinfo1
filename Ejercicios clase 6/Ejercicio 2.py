print("Bienvenido al sistema de calculo de promedio estudiantil, tome en cuenta que todas las notas tienen igual porcentaje en el total de la materia")
x = 0
a = 0
b = int(input("¿Cuantas notas tienes en tu materia?: "))
c = b
s = 1
while True:
    a = float(input(f"Nota {s}: "))
    x = a+x
    b -= 1
    s += 1
    if b == 0:
        break
z = x/c
print(f"El promedio de tus notas es igual a: {z}")