a = float(input("Ingresa la nota del primer parcial: "))
b = float(input("Ingresa la nota del segundo parcial: "))
c = float(input("Ingresa la nota del tercero parcial: "))
d = float(input("Ingresa la nota del cuarto parcial: "))
e = float(input("Ingresa la nota del quinto parcial: "))

f = ((a*0.30)+(b*0.15)+(c*0.15)+(d*0.20)+(e*0.20))

if f > 5:
    print("Esa nota es imposible, vuelve a digitar tus notas")
elif f < 0:
    print("Esa nota es imposible, vuelve a digitar tus notas")
elif f >= 3:
    print(f"Tu promedio es de {f} por lo que pasaste la materia :D" )
elif f< 3:
    print (f"Tu promedio es de {f} por lo que no pasate la materia :c")
