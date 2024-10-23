#Crea un programa que pida al usuario que introduzca el nombre de su lenguaje de programación favorito. Si la cadena de texto es igual a "Python", el programa debe imprimir un mensaje que diga "¡Muy buena elección!". Si la cadena de texto es igual a "Java" o "C++", el programa debe imprimir un mensaje que diga "Buenas opciones también". Si la cadena de texto es igual a cualquier otra cosa, el programa debe imprimir un mensaje que diga "Esa opción es un poco rara, pero respetable".

lenguaje = input("Introduzca su lenguaje de programación favorito: ").lower()

if lenguaje == "python":
    print ("¡Muy buena elección")
elif lenguaje == "java" or lenguaje == "c++":
    print ("Buenas opciones también")
else:
    print ("Esa opción es un poco rara, pero respetable")
    
#El codigo sin corregir es este, la falla se encuentra en la siguiente linea 19 para que funcionen dos strings debe ser la herramienta de iguales a la variable
#En este caso no se debe de usar la funcion In ya que solo deseamos que la palabra Python este dentro
'''
lenguaje = input("Introduzca su lenguaje de programación favorito: ").lower()

if "python" in lenguaje:
    print ("¡Muy buena elección")
elif "Java" or "C++" in lenguaje: 
    print ("Buenas opciones también")
else:
    print ("Esa opción es un poco rara, pero respetable"
    '''