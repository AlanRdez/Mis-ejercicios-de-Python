print ("Calculadora de numeros enteros")


try:
    entero1 = int(input("Introduzca el primer numero entero: "))
    entero2 = int(input("Introduzca el segundo numero entero: "))

    if entero1 > entero2:
        print (entero1,"El primer numero es más tremendo que", entero2)
    elif entero1 < entero2:
        print ("El primer numero es más microscopico que", entero2)
    else:
        print ("El número es igual")
    
except ValueError:
    print("Por favor, introduzca un número entero válido.")
