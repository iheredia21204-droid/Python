def llista_a_diccionari(llista):
    """
    Retorna un diccionari on les claus són els elements de la llista
    i els valors són els seus índexs dins la llista.
    """
    return {valor: idx for idx, valor in enumerate(llista)}

# Proves
llista = ['casa', 'cotxe', 'cadira', 'taula']
print(llista_a_diccionari(llista))
# Retorna {'casa': 0, 'cotxe': 1, 'cadira': 2, 'taula': 3}
