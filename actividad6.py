import random

secreto = random.randint(1, 100)
intentos = []

print("Adivina un número entre 1 y 100.")

while True:
  entrada = input("Tu número: ")

  if not entrada.isdigit():
    print("Escribe un número válido.")
    continue

  numero = int(entrada)
  intentos.append(numero)

  if numero < secreto:
    print("Muy bajo.")
  elif numero > secreto:
    print("Muy alto.")
  else:
    print(f"¡Ganaste! Adivinaste en {len(intentos)} intentos.")
    print(f"Tus intentos fueron: {intentos}")
    break
