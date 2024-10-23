print ("Bienvenido al simulador de batalla de Dark Souls")
camino = input("Te encuentras en el santuario del enlace de fuego, ¿qué camino tomas izquierda o derecha?: ")
objeto_llevado = False

if camino == "izquierda":
    objeto = input("Te encuentras con una espada encantada, ¿la equipas en tu inventario? si/no: ")
    if objeto == "si":
        objeto_llevado = True
        print ("Llevas equipada la espada encantada a +15")
    else:
        print ("No llevas equipada la espada encantada y continuas tu camino al cementerio de esqueletos")

    print ("Te encuentras muchos esqueletos que solo pueden morir con daño de encantamiento")
    if objeto_llevado == True:
        print ("Llevas la espada encantada a +15 y derrotas a todos los esqueletos. ¡Has ganado! puedes descansar en la hoguera")
    else:
        print ("No llevas la espada a +15 y los esqueletos vuelven a revivir ante cualquier ataque, te encierran y ¡HAS MUERTO!")

elif camino == "derecha":
    print ("Te encuentras con muchos enemigos y al fondo ves una puerta, tienes dos opciones pelear o huir")
    desicion = input ("¿Cuál es tu decisión?: ")
    if desicion == "pelear":
        print ("Son muchos enemigos, no puedes con ellos y te derrotan, ¡HAS MUERTO!")
    else:
        print ("Huyes por la puerta y te salvas. Has encontrado una nueva area, puedes descansar en la hoguera")
else:
    print ("No tomaste ninguna deicison y te vuelves hueco, ¡Has muerto!")
    
    
     
    
    
