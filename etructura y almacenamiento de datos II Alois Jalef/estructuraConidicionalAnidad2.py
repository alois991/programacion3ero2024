lados=int(input("ingrese cantidad de lados:"))
if lados==4:
    L1=(input("ingrese valor del primer lado"))
    L2=(input("ingrese valor del segundo lado"))
    L3=(input("ingrese valor del tercer lado"))
    L4=(input("ingrese valor del cuarto lado"))
    if L1==L2 and L1==L3 and L1==L4:
     print("es un cuadrado o rombo")
elif lados==3:
   print("es un triangulo o paralelogramo")    

