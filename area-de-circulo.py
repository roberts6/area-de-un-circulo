import math

# 1. Solicitar que se ingrese el radio del círculo como cadena de texto
radio = input("Por favor, ingrese el radio del círculo: ")

# Reemplazar la coma por un punto si el usuario la ingresó
radio = radio.replace(',', '.')

# Convertir el radio a un número decimal (float)
radio = float(radio)

# 2. Calcular el área del círculo utilizando la fórmula area = pi * radio^2 
area = math.pi * (radio ** 2)

# Redondear el área a 2 decimales
area_redondeada = round(area, 2)

# 3. Mostrar al usuario el resultado del área calculada
print(f"El área del círculo con radio {radio} es: {area_redondeada}")
