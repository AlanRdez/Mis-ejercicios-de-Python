# Programa que convierte un número hexadecimal a un código PIN de 4 dígitos

def convertir_a_pin():
    # Solicitar un número hexadecimal al usuario
    hex_num = input("Introduce un número hexadecimal (ejemplo: 0x1234): ")

    try:
        # Convertir el número hexadecimal a un número entero
        pin_code = int(hex_num, 16)

        # Verificar si el número convertido tiene 4 dígitos
        if 1000 <= pin_code <= 9999:
            print(f"El número {hex_num} se convierte a {pin_code}, ¡es un PIN válido!")
        else:
            print(f"El número {hex_num} se convierte a {pin_code}, pero no es un PIN válido de 4 dígitos.")
    
    except ValueError:
        print("El valor ingresado no es un número hexadecimal válido.")

# Ejecutar la función
convertir_a_pin()
