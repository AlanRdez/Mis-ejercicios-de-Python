#Crea un programa que pida al usuario que introduzca dos números enteros. El programa debe imprimir un mensaje que diga si el primer número es mayor, menor o igual al segundo número, pero en lugar de usar las palabras "mayor" o "menor", debes usar palabras divertidas como "tremendote" o "microscópico".

print ("Calculadora de numeros enteros")

entero1 = int(input("Introduzca el primer numero entero: "))
entero2 = int(input("Introduzca el segundo numero entero: "))

if entero1 > entero2:
    print (entero1,"El primer numero es más tremendo que", entero2)
elif entero1 < entero2:
    print ("El primer numero es más microscopico que", entero2)

                    
                