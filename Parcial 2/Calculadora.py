def verificar (des):
    x = 0
    while True:
        try:
            a = int (input(des))
            return a
        except:
            print("Solo valores numericos")
        x =+ 1
        if x == 5:
            break
des = verificar(""" \r1. Suma
                    \r2. Resta
                    \r3. Divisio
                    \r4. Multiplicacion
                    \r5. Salir
                    \r: """)