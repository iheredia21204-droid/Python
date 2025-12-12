# Demanem el número
while True:
    try:
        num = int(input("Introdueix un número: "))
        break
    except ValueError:
        print("Valor invàlid. Introdueix un número enter.")

# Convertim a cadena per recórrer els dígits
digits_parells = [digit for digit in str(abs(num)) if int(digit) % 2 == 0]

# Mostrem els dígits parells
if digits_parells:
    print(f"Dígits parells del número {num}: {' '.join(digits_parells)}")
else:
    print(f"No hi ha dígits parells al número {num}.")
