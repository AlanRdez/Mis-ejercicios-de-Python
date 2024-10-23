#Escribe un programa que cambie el color de un semáforo de "rojo" a "verde" y viceversa. 3 Si el semáforo está en "rojo", cambia a "verde". Si está en "verde", cambia a "rojo".

print ("Juego del semaforo")

semaforo = input ("Diga el color del semaforo: ").lower ()

if semaforo == "verde" :
    print ("El semaforo cambia a amarillo")
elif semaforo == "rojo":
    print ("El semaforo cambia a verde")
elif semaforo == "amarillo":
    print ("El semaforo cambia a rojo")
else:
    print ("Colores invalidos, ingrese un color valido")
    