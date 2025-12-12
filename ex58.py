def elements_parells(llista):
    """
    Retorna una nova llista amb els elements de la llista original que estiguin en posicions parells.
    """
    return llista[0::2]  # Comença a l'índex 0, pas 2

# Proves
llista_paraules = ["Hola", "Adéu", "Casa", "Cotxe", "Gat", "Perro"]
print(elements_parells(llista_paraules))  # Retorna ['Hola', 'Casa', 'Gat']
