# Solicitamos al usuario cuántos términos desea generar
n_terminos = int(input("¿Cuántos términos de la serie de Fibonacci deseas generar? "))

# Inicializamos los dos primeros números de la serie
a, b = 0, 1

# Validamos que el número ingresado sea positivo
if n_terminos <= 0:
    print("Por favor, ingresa un número entero positivo.")
elif n_terminos == 1:
    print(f"Serie de Fibonacci de {n_terminos} término:")
    print(a)
else:
    print(f"Serie de Fibonacci de {n_terminos} términos:")
    for _ in range(n_terminos):
        print(a, end=" ")
        # Actualizamos los valores: 'a' toma el valor de 'b', y 'b' la suma de ambos
        a, b = b, a + b
