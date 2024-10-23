print ("Cuantos años tiene tu mascota en años humanos")

mascota = input("Introduzca la especie de su mascota: ").lower ()
edad = int(input("Introduzca la edad de su mascota: "))

if mascota == "perro":
    edad = edad * 7
    print (edad)
elif mascota == "gato":
    edad = edad* 5
    print (edad)
else:
    print ("Especie invalida")
