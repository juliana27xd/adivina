# Buscar números perfectos entre 1 y 500
for numero in range(1, 501):
    suma_divisores = 0
    
    # Encontrar los divisores propios
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
            
    # Verificar si es un número perfecto
    if suma_divisores == numero:
        print(f"El número {numero} es perfecto.")
