import math

# 1. solicitar que se ingrese el radio del círculo y castear a flotante ya que el input devuelve un str
radio = float(input("por favor ingrese el radio del círculo: "))

# Reemplazar la coma por un punto si el usuario la ingresó
radio = radio.replace(',', '.')

# 2. calcular el área del círculo, utilizando la fórmula area = pi * radio^2 
area = math.pi * (radio ** 2)

# Redondear el área a 2 decimales
area_redondeada = round(area, 2)

# 3. Mostrar al usuario el resultado del área calculada
print(f"El área del círculo con radio {radio} es: {area_redondeada}")