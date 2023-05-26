Carillas_porcerlana= 250000
Implantes_dentales= 475000
Ortodoncia= 800000
Descuento_Auxiliar="15%"
Descuento_administrativo="10%"
Descuento_docente="5%"
Carillas_con_descuentoAX= Carillas_porcerlana*0.15
Carillas_con_descuentoAD=Carillas_porcerlana*0.1
Carillas_con_DOC= Carillas_porcerlana*0.05
Implantes_con_descuentoAX= Implantes_dentales*0.15
Implantes_con_descuentoAD=Implantes_dentales*0.1
Implantes_con_descuentoDOC=Implantes_dentales*0.05
Ortodoncia_con_descuentoAX= Ortodoncia*0.15
Ortodoncia_con_descuentoAD= Ortodoncia*0.1
Ortodoncia_con_descuentoDOC= Ortodoncia*0.05




print("1.- Carillas_porcelana")
print("2.- Implantes_dentales")
print("3.- Ortodoncia")
print("4.- Salir")

 
tratamiento=int(input("Que tratamiento se va a hacer "))
if tratamiento==1:
        cantiadad_carillas=int (input("Cuantas carillas de porcelana se pondra "))
        Totalcarillas= cantiadad_carillas*Carillas_porcerlana
        print(f"El precio de las carillas de porcelana es {Totalcarillas}")
        print("a.-Descuento Auxiliar")
        print("b.-Descuento Trabajador Administrativo")
        print("c.-Descuento Trabajador Docente")
        descuento= input("¿Que descuento aplica? ")
        if descuento=="a":
            print(f"El precio con el Descuento Auxiliar es {Carillas_con_descuentoAX}")
        elif descuento=="b":
            print(f"El precio con el Descuento Administrativo es {Carillas_con_descuentoAD}")
        elif descuento=="c":
         print(f"El descuento con el Descuento Doncente es {Carillas_con_DOC} ")
if tratamiento==2:
    cantidad_implantes=int(input("Cuantos implantes se pondra"))
    Totalimplantes= cantidad_implantes*Implantes_dentales
    print(f"El precio de los implantes dentales es {Totalimplantes}")
    print("a.-Descuento Auxiliar")
    print("b.-Descuento Trabajador Administrativo")
    print("c.-Descuento Trabajador Docente")
    descuento= input("¿Que descuento aplica?")
    if descuento=="a":
        print (f"El precio con el Descuento Auxiliar es {Implantes_con_descuentoAX}")
    elif descuento=="b":
        print(f"El precio con el Descuento Administrativo es {Implantes_con_descuentoAD}")
    elif descuento=="c":
        print(f"El descuento con el Descuento Doncente es {Implantes_con_descuentoDOC}")
if tratamiento==3:
    print(f"La ortodoncia tiene un precio de {Ortodoncia}" )
    print("a.-Descuento Auxiliar")
    print("b.-Descuento Trabajador Administrativo")
    print("c.-Descuento Trabajador Docente")
    descuento= input("¿Que descuento aplica?")
    if descuento=="a":
        print(f"El precio con el descuento Auxiliar es {Ortodoncia_con_descuentoAX}")
    elif descuento=="b":
        print(f"El precio con el descuento Administrativo es{Ortodoncia_con_descuentoAD}")
    elif descuento=="c":
     print(f"El descuento con el Descuento Doncente es {Ortodoncia_con_descuentoDOC }")
elif tratamiento==4:
    print("adios")

    





    




