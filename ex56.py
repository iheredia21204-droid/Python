# Demanem els dos números
while True:
    try:
        num1 = int(input("Introdueix el primer número: "))
        num2 = int(input("Introdueix el segon número: "))
        break
    except ValueError:
        print("Introdueix un número enter vàlid.")

# Assegurem que num1 sigui el menor i num2 el major
if num1 > num2:
    num1, num2 = num2, num1

# Calculem la suma
suma = sum(range(num1, num2 + 1))

print(f"La suma dels números entre {num1} i {num2} és: {suma}")
