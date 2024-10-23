numero = int(input("Introduzca un numero: "))
secreto = 8
if numero == secreto:
    print ("El numero es correcto")
elif 1 <= numero <=100:
    print ("Intentalo de nuevo")
else:
    print ("Invalido")
    
'''
Para explicar el rango de 1 a 100 o cualquier nombre se tiene que
colocar primero 1 <= Variable, y el numero que será el limite,
expresada de la siguiente manera <= 100
'''