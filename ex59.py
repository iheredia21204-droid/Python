# Nombre inicial fins on comença la sèrie
for i in range(5, 0, -1):  # 5, 4, 3, 2, 1
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()  # Saltem de línia després de cada fila
