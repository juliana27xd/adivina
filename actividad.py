# Solicitamos el número entero al usuario
numero = int(input("Introduce un número entero: "))

# Creamos un ciclo que va del 1 al 12
for i in range(1, 13):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
