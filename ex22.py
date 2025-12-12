def superposicio(llista1, llista2):
    """
    Retorna True si hi ha algun element en comú entre llista1 i llista2,
    False en cas contrari.
    """
    for element in llista1:
        if element in llista2:
            return True
    return False

# Exemples de prova
print(superposicio([1, 2, 3], [3, 4, 5]))  # True
print(superposicio([1, 2], [3, 4]))        # False
print(superposicio([], [1, 2]))            # False
print(superposicio([7, 8], [8, 9, 10]))    # True
