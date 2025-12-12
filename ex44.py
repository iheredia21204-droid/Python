# Demanem el número amb comprovació de rang
while True:
    try:
        num = int(input("Introdueix un número per a la taula de multiplicar (1-20): "))
        if 1 <= num <= 20:
            break
        else:
            print("Número fora del rang. Torna-ho a provar.")
    except ValueError:
        print("Valor invàlid. Introdueix un número enter.")

# Imprimim la taula de multiplicar
print(f"\nTaula de multiplicar de {num}:")
for i in range(1, 11):  # Normalment es fa del 1 al 10
    print(f"{num} x {i} = {num * i}")
