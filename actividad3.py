intentos = 0

while True:
    contrasena = input("Ingrese la contraseña: ")
    intentos += 1
    
    if contrasena == "admin123":
        break

print(f"¡Acceso concedido! Le tomó {intentos} intento(s) ingresar la contraseña correcta.")
