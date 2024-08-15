temperatura=float(input("Ingrese la temperatura en este momento:"))
PlatosFrios=["Ensalada","Helado"]
PlatosCalientes=["Guiso","Pescado al horno"]
if temperatura>=25:
    print("El menu sugerido para este tiempo de calor es:", PlatosFrios)
else:
    print("El menu sugerido para este tiempo de frio es:", PlatosCalientes)