while True:
 n = int(input("Introduce el numero al que deceas saber su factorial: "))
 x = 1

 if n >= 0 and n <= 20:
    for n in range(1,n+1):
     x *= n
    print(f"El factorial de {n} es {x}")
 else:
    print("Digite valores de entre 0 a 20")
 while True:
   a = str(input("¿Decea volver a calcular el factorial de otro numero?. Escriba si para volver a calcular y no para finalizar el programa: ")).lower()
   if a == "si":
    print("Entendido :D")
    break
   elif a == "no":
    print("Hasta luego :D")
    break
   else:
    print("Solo se admiten las palabras si o no para esta seleccion")
 if a == "no":
  break