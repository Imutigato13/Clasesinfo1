n = int(input("Introduce el numero de veces a realizar la sumatoria: "))
a = int(input("Introduce el valor del denominador: "))
y = []

for n in range(1, n+1):
 digito = (1/a)**n
 y.append(digito)

z = sum(y)
print(f"El resultado de la sumatoria realizada es: {z}")