print ("Calculadora de numeros enteros")

entero1 = int(input("Introduzca el primer numero entero: "))
entero2 = int(input("Introduzca el segundo numero entero: "))

if entero1 > entero2:
    print (entero1,"¡Vas por el camino correcto!")
elif entero2 > entero1:
    print ("¡Cuidado! Estás en un camino peligroso")
else:
    print ("Estás en un camino muy equilibrado")