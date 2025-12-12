def index_paraula(llista, paraula):
    """
    Retorna l'índex de la paraula dins de la llista ordenada.
    Si no existeix, retorna -1.
    """
    try:
        return llista.index(paraula)
    except ValueError:
        return -1

# Proves
llista_paraules = ['anell', 'bicicleta', 'casa', 'gat', 'poma']

print(index_paraula(llista_paraules, 'casa'))    # Retorna 2
print(index_paraula(llista_paraules, 'cotxe'))   # Retorna -1
print(index_paraula(llista_paraules, 'gat'))     # Retorna 3
