# Solicitar el número al usuario
numero = int(input("Ingrese un número entero positivo: "))

# Bandera para indicar si es primo
es_primo = True

# Validar que sea un número mayor a 1
if numero <= 1:
    es_primo = False
else:
    # Ciclo para verificar divisores desde 2 hasta la raíz del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break  # Rompe el ciclo si encuentra un divisor

# Mostrar el resultado según la bandera
if es_primo:
    print(f"{numero} es un número PRIMO.")
else:
    print(f"{numero} NO es un número primo.")
