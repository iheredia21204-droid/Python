# Demanem el capital inicial amb comprovació de rang
while True:
    try:
        capital_inicial = float(input("Introdueix la quantitat a sol·licitar (50.000€ - 800.000€): "))
        if 50000 <= capital_inicial <= 800000:
            break
        else:
            print("Quantitat fora del rang. Torna-ho a provar.")
    except ValueError:
        print("Valor invàlid. Introdueix un número.")

# Demanem l'interès amb comprovació de rang
while True:
    try:
        interes = float(input("Introdueix l'interès (%) (0.5 - 13): "))
        if 0.5 <= interes <= 13:
            break
        else:
            print("Interès fora del rang. Torna-ho a provar.")
    except ValueError:
        print("Valor invàlid. Introdueix un número.")

# Demanem el nombre d'anys amb comprovació de rang
while True:
    try:
        anys = int(input("Introdueix el número d'anys (3 - 40): "))
        if 3 <= anys <= 40:
            break
        else:
            print("Nombre d'anys fora del rang. Torna-ho a provar.")
    except ValueError:
        print("Valor invàlid. Introdueix un número enter.")

# Calculem el capital final
capital_final = capital_inicial * (1 + interes/100) ** anys

# Mostrem el resultat amb 2 decimals
print(f"\nEl capital final després de {anys} anys serà: {capital_final:.2f}€")
