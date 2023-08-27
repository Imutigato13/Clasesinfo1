def calcular_potencia(b, e):
    return b ** e

n = int(input("Ingresa el valor a elevar (0-9): "))
x = int(input("Ingresa el valor exponente (positivo hasta 9): "))

if 0 <= n <= 9 and x > 0 and x <= 9:
    for x in range(x + 1):
        r = calcular_potencia(n, x)
        print(f"{n}^{x} = {r}")
else:
    print("Ingresa valores válidos para n y x.")
