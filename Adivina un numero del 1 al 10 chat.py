print ("Es hora de que leas mi mente")

numero = 7
eleccion = int(input("Di un numero del 1 al 10: "))
if eleccion == numero:
    print ("Adivinaste el número, ten una galleta")
elif 1 <= eleccion <= 10:
    print ("¡Casi, intentalo de nuevo!")
else:
    print ("El número debe ser del 1 al 10, intentalo de nuevo")
    
           