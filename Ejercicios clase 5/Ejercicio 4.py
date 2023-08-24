a = int(input("Digite un numero: "))
b = int(input("Digite otro numero: "))
c= int(input("Digite un ultimo numero: "))

if a > b and a > c:
    if b > c:
        print (f"El orden de mayor a menor de esos numeros es {a},{b},{c}")
    elif c > b:
        print (f"El orden de mayor a menor de esos numeros es {a},{c},{b}")
if b > a and b > c:
    if a > c:
        print (f"El orden de mayor a menor de esos numeros es {b},{a},{c}")
    elif c > a:
        print (f"El orden de mayor a menor de esos numeros es {b},{c},{a}")
if c > b and c > a:
    if a > b:
        print (f"El orden de mayor a menor de esos numeros es {c},{a},{b}")
    elif b > a:
        print (f"El orden de mayor a menor de esos numeros es {c},{b},{a}")
