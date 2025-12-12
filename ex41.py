# Demanem un número menor de 100
while True:
    try:
        num = int(input("Introdueix un número menor de 100: "))
        if num < 100:
            break
        else:
            print("El número ha de ser menor de 100.")
    except ValueError:
        print("Introdueix un número vàlid.")

# Inicialitzem la suma
suma_quadrats = 0

# Recorrem els números restants de 4 en 4 fins a 0
for i in range(num - 4, -1, -4):  # Comença en num-4, va fins a 0 exclòs, pas -4
    suma_quadrats += i ** 2

print(f"La suma dels quadrats és: {suma_quadrats}")
