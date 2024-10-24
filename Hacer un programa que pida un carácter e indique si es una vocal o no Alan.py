#Hacer un programa que pida un carácter e indique si es una vocal o no.

letra = input("Escriba cualquier letra de la A a la Z: ").lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print ("La letra que introdujo son vocales")
else:
    print ("La letra que introdujo no cuentan como vocales")
    
#No es necesario str ya que no deseamos convertir algún numero a caracter o letra, ya que input entrega cadena de caracteres