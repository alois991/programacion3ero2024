lista_de_socios = ["Alois", "nasim", "ernesto", "", "Leon"]
# Verificar si el socio existe en la lista y mostrar el resultado
# Solicitar al usuario que ingrese el nombre del socio a buscar
nombre_a_buscar = input("Ingrese el nombre del socio a buscar: ")
if nombre_a_buscar in lista_de_socios:
    print("{nombre-de-socio} existe en la lista de socios.")
else:
    print("[nombre-de-socio] no existe en la lista de socios,")
    
