# Nombres parells fins al 100
print("Nombres parells fins al 100:")
for i in range(2, 101, 2):  # Comença en 2, fins a 100, pas 2
    print(i, end=", " if i < 100 else "\n")  # Coma menys en l'últim

# Nombres senars fins al 99
print("\nNombres senars fins al 99:")
for i in range(1, 100, 2):  # Comença en 1, fins a 99, pas 2
    print(i, end=", " if i < 99 else "\n")
