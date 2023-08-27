n = int(input("Digite hasta que numero decea analizar: "))
x = 0
for n in range(1,n+1):
    if n % 2 != 0:
      x = n+x
 
print(f"La suma de los elementos impares entre 1 y el digito elegido es igual a {x}")
   
