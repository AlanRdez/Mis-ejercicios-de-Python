#Hacer un programa que pida 3 números y determine cuál es el mayor.

numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))
numero3 = int(input("Digite el tercer numero: "))



if numero1 == numero2 and numero1 == numero3:
    print ("Todos los numeros son iguales")
elif numero1 >= numero2 and numero1 >= numero3:
    print ("El primer número es el mayor")
elif numero2 >= numero1 and numero2 >= numero3:
    print ("El segundo número es el mayor")
else:
    print ("El tercer número es el mayor")
   
    
