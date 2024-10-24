#Hacer un programa que pida 2 números y se de cuenta cuál de ellos es par, o si ambos lo son.

numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))

if numero1 % 2 == 0 and numero2 %2==0:
    print("Ambos números son pares")
elif numero1 %2 == 0 and numero2 %2!=0:
    print (f"El primer número es par")
elif numero1 %2!=0 and numero2 %2 == 0:
    print (f"El segundo número es par") 
else:
    print("Ambos numeros son impares")
    
'''
Mi solución
# Programa que determina si los números son pares o impares
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos números son pares")
elif numero1 % 2 == 0:
    print("El primer número es par")
elif numero2 % 2 == 0:
    print("El segundo número es par")
else:
    print("Ambos números son impares")

'''

