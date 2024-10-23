#Crea un programa que pida al usuario que introduzca una cadena de texto. El programa debe imprimir la cadena de texto en mayúsculas y rodeada de signos de admiración.

cadena = input("Introduzca una cadena de texto: ")

cadena_modificada = ("¡" + cadena.upper() + "!")

print (cadena_modificada)