cant_mediciones = int(input("Introduzca la cantidad de mediciones a introducir: "))
cont = 1
z = 1
y = []
while cont <= cant_mediciones:
 mediciones = float(input(f"Introduzca la medicion N.{z}: "))
 if mediciones > 30:
  print ("ALERTA. Temperatura crita superior a 30°")
 elif mediciones < 15:
  print("ALERTA. Temperatura critica inferior a 15°") 
 else:
  print("Rango normal")
  y.append(mediciones)
  cont += 1
  z += 1
x = sum(y)/cant_mediciones
print(f"El promedio de las mediciones fue {x}") 