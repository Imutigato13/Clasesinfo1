def calcular_potencia(b, e):
    return b ** e

n = int(input("Ingresa el valor a elevar (0-9): "))
x = int(input("Ingresa el valor exponete (positivo hasta 9): "))

if 0 <= n <= 9 and x > 0 and x <= 9:
    for e in range(n + 1):
        r = calcular_potencia(n, e)
        print(f"{n}^{e} = {r}")
else:
    print("Ingresa valores válidos para n y x.")