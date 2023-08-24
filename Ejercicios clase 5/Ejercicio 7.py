a = int(input("Introduce un numero: "))
b = int(input("Introduce un numero: "))
c = int(input("Introduce un numero: "))
d = int(input("Introduce un numero: "))

if a> b and a > c and a> d:
    x = a
if b> a and b > c and b> d:
    x = b
if c> b and c > a and c> d:
    x = c
if d> b and d > c and d> a:
    x = d
if a< b and a < d and a< c:
    y = a
if b< a and b < c and b< d:
    y = b
if c< b and c < a and c< d:
    y = c
if d< b and d < c and d< a:
    y = d
z = (x+y)
print(f"La sumatoria del numero mayor y menor de los numeros proporcionados es {z}")
