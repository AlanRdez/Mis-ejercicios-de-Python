print ("Es hora de que leas mi mente")

import random
numero = random.randint (1,10)
eleccion = int(input("Di un numero del 1 al 10: "))
if eleccion == numero:
    print ("Adivinaste el número, ten una galleta")
else:
    print ("Intentalo de nuevo")