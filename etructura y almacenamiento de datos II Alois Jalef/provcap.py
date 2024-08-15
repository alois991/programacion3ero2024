provincias={"Córdoba":"Córdoba","Buenos Aires":"La Plata", }


pciaBuscarValorCapital=input("Ingresar provincia a buscar capital: ")
#Buscamos el valor por clave, en este caso capital ingresando provincia
x = provincias[pciaBuscarValorCapital]
print("su capital es:",x)
print("_______________________")




for p, c in provincias.items():
    print(p, "-", c)