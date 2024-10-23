#Crea un programa que pida al usuario que introduzca un número entero. Si el número es divisible por 3, el programa debe imprimir un mensaje que diga "¡DJ, pon la música de los 80s!". Si el número es divisible por 5, el programa debe imprimir un mensaje que diga "¡DJ, pon la música electrónica!". Si el número es divisible por 3 y por 5, el programa debe imprimir un mensaje que diga "¡DJ, pon la música de los 90s!". Si el número no es divisible por 3 ni por 5, el programa debe imprimir un mensaje que diga "¡DJ, pon la música de moda!".
numero = int(input("Introduzca un numero: "))

if numero %3== 0 and numero %5==0:
    print ("¡DJ, pon la música de los 90s!")
elif numero %5 == 0:
    print ("¡DJ, pon la música electrónica!")
elif numero %3 == 0:
    print ("¡DJ, pon la música de los 80s!")
else:
    print ("¡DJ, pon la música de moda!")

#Formula para sacar multiplos es %(numero) == 0