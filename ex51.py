def elimina_duplicats(llista):
    """
    Retorna una nova llista sense duplicats, mantenint l'ordre dels elements originals.
    """
    nova_llista = []
    for element in llista:
        if element not in nova_llista:
            nova_llista.append(element)
    return nova_llista

# Proves
llista1 = [1, 2, 2, 3, 4, 4, 5]
llista2 = ['a', 'b', 'a', 'c', 'b']

print(elimina_duplicats(llista1))  # Retorna [1, 2, 3, 4, 5]
print(elimina_duplicats(llista2))  # Retorna ['a', 'b', 'c']
