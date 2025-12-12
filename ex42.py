# Demanem el número amb comprovació de rang
while True:
    try:
        num = int(input("Introdueix un número (1 - 900000): "))
        if 1 <= num <= 900000:
            break
        else:
            print("Número fora del rang. Torna-ho a provar.")
    except ValueError:
        print("Valor invàlid. Introdueix un número enter.")

# Mètode 1: convertir a cadena i comptar caràcters
num_digits = len(str(num))

print(f"El número {num} té {num_digits} dígits.")
