producto = input("Añada el nombre de su producto: ").lower()
precio = float(input("Cuál es el precio de su producto: "))
descuento = precio * 0.15
final = precio - descuento


print (f"El producto {producto} Tiene 15% de descuento así que su producto tendrá un precio de {final}")