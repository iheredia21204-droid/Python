# Demanem el número
while True:
    try:
        num = int(input("Introdueix un número: "))
        break
    except ValueError:
        print("Valor invàlid. Introdueix un número enter.")

# Convertim a cadena per recórrer els dígits i fem la suma
suma_digits = sum(int(digit) for digit in str(abs(num)))  # abs() per números negatius

# Mostrem la suma i si és parell o senar
print(f"La suma dels dígits és: {suma_digits}")
if suma_digits % 2 == 0:
    print("La suma és parell.")
else:
    print("La suma és senar.")
