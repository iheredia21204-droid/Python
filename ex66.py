def valors_coincideixen(llista):
    """
    Retorna el nombre d'elements on el valor coincideix amb l'índex.
    """
    return sum(1 for idx, valor in enumerate(llista) if idx == valor)

# Proves
llista1 = [0, 2, 3, 3, 4]
llista2 = [0, 1, 2, 3, 4]
llista3 = [5, 6, 7]

print(valors_coincideixen(llista1))  # Retorna 3
print(valors_coincideixen(llista2))  # Retorna 5
print(valors_coincideixen(llista3))  # Retorna 0
