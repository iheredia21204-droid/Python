def menu_principal():
    opcio=0
    while opcio<1 or opcio>3:
        opcio = int(input("""Elegeixi una opció:
                          1. calculadra decimal
                          2. calculadora real (floats)
                          3. sortir \n"""))
        if opcio>0 and opcio<4:
            return opcio
        else:
            print("L'opció seleccionada no és correcte, torni-ho a provar!!\n")
def menu_calculadora():
    opcio=0
    while opcio<1 or opcio>5:
        opcio=int(input("""Elegeixi una opció:
                        1. Suma
                        2. Resta
                        3. Multiplicació
                        4. Divisió
                        5. Sortir
                        """))
        if opcio>0 and opcio<6:
            return opcio
        else:
            print("L'opcio seleccionada no és correcte, torni-ho aprovar!! \n")
        op=0
def calculadora_decimal(opcio):
    if opcio>0 and opcio<6:
        a = int(input("Introduexi el primer número: "))
        b = int(input("Introduexi el segon número: "))
    match(opcio):
        case 1:
            #suma
            print("Estic fent la suma! \n")
            c = a + b
            print("El resultat de sumar {} + {} és {}".format(a, b,c))
        case 2:
            #resta
            print("Estic fent la resta! \n")
            c = a - b
            print("El resultat de restar {} - {} és {}".format(a, b,c))
        case 3:
            #multiplicacio
            print("Estic fent la multiplicació! \n")
            c = a * b
            print("El resultat de multiplicació {} * {} és {}".format(a, b,c))
        case 4:
            # Divisió 
            print("Estic fent la divisió! \n")
            c = a // b
            print("El resultat de dividir {} / {} és {}".format(a, b,c))
        case _:
            print("Gràcies, fins aviat! \n")
def calculadora_real(opcio):
    if opcio>0 and opcio<6:
        a = float(input("Introduexi el primer número: "))
        b = float(input("Introduexi el segon número: "))
    match(opcio):
        case 1:
            #suma
            print("Estic fent la suma! \n")
            c = a + b
            print("El resultat de sumar {} + {} és {}".format(a, b,c))
        case 2:
            #resta
            print("Estic fent la resta! \n")
            c = a - b
            print("El resultat de restar {} - {} és {}".format(a, b,c))
        case 3:
            #multiplicacio
            print("Estic fent la multiplicació! \n")
            c = a * b
            print("El resultat de sumar {} * {} és {}".format(a, b,c))
        case 4:
            # Divisió 
            print("Estic fent la divisió! \n")
            c = a / b
            print("El resultat de sumar {} / {} és {}".format(a, b,c))
        case _:
            print("Gràcies, fins aviat! \n")

#Programa prinicipal
op = 1
while op!=0:
    op = menu_principal()
    if op==1:
        # Calculadora decimal
        print("Estic passant pero la calculadora decimal! \n")
        calculadora_decimal(menu_calculadora())
    elif op==2:
        # Calculadora real
        print("Estic passant per la calculadora real! \n")
        calculadora_real(menu_calculadora())
    else:
        print("Gràcies per a utilizar la meva calculadora, fins un altre dia! \n")
        op=0