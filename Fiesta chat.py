
'''
Crea un programa que pida al usuario que introduzca una cadena de texto. Si la cadena de texto contiene la palabra "fiesta", el programa debe imprimir un mensaje que diga "¡Fiesta, fiesta, fiesta!". Si no la contiene, el programa debe imprimir un mensaje que diga "No hay fiesta sin tí :("
'''

entrada = input("¿Quieres venir a la fiesta o quedarte en casa?: ").lower()

if "fiesta" in entrada:
    print (f"¡Fiesta, fiesta, fiesta!")
else:
    print (f"No hay fiesta sin tí :(")