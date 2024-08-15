
intentos = 0
while intentos < 3:
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario == "alois jalef" and contraseña == "alois1":
        print("¡Bienvenido al sistema!")
        break
    else:
        intentos += 1
        if intentos < 3:
            print("Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")
        else:
            print("superaste el número de intentos permitidos. Adiós.")