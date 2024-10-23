edad = int(input("Digite su edad: "))

if edad >1 and edad <100:
    print ("Edad Correcta")
    if edad >= 18:
        print ("Eres mayor de edad")
    elif edad >0:
        print("Pero eres menor de edad")
else:
    print ("Digite un numero correcto")