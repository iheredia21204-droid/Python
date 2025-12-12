def eliminarcapicua(llista):
    """
    Retorna una nova llista sense el primer i l'últim element.
    """
    if len(llista) <= 2:
        return []  # Si la llista té 2 o menys elements, retorna llista buida
    return llista[1:-1]  # Talla la llista des del segon fins al penúltim element

# Proves
llista1 = [1, 2, 3, 4, 5]
llista2 = ['a', 'b', 'c', 'd']
llista3 = [10, 20]

print(eliminarcapicua(llista1))  # Retorna [2, 3, 4]
print(eliminarcapicua(llista2))  # Retorna ['b', 'c']
print(eliminarcapicua(llista3))  # Retorna []
