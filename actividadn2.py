suma_total = 0
contador_positivos = 0
contador_negativos = 0
contador_numeros = 0

print("Introduce números enteros (ingresa -1 para terminar):")

while True:
    numero = int(input("Número: "))
    
    if numero == -1:
        break
        
    suma_total += numero
    contador_numeros += 1
    
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1

# Evitar división por cero si el usuario ingresa -1 como primer valor
if contador_numeros > 0:
    promedio = suma_total / contador_numeros
else:
    promedio = 0

print("\n--- Resultados ---")
print(f"Suma total: {suma_total}")
print(f"Cantidad de positivos: {contador_positivos}")
print(f"Cantidad de negativos: {contador_negativos}")
print(f"Promedio: {promedio}")
