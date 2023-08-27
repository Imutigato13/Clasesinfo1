n = int(input("Digite hasta que numero decea analizar"))
x = 0
for n in range(1,n+1):
    if n % 2 != 0:
      x = n+x
      print(f"X en esta iteracion es igual a {x}")
print(f"X es igual a {x}")
   